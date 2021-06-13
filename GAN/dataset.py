import h5py
import numpy as np
import tensorflow as tf


def read_hdf5_old(counter):

    with h5py.File("doinuak.hdf5", "r") as file:
        tempo = np.array(file[str(counter) + "/tempo"])
        downbeat = np.array(file[str(counter) + "/downbeat"]).astype(int)
        piano_roll = np.array(file[str(counter) + "/piano_roll"])

    zeros_array = np.zeros(shape=(4096 - piano_roll.shape[0], 1))

    tempo = np.reshape(tempo, (tempo.shape[0], 1)) / 300
    tempo = np.concatenate((tempo, zeros_array))

    downbeat = np.reshape(downbeat, (downbeat.shape[0], 1))
    downbeat = np.concatenate((downbeat, zeros_array))

    piano_roll = np.argmax(piano_roll, axis=1)
    piano_roll = np.reshape(piano_roll, (piano_roll.shape[0], 1)) / 127
    piano_roll = np.concatenate((piano_roll, zeros_array))

    midi = np.concatenate((tempo, downbeat, piano_roll), axis=-1)
    midi = np.reshape(midi, (64, 64, 3))

    return midi


def read_hdf5(counter):

    with h5py.File("doinuak.hdf5", "r") as file:
        matrix = np.array(file[str(counter) + "/matrix"])

    matrix = np.reshape(matrix, (64, 512, 1)) / 255

    return matrix


def get_dataset(batch_size, seed):

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

    dataset = tf.convert_to_tensor(dataset, dtype=tf.float32)
    dataset = tf.data.Dataset.from_tensor_slices(dataset)
    dataset = dataset.shuffle(buffer_size=batch_size * 8, seed=seed)
    dataset = dataset.batch(batch_size)

    return dataset

