.. _quickstart:

Quick Start: Running Anemoi Pipeline
======================================

#. Clone the main branch of this repository:

   .. code-block:: console

      git clone https://github.com/NOAA-EPIC/anemoi-pipeline.git

   .. note::

      The ``era5`` and ``ufs_replay`` branches are tracking the ``main`` branch. 

#. Set up the conda environment using the ``env/anemoi_pipeline.yaml`` conda environment file:

   .. code-block:: console
      
      cd anemoi_pipeline
      git checkout era5
      module load conda
      conda env create --name anemoi_pipeline --file=env/anemoi_pipeline.yaml # this uses pip and takes a few minutes
      conda env list # this shows where the new conda env file lives
      conda activate anemo_pipeline

#. Pull in the latest branch/version of the Anemoi modules of interest & save them under your local ``/anemoi`` folder:

   * `anemoi-datasets <https://github.com/ecmwf/anemoi-datasets>`_
   * `anemoi-graphs <https://github.com/ecmwf/anemoi-graphs>`_
   * `anemoi-models <https://github.com/ecmwf/anemoi-models>`_
   * `anemoi-training <https://github.com/ecmwf/anemoi-training>`_
   * `anemoi-utils <https://github.com/ecmwf/anemoi-utils>`_

   .. note:: Versions of the following repositories being tested against era5 can be found under https://github.com/NOAA-EPIC/anemoi-pipeline/tree/era5/anemoi. 
   
      * *anemoi-datasets (main)* - pulled on 10/07/24 1:08pm ET
      * *anemoi-utils (develop)* - pulled on 10/07/24 1:08pm ET
      * *anemoi-graphs (develop)* - pulled on 10/07/24 1:08pm ET
      * *anemoi-training (develop)* - pulled on 10/07/24 1:08pm ET
      * *anemoi-models (develop)* - pulled on 10/07/24 1:08pm ET


#. Generate a subset of ERA5 via:

   * ``Generate_ERA5_Data_Subset.ipynb``

   .. note:: Generated ERA5 data sample will be saved under ``/sample_data/gcp_era5_subset.zarr``


#. To execute each anemoi module, run each demo mentioned under the following notebook:
   
   * ``Pipeline_Demo.ipynb``
     
      * **Demo I: Dataset Module**
         * To convert multi-dimension dataset (e.g. zarr) saved under ``/sample_data/gcp_era5_subset.zarr`` to an Anemoi-Formatted Zarr based on the configuration file set under ``/datasets_configs`` (e.g., ``/datasets_configs/local-gcp-sample-zarr.yaml``), run first two cells under Demo I.
            
         * Also, could leverage the Anemoi-Formatted Zarr sample being tested on Perlmutter, which is located under: ``/pscratch/sd/s/schin/pipeline/anemoi-pipeline/anemoi-local-gcp-sample-zarr.zarr``
           
      * **Demo II: Graph Module**
         * Generate the neural network graph based on the configuration file residing under ``/graphs_configs`` (e.g., ``/graphs_configs/local_gcp_encoder_processor_decoder_connect_bw_hiddens_recipe.yaml``)
            
         * To generate graph, run the first two cells under Demo II.
            
         * To inspect the generated graph, run the fourth cell under Demo II.
            
      * **Demo III: Training Module**
         * To train GNN model type of interest based on the various configuration files required for training (refer to the listed configuration files in the Demo III), run all cells under Demo III.
      

   .. note:: If an ECMWF developer modifies a given anemoi module's list of "command" scripts, then new arguments for a given anemoi module may arise & this demo would have to accomodate for the change.
