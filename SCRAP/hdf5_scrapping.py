import h5py
import requests




def url_to_hdf5(url, counter):
    response = requests.get(url)
    midi_file = response.content
    

    with h5py.File('doinuak.hdf5', 'w') as file:
        dset = file.create_dataset('')