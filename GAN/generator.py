import h5py
from h5py._hl import dataset
import numpy as np
import matplotlib.pyplot as plt


def read_hdf5(counter):

    with h5py.File("doinuak.hdf5", "r") as file:
        tempo = np.array(file[str(counter) + "/tempo"])
        downbeat = np.array(file[str(counter) + "/downbeat"]).astype(int)
        piano_roll = np.array(file[str(counter) + "/piano_roll"])

    minus_array = np.zeros(shape=(3864 - piano_roll.shape[0], 1)) - 1

    tempo = np.reshape(tempo, (tempo.shape[0], 1)) / 300
    tempo = np.concatenate((tempo, minus_array))

    downbeat = np.reshape(downbeat, (downbeat.shape[0], 1))
    downbeat = np.concatenate((downbeat, minus_array))

    piano_roll = np.argmax(piano_roll, axis=1)
    piano_roll = np.reshape(piano_roll, (piano_roll.shape[0], 1)) / 127
    piano_roll = np.concatenate((piano_roll, minus_array))

    midi = np.concatenate((tempo, downbeat, piano_roll), axis=-1)

    return midi


def get_dataset():

    with h5py.File("doinuak.hdf5", "r") as file:
        counters = list(file.keys())

    first = True

    for counter in counters:

        if first:
            midi = read_hdf5(counter)
            dataset = np.reshape(midi, (1, *midi.shape))
            first = False

        else:
            midi = read_hdf5(counter)
            midi = np.reshape(midi, (1, *midi.shape))
            dataset = np.append(dataset, midi, axis=0)

    return dataset


dataset_midi = get_dataset()
print(dataset_midi.shape)

