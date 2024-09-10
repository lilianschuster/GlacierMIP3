Most recent postprocessing date: `DATE = "Feb12_2024"`


### 0: Preprocessing, create datasets that can be analysed:

- note that `../data/temp_ch_ipcc_ar6_isimip3b.csv` is produced in this noteboook: ../isimip3b_postprocessing_analysis/isimip3b_postprocess_to_monthly.ipynb --> TODO: eventually move to here ... 
- `00a_gmt_climate_scenarios_figure.ipynb`
    - creates the extended data figure that shows the climate timeseries

- `00b_extract_isimip3a_gswp3-w5e5_glacier_climate_change.ipynb`:
    - get past and current climate from ISIMIP3a GSWP3-W5E5 for the different glacier regions
- `00c_extract_isimip3b_glacier_climate_change.ipynb`: 
    - creates glacier-area global and regional temperature change averages `../data/temp_ch_ipcc_ar6_isimip3b_glacier_regionally.csv` and `figures/00_climate/00_temp_change_global_regional_glacier_hist_{scenario}.png`
    - to only get global mean temperature changes for each of the experiments (time periods and scenarios) and GCMs: go to `../isimip3b_postprocessing_analysis/isimip3b_postprocess_to_monthly.ipynb`
        --> this creates `../data/temp_ch_ipcc_ar6_isimip3b.csv`

- `0a_analysis_regional_model_dataset_merging_and_initial_state_comparison.ipynb`
    - merges all regional glacier runs of the different models into one netCDF file 
    - creates: https://cluster.klima.uni-bremen.de/~lschuster/glacierMIP3_analysis/glacierMIP3_apr04_models_all_rgi_regions_sum_scaled.nc
    - (there might be a more recent date available)
    - volume/area scaling applied so that all models start at the same initial state
- `0a1_test_for_duplicates_and_other_errors.ipynb`
    - checks if there are duplicates in the data of the submitted groups (now all duplicates were removed/resubmitted, so the tests are running without errors)
    
- `0b_create_extended_5000yr_timeseries.ipynb`
    - uses the scaled netCDF file from the previous notebook and creates an extended notebook where all simulations go until simulation year 5000
        - applied option: repeat the values of the last 101 years
    - creates e.g. https://cluster.klima.uni-bremen.de/~lschuster/glacierMIP3_analysis/glacierMIP3_Feb12_2024_models_all_rgi_regions_sum_scaled_extended_repeat_last_101yrs.nc
    
- `0c_correction_regional_volume_change_until_2020.ipynb`
    - shifts all time series to roughly the 2020 volume 
    - creates some regional timeseries figures that are nice to describe the simulation year approach
    - creates some test figures to show how much  simulation years are shifted and how well the 2020 volume is matched 
    - creates the hugonnet 2021 / Farinotti et al. 2019 summary statistics that also includes the estimated median RGI year and the 2020 regional volume:
        - 'rgi_vs_2020_volume_hugonnet_estimates.csv'
    - creates the `shift....nc` file
        e.g.: https://cluster.klima.uni-bremen.de/~lschuster/glacierMIP3_analysis/all_shifted_glacierMIP3_Jan29_2024_models_all_rgi_regions_sum_scaled_extended_repeat_last_101yrs_via_5yravg.nc
