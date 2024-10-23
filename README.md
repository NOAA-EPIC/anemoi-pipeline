# anemoi-pipeline

Anemoi-Converted dataset on Perlmutter:
- /pscratch/sd/s/schin/pipeline/anemoi-pipeline/anemoi-local-gcp-sample-zarr.zarr
    

1) Pull in the latest branch/version of the Anemoi modules of interest & save under the /anemoi folder on your local:
   - anemoi-datasets (https://github.com/ecmwf/anemoi-datasets)
     
   - anemoi-graphs (https://github.com/ecmwf/anemoi-graphs)
     
   - anemoi-models (https://github.com/ecmwf/anemoi-models)
     
   - anemoi-training (https://github.com/ecmwf/anemoi-training)
     
   - anemoi-utils (https://github.com/ecmwf/anemoi-utils)

*Note: Versions of the following repos being tested against era5 can be found under [https://github.com/NOAA-EPIC/anemoi-pipeline/tree/era5/ane](https://github.com/NOAA-EPIC/anemoi-pipeline/tree/era5/anemoi):
- anemoi-datasets (main) - pulled on 10/07/24 1:08pm ET
- anemoi-utils (develop) - pulled on 10/07/24 1:08pm ET
- anemoi-graphs (develop) - pulled on 10/07/24 1:08pm ET
- anemoi-models (develop) - pulled on 10/07/24 1:08pm ET
  
2) Generate a subset of ERA5 via:
   - Generate_ERA5_Data_Subset.ipynb

*Note: Data will be saved to './sample_data/gcp_era5_subset.zarr'
     
3) Run each individual anemoi module via:
   - Pipeline_Demo.ipynb
  
*Note: If an ECMWF developer makes a modification to a given module's list of "command" scripts, then new arguments for a given anemoi module may arise and demo would have to accomodate for the change.
