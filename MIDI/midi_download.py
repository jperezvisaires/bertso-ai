import time
import os
import glob

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

        print(midi_path, "OK")

    except:
        print(midi_path, "ERROR")


def midis_to_images(midi_path, image_path, hdf5_name):

    midi_path = os.path.join("/home/jon/Repos/bertso-ai/MIDI", midi_path)

    for counter, doinu in enumerate(glob.glob(midi_path + "/**/*.mid", recursive=True)):

        try:
            midi_file = os.path.join(midi_path, doinu)
            midi_to_image(midi_file, image_path)
            print(doinu, "OK")

        except Exception as error:
            print(error)
            print(doinu, "ERROR")


def download_midis(url_list):

    for counter, url in enumerate(url_list):
        time.sleep(0.5)

        try:
            urls_to_midis(counter, url)
            print(counter, "OK")

        except:
            print(counter, "NaN")


download = False
create_images = True
create_piano = False

if download:
    df = pd.read_csv("doinu_meta.csv", sep=",")
    url_list = list(df["midi_url"])
    download_midis(url_list)

if create_images:
    midis_to_images("MIDIS", "IMAGES", "doinuak")

if create_piano:
    midis_to_images("MIDIS_PIANO", "IMAGES_PIANO", "piano")
