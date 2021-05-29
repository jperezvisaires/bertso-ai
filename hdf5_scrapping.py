import h5py
import numpy as np
import requests
import pretty_midi as midi
import pypianoroll as piano
import matplotlib.pyplot as plt


def url_to_hdf5(url, counter):
    response = requests.get(url)

    with open("file.mid", "wb") as saveMidFile:
        saveMidFile.write(response.content)

    # with h5py.File("doinuak.hdf5", "w") as file:
    #     file.create_dataset(name=str(counter), data=piano_roll)
    #     print("OK")


url = "https://bdb.bertsozale.eus/common/file/get/24493"

url_to_hdf5(url, 0)

multitrack = piano.read("file.mid")
resolution = multitrack.resolution
tempo = multitrack.tempo
downbeat = multitrack.downbeat.astype(int)
pianoroll = multitrack.tracks[0].pianoroll


# with h5py.File("doinuak.hdf5", "r") as file:
#     piano_roll = np.array(file["0"])

# print(np.argmax(piano_roll, 0))

# plt.plot(np.argmax(piano_roll, 0))
# plt.show()

