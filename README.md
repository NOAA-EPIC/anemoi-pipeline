# anemoi-pipeline

## Quick Start:

__1) Setup conda environment based on the following conda environment YAML file:__

- _/env/anemoi_pipeline.yaml_

<br />
<br />

__2) Clone main branch of this repo to local.__

<br />
<br />

__3) Pull in the latest branch/version of the Anemoi modules of interest & save them under your local _/anemoi_ folder:__

- _anemoi-datasets_ (https://github.com/ecmwf/anemoi-datasets)
     
- _anemoi-graphs_ (https://github.com/ecmwf/anemoi-graphs)
     
- _anemoi-models_ (https://github.com/ecmwf/anemoi-models)
     
- _anemoi-training_ (https://github.com/ecmwf/anemoi-training)
     
- _anemoi-utils_ (https://github.com/ecmwf/anemoi-utils)

_*Note: Versions of the following repos being tested against era5 can be found under [https://github.com/NOAA-EPIC/anemoi-pipeline/tree/era5/ane](https://github.com/NOAA-EPIC/anemoi-pipeline/tree/era5/anemoi):_
- _anemoi-datasets (main)_ - pulled on 10/07/24 1:08pm ET
- _anemoi-utils (develop)_ - pulled on 10/07/24 1:08pm ET
- _anemoi-graphs (develop)_ - pulled on 10/07/24 1:08pm ET
- _anemoi-training (develop)_ - pulled on 10/07/24 1:08pm ET
- _anemoi-models (develop)_ - pulled on 10/07/24 1:08pm ET

<br />
<br />

__4) Generate a subset of ERA5 via:__

- _Generate_ERA5_Data_Subset.ipynb_

_*Note: Generated ERA5 data sample will be saved under './sample_data/gcp_era5_subset.zarr'_

<br />
<br />

__5) Run each individual anemoi module as mentioned under the following demo:__
   
- _Pipeline_Demo.ipynb_
     
     - __Demo I: Dataset Module__
          - To convert multi-dimension dataset (e.g. zarr) saved under _/sample_data/gcp_era5_subset.zarr_ to an Anemoi-Formatted Zarr based on the configuration file set under _/datasets_configs_ (e.g. _/datasets_configs/local-gcp-sample-zarr.yaml_), run first two cells under Demo I.
          - Also, could leverage the Anemoi-Formatted Zarr sample being tested on Perlmutter, which is located under: _/pscratch/sd/s/schin/pipeline/anemoi-pipeline/anemoi-local-gcp-sample-zarr.zarr_
           
     - __Demo II: Graph Module__
          - Generate the neural network graph based on the configuration file residing under _/graphs_configs_ (e.g. _/graphs_configs/local_gcp_encoder_processor_decoder_connect_bw_hiddens_recipe.yaml_)
          - To generate graph, run the first two cells under Demo II.
          - To inspect the generated graph, run the fourth cell under Demo II.
            
     - __Demo III: Training Module__
          - To train GNN model type of interest based on the various configuration files required for training (refer to the listed configuration files in the Demo III), run all cells under Demo III. 

_*Note: If an ECMWF developer modifies a given anemoi module's list of "command" scripts, then new arguments for a given anemoi module may arise & this demo would have to accomodate for the change._
