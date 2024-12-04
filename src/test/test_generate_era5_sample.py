import sys

import pytest
import xarray as xr
import logging
import sys


@pytest.mark.integration
@pytest.mark.slow
def test() -> None:
    gs_url = "gs://gcp-public-data-arco-era5/ar/1959-2022-1h-360x181_equiangular_with_poles_conservative.zarr"
    chunk_sz = 48
    gcp_ar_era5_subset = xr.open_zarr(
        gs_url, chunks={"time": chunk_sz}, consolidated=True
    )
    start_date = "2020-12-31"
    end_date = "2021-02-01"
    gcp_ar_era5_subset = gcp_ar_era5_subset.sel(time=slice(start_date, end_date))
    gcp_ar_era5_subset.to_zarr("./sample_data/gcp_era5_subset.zarr")
