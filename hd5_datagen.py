import pandas as pd
import numpy as np
import os
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

home = os.path.expanduser('~')
directory = os.path.join('Imp_Research','Dataset')

populations = ['CIcol','CMgam','FRgam','GAgam','GHcol','GHgam','GM','GNcol','GNgam','GQgam','GW','KE','UGgam']
chromo_arms = ['3R','3L']
for population in populations:
    for arm in chromo_arms:
        pop_name = population+'.'+arm
        print(f'File in progress : {pop_name}\n')
        filename = f'haplotype.intergenic.{pop_name}.Rdata'
        data_path = os.path.join(home, directory, filename)
        store_path = os.path.join(home,directory,"HDF_Dataset")

        data = robjects.r['load'](data_path)
        # storing transpose of Haplotype because sk-allel takes SNP x samples as input
        haplotype = np.array(robjects.r['haplotype'],dtype=np.uint8).T
        POS = np.array(robjects.r['POS'])

        # To read the dataset, keys present in name can be used : 'Haplotype' and 'POS'
        storefile = os.path.join(store_path, f'Haplotype.POS.{pop_name}.hd5')
        hap = pd.DataFrame(haplotype).astype('int8')
        pos = pd.DataFrame(POS)
        # To prevent out of memory error Delete the variables
        del haplotype, POS
        hap.to_hdf(storefile,key='Haplotype',format='fixed',mode='w',complevel=9)
        del hap
        pos.to_hdf(storefile,key='POS',format='fixed',mode='a',complevel=9)
        del pos

