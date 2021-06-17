import os

import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import BinaryCrossentropy
import numpy as np
import matplotlib.pyplot as plt

from models import get_discriminator, get_generator
from gan import GAN, GANMonitor


def print_random_samples(num_doinu, latent_dim, generator):
    random_latent_vectors = tf.random.normal(shape=(num_doinu, latent_dim))
    generated_doinuak = generator(random_latent_vectors)
    generated_doinuak.numpy()

    for i in range(num_doinu):
        matrix = np.array(generated_doinuak[i])
        matrix = matrix * 255.0
        # matrix = matrix.astype(np.uint8)
        plt.imshow(np.reshape(matrix, (256, 256)))
        plt.show()


batch_size = 16
seed = 42
latent_dim = 16
epochs = 50

abs_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(abs_path, "IMAGES")

print("Loading dataset...")
dataset = tf.keras.preprocessing.image_dataset_from_directory(
    directory=image_path,
    label_mode=None,
    color_mode="grayscale",
    batch_size=batch_size,
    image_size=(256, 256),
    shuffle=True,
    seed=seed,
)
discriminator = get_discriminator()
generator = get_generator(latent_dim)
discriminator.summary()
generator.summary()
gan = GAN(discriminator=discriminator, generator=generator, latent_dim=latent_dim,)

print_random_samples(1, latent_dim, generator)

gan.compile(
    d_optimizer=Adam(learning_rate=1e-4, beta_1=0.5),
    g_optimizer=Adam(learning_rate=2e-4, beta_1=0.5),
    loss_function=BinaryCrossentropy(),
)

gan.fit(
    dataset, epochs=epochs, callbacks=[GANMonitor(num_doinu=1, latent_dim=latent_dim)]
)
