import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

from models import get_discriminator, get_generator
from gan import GAN, GANMonitor


batch_size = 64
seed = 42
latent_dim = 128
num_proto = 64
epochs = 50
load_models = True

abs_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(abs_path, "IMAGES")

print("Loading dataset...")
dataset = tf.keras.preprocessing.image_dataset_from_directory(
    directory=image_path,
    label_mode=None,
    color_mode="grayscale",
    batch_size=batch_size,
    image_size=(32, 32),
    shuffle=True,
    seed=seed,
)
discriminator = get_discriminator()
generator = get_generator(latent_dim, num_proto)
gan = GAN(discriminator=discriminator, generator=generator, latent_dim=latent_dim,)

g_optimizer = Adam(learning_rate=2e-4, beta_1=0.5)
d_optimizer = Adam(learning_rate=2e-4, beta_1=0.5)

gan.compile(
    d_optimizer=d_optimizer,
    g_optimizer=g_optimizer,
    loss_function=BinaryCrossentropy(),
)

generator_path = os.path.join("SAVE", "generator")
discriminator_path = os.path.join("SAVE", "discriminator")
generator_model_path = os.path.join(generator_path, "generator.h5")
discriminator_model_path = os.path.join(discriminator_path, "discriminator.h5")

# Check if previous models exist:
if load_model:

    if os.path.isfile(generator_model_path):
        gan.generator = load_model(generator_model_path)
        print("Generator loaded.")

    if os.path.isfile(discriminator_model_path):
        gan.discriminator = load_model(discriminator_model_path)
        print("Discriminator loaded.")


gan.fit(
    dataset, epochs=epochs, callbacks=[GANMonitor(num_doinu=1, latent_dim=latent_dim)]
)

os.makedirs(generator_path, exist_ok=True)
os.makedirs(discriminator_path, exist_ok=True)
gan.generator.save(generator_model_path)
print("Generator saved.")
gan.discriminator.save(discriminator_model_path)
print("Discriminator saved.")

