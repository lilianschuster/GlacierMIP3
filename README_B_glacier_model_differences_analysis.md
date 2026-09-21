
# GlacierMIP3 Part B -> analyse glacier model differences
... TODO add more documentation here ... 

- `PartB_0x_individual_glacier_check.ipynb` (***only interesting for GlacierMIP3 Part 2***)
    - checks if individual glacier interannual variability coincides between glacier models
    - looks at per-glacier files!!!
    - PyGEM' interannual variability coincides well with the one from OGGM & OGGM-VAS, but GloGEMFlow's interannual variability does not coincide at all with them 

- `PartB_1_annual_variability.ipynb` (***only interesting for GlacierMIP3 Part 2***)
    - shows the differences in the interannual regional volume variability between the glacier models (some models, specifically GloGEM-family, do not correlate with the other models)
    - can not do that properly due to some strange things done in some models
    
- `PartB_1_glacier_model_differences_first trials.ipynb` (***only interesting for GlacierMIP3 Part 2***)
 
- `PartB_3_glacier_model_differences.ipynb` (***only interesting for GlacierMIP3 Part 2***)
    - plot the difference period - ref_peroid for each glacier model -> filter out downscaling difference 
        - look at differences between time series to reduce the downscaling influence  (as downscaling is different for every glacier model)
        - not sure how to go on with that! 
        