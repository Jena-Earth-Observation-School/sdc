import dask
import xarray as xr
from sdc.cluster import start_slurm_cluster

dask.config.set({'array.chunk-size': '256MiB'})
xr.set_options(keep_attrs=True)

dask_client, cluster = start_slurm_cluster()
