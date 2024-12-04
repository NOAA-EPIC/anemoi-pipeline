from anemoi.datasets.commands.create import Create as CreateDataset
from anemoi.graphs.commands.create import Create as CreateGraph
from anemoi.graphs.commands.inspect import Inspect
from anemoi.training.commands.config import ConfigGenerator
import os, argparse

from anemoi.training.commands.train import Train

main_ds_config_fldrname = "datasets_configs"
os.environ["HYDRA_FULL_ERROR"] = "1"
main_graphs_config_fldrname = "graphs_configs"


def test_convert_era5_gcp_to_anemoi_zarr():
    # ERA5 zarr sample from GCP on local converted to anemoi-formatted zarr
    ds_config_fn = "local-gcp-sample-zarr.yaml"
    save2fn = "anemoi-local-gcp-sample-zarr.zarr"

    args = argparse.Namespace(
        config=f"./{main_ds_config_fldrname}/{ds_config_fn}",
        path=save2fn,
        overwrite=True,
        test="",
        threads=int(),
        processes=8,
        command="",
    )
    CreateDataset().run(args)


def test_generate_graph_gcp() -> None:
    graphs_config_fn = (
        "local_gcp_encoder_processor_decoder_connect_bw_hiddens_recipe.yaml"
    )
    save2fn = "anemoi-local-gcp-sample-zarr-graph.pt"

    args = argparse.Namespace(
        config=f"{os.getcwd()}/{main_graphs_config_fldrname}/{graphs_config_fn}",
        save_path=save2fn,
        overwrite=False,
        description="",
    )
    CreateGraph().run(args)


def test_inspect_graph_gcp() -> None:
    saved_graph_fn = "anemoi-local-gcp-sample-zarr-graph.pt"

    args = argparse.Namespace(
        path=saved_graph_fn,
        output_path="anemoi-local-gcp-sample-zarr-graph-output-plots",
        description="",
    )
    Inspect().run(args)


def test_generate_training_configuration_files() -> None:
    args = argparse.Namespace(
        subcommand="generate", overwrite=False, output="./training_configs_master"
    )

    ConfigGenerator().run(args)


def test_train_model() -> None:
    args = argparse.Namespace(command="")
    Train().run(args)
