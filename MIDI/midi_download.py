import time
import os

import numpy as np
import pandas as pd
import requests

from midi2image import midi_to_image


def urls_to_midis(counter, url):
    response = requests.get(url)
    os.makedirs("MIDIS", exist_ok=True)
    os.makedirs("IMAGES", exist_ok=True)
    midi_path = os.path.join("MIDIS", "doinu_{}.mid".format(counter))

    try:

        with open(midi_path, "wb") as file:
            file.write(response.content)

    except:
        print("ERROR")


def midis_to_images(midi_path, image_path, hdf5_name):

    for doinu in os.listdir(midi_path):

        try:
            midi_to_image(os.path.join(midi_path, doinu), image_path, hdf5_name, 1)

        except:
            print("Bad MIDI")


def download_midis(url_list):

    for counter, url in enumerate(url_list):
        time.sleep(0.5)
        print(counter)
        url_to_midi(counter, url)


download = False
create_images = True
create_bach = True

if download:
    df = pd.read_csv("zortziko_txiki_zuzen.csv", sep=",")
    url_list = list(df["midi_url"])
    download_midis(url_list)

if create_images:
    midis_to_images("MIDIS", "IMAGES", "doinuak")

if create_bach:
    midis_to_images("MIDIS_BACH", "IMAGES_BACH", "bach")
