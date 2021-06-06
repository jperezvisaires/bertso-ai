import sys

import tensorflow as tf
import numpy as np
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import BinaryCrossentropy

from dataset import get_dataset
from models import get_discriminator, get_generator
from gan import GAN


batch_size = 16
seed = 42
latent_dim = 256
epochs = 50


dataset = get_dataset(batch_size, seed)
discriminator = get_discriminator()
generator = get_generator(latent_dim)
gan = GAN(discriminator=discriminator, generator=generator, latent_dim=latent_dim,)

gan.compile(
    d_optimizer=Adam(learning_rate=2e-4, beta_1=0.5),
    g_optimizer=Adam(learning_rate=2e-4, beta_1=0.5),
    loss_function=BinaryCrossentropy(),
)

gan.fit(dataset, epochs=epochs)

