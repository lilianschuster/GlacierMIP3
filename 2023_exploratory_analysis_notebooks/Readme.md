# Notebook overview:

# find . -size +100M | cat >> .gitignore

### 0: Preprocessing, create datasets that can be analysed:

- `000_test_for_duplicates_and_other_errors.ipynb`:
    - checks if there are duplicates in the data of the submitted groups (now all duplicates were removed/resubmitted, so the tests are running without errors)
    
- `00_extract_isimip3b_glacier_climate_change.ipynb`: 
    - creates glacier-area global and regional temperature change averages `../data/temp_ch_ipcc_isimip3b_glacier_regionally.csv` and `figures/00_climate/00_temp_change_global_regional_glacier_hist_{scenario}.png`
    - to only get global mean temperature changes for each of the experiments (time periods and scenarios) and GCMs: go to `../isimip3b_postprocessing_analysis/isimip3b_postprocess_to_monthly.ipynb`
    
- `0a_analysis_regional_model_dataset_merging_and_initial_state_comparison.ipynb`
    - merges all regional glacier runs of the different models into one netCDF file 
    - creates: https://cluster.klima.uni-bremen.de/~lschuster/glacierMIP3_analysis/glacierMIP3_apr04_models_all_rgi_regions_sum_scaled.nc
    - (there might be a more recent date available)
    - volume/area scaling applied so that all models start at the same initial state
    
- `0b_create_extended_5000yr_timeseries.ipynb`
    - uses the scaled netCDF file from the previous notebook and creates an extended notebook where all simulations go until simulation year 5000
        - applied option: repeat the values of the last 101 years
    - creates e.g. https://cluster.klima.uni-bremen.de/~lschuster/glacierMIP3_analysis/glacierMIP3_Jan29_2024_models_all_rgi_regions_sum_scaled_extended_repeat_last_101yrs.nc
    
- `0c_correction_regional_volume_change_until_2020.ipynb`-
    - shifts all time series to roughly the 2020 volume 
    - creates some regional timeseries figures that are nice to describe the simulation year approach
    - creates some test figures to show how much  simulation years are shifted and how well the 2020 volume is matched 
    - creates the hugonnet 2021 / Farinotti et al. 2019 summary statistics that also includes the estimated median RGI year and the 2020 regional volume:
        - 'rgi_vs_2020_volume_hugonnet_estimates.csv'
    - creates the `shift....nc` file
        e.g.: https://cluster.klima.uni-bremen.de/~lschuster/glacierMIP3_analysis/all_shifted_glacierMIP3_Jan29_2024_models_all_rgi_regions_sum_scaled_extended_repeat_last_101yrs_via_5yravg.nc



 
### 1: First Analysis without really using temperature data

