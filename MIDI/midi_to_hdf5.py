import h5py
import numpy as np

file = h5py.File(name="file.hdf5", mode="w")
group = file.create_group(name="")
dset = file.create_dataset(name="dataset", shape=(100,), dtype="i")
dset.attrs
