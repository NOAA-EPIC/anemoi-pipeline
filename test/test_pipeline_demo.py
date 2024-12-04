from anemoi.datasets.commands.create import *
import os, argparse


main_ds_config_fldrname = "datasets_configs"


def test_convert_to_anemoi_zarr():
    # ERA5 zarr sample from GCP on local converted to anemoi-formatted zarr
    ds_config_fn = "local-gcp-sample-zarr.yaml"
    save2fn = "anemoi-local-gcp-sample-zarr.zarr"

    args = argparse.Namespace(
        config=f"../{main_ds_config_fldrname}/{ds_config_fn}",
        path=save2fn,
        overwrite=True,
        test="",
        threads=int(),
        processes=int(),
        command="",
    )
    Create().run(args)
