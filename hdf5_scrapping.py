import h5py
import requests
import mido

from MIDI.read_midi import mid2arry


def url_to_hdf5(url, counter):
    response = requests.get(url)

    with open("file.mid", "wb") as saveMidFile:
        saveMidFile.write(response.content)

    midi_file = mido.MidiFile("file.mid", clip=True)
    midi_array = mid2arry(midi_file)
    array_shape = midi_array.shape

    with h5py.File("doinuak.hdf5", "w") as file:
        dset = file.create_dataset(name=str(counter), shape=array_shape, dtype="i")
        print("OK")


url = "https://bdb.bertsozale.eus/common/file/get/24493"

url_to_hdf5(url, 0)

with h5py.File("doinuak.hdf5", "r") as file:
    print(file["0"])