- `1_overview_timeseries_plots.iypnb`
    - creates simple volume time series plots for every RGI region, and then also for every GCM separately (plots inside of `figures/1_overview_timeseries_plot`)
    - also creates some test figures to analyse whether steady-state is reached
        - however, the issue is that the timing of steady-state depends a lot on the definition
        - will instead use a figure from 3_response_time_analysis_with_2020_shift.ipynb as supplemental figure!!! (then we show already in the same figure also the time to reach 50 or 80% of the total changes

    


### 2: Also include temp. change data
- `lowess_fits/lowess_percentile_interval_fit_per_region_added_uncertainties.py`
    - need to execute the lines of `commandos_slurm.txt`
    - python scripts to create the lowess fits with uncertainties 
    - creates csv files with the lowess best frac fits:
        - e.g.: `lowess_fits/fitted_lowess_best_frac_shift_years_rel_2020_101yr_avg_period_lowess_added_quantiles_added_current12deg_5000_{DATE}.csv`
    - creates csv files with the exponential fit (just for comparison), here the "shifted variant"
        - e.g.: fitted_lowess_best_frac_shift_years_rel_2020_101yr_avg_period_lowess_added_quantiles_added_current12deg_5000_{DATE}.csv
    - creates rather complex figure variants of Fig.2 of the manuscript (figures are in 2a_lowess_fits)
        - those are simplified later in 2_glacier_vs_climate_change_evolution.ipynb


- `per_glacier_lowess_calib/lowess_percentile_interval_fit_per_model_per_region.py`
    - python scripts to create the per-glacier lowess fits 
        - (necessary to assess glacier model uncertainties of the temperature sensitivities)
        - same csv files as in lowess_fits/...
        - figures are in 2a_lowess_fits 


- `2_glacier_vs_climate_change_evolution.ipynb`
    - global plot, and for every RGI region, showing results by always using median (and quantiles) of glacier models 
    - creates figures inside of `2_timeseries_temp_ch_reg_glob` and the Fig. `2_condensed_rgi_region_analysis.png` 
         - manuscript figure 1, 2 (TODO: need to update the figure to show LOWESS fit with uncertainties instead of exp. fit)
         - actually Fig. 1 needs the fits that are shown in 
    - creates figures of global vs regional warming (for supplements)
    - creates supplemental figures with x-axis the RGI regions and as y-axis ... (allow to also show uncertainties): 
        - steady-state statistics with uncertainties (1.2°C ice loss, temp. sensitvities - TODO _> update and add uncertainties)
    
- `2_find_equilibrium_steady_state_yr.ipynb`
    - find steady-state year (potentially interesting for one supplemental figure)


- `2depr_analysis_regional_glacier_vs_climate_change.ipynb` **(at the moment not anymore used for anything in the manuscript)**
    - comparison of glacier changes to global or glacier regional climate changes 
    
### 3: further analysis of steady state and time to reach 50 or 80% of the total changes
- `3a_response_time_analysis_with_2020_shift.ipynb`
        - time to reach 50 or 80% of the total changes (median over all models
            - also done for every glacier model separately (but this uses the "unshifted" data (to check!!!)
        - creates supplemental figures of "Time to reach 50%/80 % of the changes statistics" 
        - `3depr_response_time_analysis.ipynb`:
            - old version without a simulation year shift (maybe nice for GlacierMIP3 Part 2 study)
- `3b_extract_regional_climatic_glacier_median_response_time_characteristics.ipynb`
        - extracts all the regional glacier/climate and response time characteristics and saves them under:
            - creates '3_shift_summary_region_characteristics.csv'
        - `3depr_fitted_glacier_response_clustering_all_exp_OLD.ipynb`:
            - also includes exponential fit clustering
            - deprecated
        - `3depr_fitted_glacier_response_clustering_temp_above_0_8.ipynb`:
            - this is the same (but an older version notebook), thatonly used exponential fits with experiments with data >=0.8°C
            - deprecated 

- `3c_lowess_shifted_fit_region_characteristics_glacier_response.ipynb
        
        
### 4: further aggregated figures such as the world map

- `4_world_map_figure.ipynb`
    - world map plot created 
    - (the subplots that go below the world map are created by 3_lowess_shifted_fit_region_characteristics_glacier_response.ipynb)
    - 

### discussion analysis
- `5x_RGI04_barnes_ice_cap_analysis.ipynb`
- `5_comparison_to_marzeion_et_al_2018.ipynb`



## GlacierMIP3 Part B -> analyse glacier model differences


- `PartB_0x_individual_glacier_check.ipynb` (***only interesting for GlacierMIP3 Part 2***)
    - checks if individual glacier interannual variability coincides between glacier models
    - looks at per-glacier files!!!
    - PyGEM' interannual variability coincides well with the one from OGGM & OGGM-VAS, but GloGEMFlow's interannual variability does not coincide at all with them 
    

- `PartB_1_annual_variability.ipynb` (***only interesting for GlacierMIP3 Part 2***)
    - shows the differences in the interannual regional volume variability between the glacier models (some models, specifically GloGEM-family, do not correlate with the other models)
    
- `PartB_1_glacier_model_differences_first trials.ipynb` (***only interesting for GlacierMIP3 Part 2***)
 
- `PartB_3_glacier_model_differences.ipynb` (***only interesting for GlacierMIP3 Part 2***)
    - plot the difference period - ref_peroid for each glacier model -> filter out downscaling difference 
        - look at differences between time series to reduce the downscaling influence  (as downscaling is different for every glacier model)
        - not sure how to go on with that! 
        
        
        
 ### Plans

- analyse interannual variability -> we can not do that due to some strange things done in some models
