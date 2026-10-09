
# GlacierMIP3 Part B -> analyse glacier model differences
... TODO add more documentation here ... 

- `PartB_0x_individual_glacier_check.ipynb` 
    - checks if individual glacier interannual variability coincides between glacier models
    - looks at per-glacier files!!!
    - PyGEM' interannual variability coincides well with the one from OGGM & OGGM-VAS, but GloGEMFlow's interannual variability does not coincide at all with them 


- `PartB_0_area_vs_volume_response_time.ipynb`
    - non-shifted response timescale estimated at mass/area shrinkage rates of -50%, -80% and -90%. The response timescales is only computed if at least 25% of the mass/area is lost (otherwise the noise is too large)...
    - The following file is created, which is later used in other notebooks for the analysis and visualisations:
`'../PartB_data/resp_time_non_shifted_for_deltaT_rgi_reg_roll_volume_area_21yravg.csv'`
    - (very similar to http://localhost:7269/lab/tree/www_lschuster/GlacierMIP3/0_pre_post_processing/0e_response_timescale_estimates.ipynb, but here for the non-shifted, and for both volume and area!!!)

!!! `delta ... to median model` columns of csv files. TODO: remove maybe this column for the file at the end because it also includes OGGM-VAS to get to the median ... 


- `PartB_1_annual_variability.ipynb` (***only interesting for GlacierMIP3 Part 2***)
    - shows the differences in the interannual regional volume variability between the glacier models (some models, specifically GloGEM-family, do not correlate with the other models)
    - can not do that properly due to some strange things done in some models
    
- `PartB_1_glacier_model_differences_first trials.ipynb` (***only interesting for GlacierMIP3 Part 2***)
 
- `PartB_3_glacier_model_differences.ipynb` (***only interesting for GlacierMIP3 Part 2***)
    - plot the difference period - ref_peroid for each glacier model -> filter out downscaling difference 
        - look at differences between time series to reduce the downscaling influence  (as downscaling is different for every glacier model)
        - not sure how to go on with that! 
        