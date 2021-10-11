# Analysis and Classification of Anopheles Populations in AG1000-3R dataset using Intergenic SNPs
### [Target-Malaria Group](https://targetmalaria.org) in Burt Lab, Imperial College London

## Objectives Covered
* __Exploratory Data Analysis__
  * SNPs Filtering Statistics 
  * Minor Allele Filtering - Exploring the right MAF threhsold for rare allele filtering while preserving private alleles
  * Unsupervised exploration - PCA and UMAP visualizations for 4.8 Million SNPs and sampples from 16 populations. UMAP hyperparameter tunining for chromosome arm 3R.
* __Classification of 13 Populations__
  * Pipeline for population classification using genetic sequences
  * Futher improvement through dimensionality reduction and domain related techniques
* __Pairwise analysis of 66 population pairs__
* __Exploring SNP contribution and importance for population differentiation__
* __Generic Python functions to reproduce and automate most of the analyses__

## Dataset
* MalariaGen AG1000 Phase 2 AR1 release
* 2,284 Haplotypic samples or 1,142 individual samples from 16 populations -
> BFcol, BFgam, AOcol, CIcol, CMgam, FRgam, GAgam, GHcol, GHgam, GM, GNcol, GNgam, GQgam, GW, KE, and UGgam
* 4,836,295 ___Intergenic SNPs___ from chromosome arm 3R
* Phased Haplotype data/biallelic (0 or 1)

<img src=/plots/UMAP_all_unscaled_jaccard_n50_unsupervised_2.png width="450" height="350"> <img src=/plots/UMAP_all_unscaled_jaccard_n15_unsupervised_c.png width="450" height="350">
