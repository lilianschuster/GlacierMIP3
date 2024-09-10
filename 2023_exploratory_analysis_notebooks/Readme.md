# Notebook overview:
Most recent postprocessing date: `DATE = "Feb12_2024"`

Pre and postprocessing is described in [README_0_pre_post_processing](README_0_pre_post_processing).
 
### 1: First Analysis without really using temperature data

- `1_overview_timeseries_plots.iypnb` 
    - creates simple volume time series plots for every RGI region, and then also for every GCM separately (plots inside of `figures/1_overview_timeseries_plot`)
    - also creates some test figures to analyse whether steady-state is reached *(not updated to IPCC AR6 stuff)*
        - however, the issue is that the timing of steady-state depends a lot on the definition
        - will instead use a figure from 3_response_time_analysis_with_2020_shift.ipynb as supplemental figure!!! (then we show already in the same figure also the time to reach 50 or 80% of the total changes

    


### 2: Now compare dta relative to temp. change data 
- `lowess_fits/lowess_percentile_interval_fit_per_region_added_uncertainties.py` 
    - need to execute the lines of `commandos_slurm.txt`
    - python scripts to create the lowess fits with uncertainties 
    - creates csv files with the lowess best frac fits: 
        - e.g.: `lowess_fits/fitted_lowess_best_frac_shift_years_rel_2020_101yr_avg_period_lowess_added_quantiles_added_current12deg_5000_{DATE}_ipcc_ar6.csv`
    - creates csv files with the exponential fit (just for comparison), here the "shifted variant":
        - e.g.: fitted_lowess_best_frac_shift_years_rel_2020_101yr_avg_period_lowess_added_quantiles_added_current12deg_5000_{DATE}_ipcc_ar6.csv
    - creates rather complex figure variants of Fig.2 of the manuscript (figures are in 2a_lowess_fits) :
        - those are simplified later in `2a_glacier_vs_climate_change_evolution.ipynb`
    - ipcc srocc fits are in lowess_fits/fits_with_ipcc_srocc


- `per_glacier_lowess_calib/lowess_percentile_interval_fit_per_model_per_region.py` :
    - python scripts to create the per-glacier lowess fits 
        - (necessary to assess glacier model uncertainties of the temperature sensitivities)
        - same csv files as in lowess_fits/...
        - figures are in 2a_lowess_fits 


- `2a_glacier_vs_climate_change_evolution.ipynb` 
    - global plot, and for every RGI region, showing results by always using median (and quantiles) of glacier models 
    - creates figures inside of `2_timeseries_temp_ch_reg_glob` and the Fig. `2_condensed_rgi_region_analysis.png` 
         - manuscript figure 1, 2 (TODO: need to update the figure to show LOWESS fit with uncertainties instead of exp. fit)
         - actually Fig. 1 needs the fits that are shown in 
    - creates figures of global vs regional warming (for supplements)
    - creates supplemental figures with x-axis the RGI regions and as y-axis ... (allow to also show uncertainties): 
        - steady-state statistics with uncertainties (1.2°C ice loss, temp. sensitvities - TODO _> update and add uncertainties)
    
- `2b_find_equilibrium_steady_state_yr.ipynb`
    - find steady-state year (used at the moment for one supplemental figure)


- `2depr_analysis_regional_glacier_vs_climate_change.ipynb` 
    - comparison of glacier changes to global or glacier regional climate changes 
    - does not do the shift in the simulation years, but maybe good to keep it here for the moment, as it gives a quick overview of the non-shifted estimates ... 
    - **(at the moment not anymore used for anything in the manuscript)**
    
### 3: further analysis of steady state, time to reach 50 or 80% of the total changes, and of regional characteristics related to these regional differences

- `3a_response_time_analysis_with_2020_shift.ipynb`
    - time to reach 50 or 80% of the total changes (median over all models
        - also done for every glacier model separately (but this uses the "unshifted" data (to check!!!)
        - creates supplemental figures of "Time to reach 50%/80 % of the changes statistics" 
    - `3depr_response_time_analysis.ipynb`:
        - old version without a simulation year shift (maybe nice for GlacierMIP3 Part 2 study)
        
- `3b_extract_regional_climatic_glacier_median_response_time_characteristics.ipynb`
    -  extracts all the regional glacier/climate and response time characteristics and saves them under:
        - creates '3_shift_summary_region_characteristics.csv'
    - `3depr_fitted_glacier_response_clustering_all_exp_OLD.ipynb`:
        - also includes exponential fit clustering
        - deprecated
    - `3depr_fitted_glacier_response_clustering_temp_above_0_8.ipynb`:
        - this is the same (but an older version notebook), thatonly used exponential fits with experiments with data >=0.8°C
        - deprecated 

- `3c_lowess_shifted_fit_region_characteristics_glacier_response.ipynb`
   - does the K-means clustering
   - creates Fig. 3b,c,d

- `3x_create_fig4.ipynb`
    - creates Fig. 4


### 4: further aggregated figures such as the world map

- `4_world_map_figure.ipynb`
    - world map plot created 
    - (the subplots that go below the world map are created in `3_lowess_shifted_fit_region_characteristics_glacier_response.ipynb`)

### discussion analysis
- `5_comparison_to_marzeion_et_al_2018.ipynb`
    - Comparison of the GlacierMIP3 results (relative to inventory date) to those from Marzeion et al., (2018)
    
- `5_comparison_to_zekollari_et_al_2024.ipynb`
    - comparison to the 2100 projections

- `5x_RGI04_barnes_ice_cap_analysis.ipynb`
    - analysis of per-glacier files just for the Barnes Ice cap RGI IDs

- `5_tests_for_conversion_to_SLR_equivalent.ipynb`
    - at the moment just includes a test how to use OGGM to get a fit of how much glacier volume bsl is lost vs total volume -> fit would need to be repreated for every RGI region ... 

### Supplementary Data
- `6_csv_tables_creation.ipynb`
    - creates table for suppl. information about current and past volume changes (+ some regional characteristics, such as regional glacier surface slope)
    - creates aswell table with steady-state regional glacier volume estimates with uncertainties ...
    - ... what other tables do we need ? 
        - TODO: maybe time to reach 80% of the total changes for the different regions??? 
    - could be saved as .csv file, and directly exported as `.docx` file for the manuscript


## GlacierMIP3 Part B -> analyse glacier model differences


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
        
        
####### find . -size +100M | cat >> .gitignore
- note that at the moment, all netcdf files or csv files are not included in the GitHub repository
    - TODO: reduce amount of necessary csv files and data in order that they all have sizes <100 MB and can be uploaded to GitHub
    
    
- todo:
    - move all data csv-files into `data` folder, and adapt all paths accordingly ... 
