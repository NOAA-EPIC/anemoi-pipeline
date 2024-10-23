# anemoi-pipeline

## Quick Start:

1) __Pull in the latest branch/version of the Anemoi modules of interest & save under the /anemoi folder on your local:__

- anemoi-datasets (https://github.com/ecmwf/anemoi-datasets)
     
- anemoi-graphs (https://github.com/ecmwf/anemoi-graphs)
     
- anemoi-models (https://github.com/ecmwf/anemoi-models)
     
- anemoi-training (https://github.com/ecmwf/anemoi-training)
     
- anemoi-utils (https://github.com/ecmwf/anemoi-utils)

_*Note: Versions of the following repos being tested against era5 can be found under [https://github.com/NOAA-EPIC/anemoi-pipeline/tree/era5/ane](https://github.com/NOAA-EPIC/anemoi-pipeline/tree/era5/anemoi):_
- anemoi-datasets (main) - pulled on 10/07/24 1:08pm ET
- anemoi-utils (develop) - pulled on 10/07/24 1:08pm ET
- anemoi-graphs (develop) - pulled on 10/07/24 1:08pm ET
- anemoi-models (develop) - pulled on 10/07/24 1:08pm ET
  
2) __Generate a subset of ERA5 via:__

- _Generate_ERA5_Data_Subset.ipynb_

_*Note: Data sample will be saved to './sample_data/gcp_era5_subset.zarr'_
     
3) ___Run each individual anemoi module as mentioned under the following demo:__
   
- _Pipeline_Demo.ipynb_
     
     - __Demo I: Dataset Module__
          - To convert multi-dimension dataset (e.g. zarr) saved under _/sample_data/gcp_era5_subset.zarr_ to an Anemoi-Formatted Zarr based on the configuration file set under _/datasets_configs_ (e.g. _/datasets_configs/local-gcp-sample-zarr.yaml_), run first two cells of Demo I.
          - Also, could leverage the Anemoi-Formatted Zarr sample being tested on Perlmutter, which is located under: _/pscratch/sd/s/schin/pipeline/anemoi-pipeline/anemoi-local-gcp-sample-zarr.zarr_
           
     - __Demo II: Graph Module__
          - Generate the Graph based on the configuration file residing under _/graphs_configs_ (e.g. _/graphs_configs/local_gcp_encoder_processor_decoder_connect_bw_hiddens_recipe.yaml_)
          - To generate graph, run the first two cells of Demo II.
          - To inspect the generated graph, run the fourth cell of Demo II.
            
     - __Demo III: Training Module__
          - Train GNN model type of interest based on the various configuration files required for training (refer to the listed configuration files in the Demo III).
          - Run all cells in Demo III. 

_*Note: If an ECMWF developer makes a modification to a given module's list of "command" scripts, then new arguments for a given anemoi module may arise and demo would have to accomodate for the change._
