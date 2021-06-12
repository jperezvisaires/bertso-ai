import time

import h5py
import numpy as np
import pandas as pd
import requests
import pypianoroll as piano


def url_to_hdf5(counter, url):
    failed_read = False
    failed = False

    response = requests.get(url)

    with open("file.mid", "wb") as saveMidFile:
        saveMidFile.write(response.content)

    try:
        multitrack = piano.read("file.mid")

    except:
        print("ERROR LECTURA")
        failed_read = True

    if not failed_read:

        if (
            (multitrack.tempo is None)
            or (multitrack.downbeat is None)
            or (multitrack.tracks[0].pianoroll is None)
        ):
            failed = True
            print("ERROR COMPOSICION")

        else:
            resolution = multitrack.resolution
            tempo = multitrack.tempo
            downbeat = multitrack.downbeat.astype(int)
            piano_roll = multitrack.tracks[0].pianoroll

        if not failed:

            with h5py.File("doinuak.hdf5", "a") as file:
                group = file.create_group(name=str(counter), track_order=True)
                group.attrs["resolution"] = resolution
                group.create_dataset(name="tempo", data=tempo, compression="lzf")
                group.create_dataset(name="downbeat", data=downbeat, compression="lzf")
                group.create_dataset(
                    name="piano_roll", data=piano_roll, compression="lzf"
                )

            with h5py.File("doinuak.hdf5", "r") as file:
                print(np.array(file[str(counter) + "/tempo"]).shape)


def hdf5_to_midi(counter):

    with h5py.File("doinuak.hdf5", "r") as file:
        tempo = np.array(file[str(counter) + "/tempo"])
        downbeat = np.array(file[str(counter) + "/downbeat"]).astype(bool)
        piano_roll = np.array(file[str(counter) + "/piano_roll"])

    track = piano.StandardTrack(
        name="Grand Piano", program=0, is_drum=False, pianoroll=piano_roll,
    )
    multitrack = piano.Multitrack(
        name=None, resolution=24, tempo=tempo, downbeat=downbeat, tracks=[track],
    )
    piano.write("generated_doinu.mid", multitrack)


def get_hdf5(url_list):

    for counter, url in enumerate(url_list):
        time.sleep(0.5)
        print(counter)
        url_to_hdf5(counter, url)


df = pd.read_csv("zortziko_txiki_4.csv", sep=",")
url_list = list(df["midi_url"])
get_hdf5(url_list)

