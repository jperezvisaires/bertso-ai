import os

import tensorflow as tf
from tensorflow.keras import Model, metrics, callbacks, utils
import numpy as np
from imageio import imwrite


class GAN(Model):
    def __init__(self, discriminator, generator, latent_dim):
        super(GAN, self).__init__()
        self.discriminator = discriminator
        self.generator = generator
        self.latent_dim = latent_dim

    def compile(self, d_optimizer, g_optimizer, loss_function):
        super(GAN, self).compile()
        self.d_optimizer = d_optimizer
        self.g_optimizer = g_optimizer
        self.loss_function = loss_function
        self.d_metric = metrics.Mean(name="d_loss")
        self.g_metric = metrics.Mean(name="g_loss")

    @property
    def metrics(self):
        return [self.d_metric, self.g_metric]

    def train_step(self, real_doinuak):
        # Sample random points in the latent space.
        batch_size = tf.shape(real_doinuak)[0]
        random_latent_vectors = tf.random.normal(shape=(batch_size, self.latent_dim))

        # Decode to fake doinuak.
        generated_doinuak = self.generator(random_latent_vectors)

        # Combine them with real doinuak.
        combined_doinuak = tf.concat([generated_doinuak, real_doinuak], axis=0)

        # Assamble labels discriminating real from fake doinuak.
        labels = tf.concat(
            [tf.ones((batch_size, 1)), tf.zeros((batch_size, 1))], axis=0
        )

        # Add random noise to the labels - important trick!
        labels += 0.05 * tf.random.uniform(tf.shape(labels))

        # Train the discriminator.
        with tf.GradientTape() as tape:
            predictions = self.discriminator(combined_doinuak)
            d_loss = self.loss_function(labels, predictions)

        grads = tape.gradient(d_loss, self.discriminator.trainable_weights)
        self.d_optimizer.apply_gradients(
            zip(grads, self.discriminator.trainable_weights)
        )

        # Sample random points in the latent space
        random_latent_vectors = tf.random.normal(shape=(batch_size, self.latent_dim))

        # Assamble labels that say "all real doinuak".
        misleading_labels = tf.zeros((batch_size, 1))

        # Train the generator (we DO NOT update the weights of the discriminator)
        with tf.GradientTape() as tape:
            predictions = self.discriminator(self.generator(random_latent_vectors))
            g_loss = self.loss_function(misleading_labels, predictions)

        grads = tape.gradient(g_loss, self.generator.trainable_weights)
        self.g_optimizer.apply_gradients(zip(grads, self.generator.trainable_weights))

        # Update metrics
        self.d_metric.update_state(d_loss)
        self.g_metric.update_state(g_loss)

        return {
            "d_loss": self.d_metric.result(),
            "g_loss": self.g_metric.result(),
        }


class GANMonitor(callbacks.Callback):
    def __init__(self, num_doinu=1, latent_dim=64):
        self.num_doinu = num_doinu
        self.latent_dim = latent_dim

    def on_epoch_end(self, epoch, logs=None):
        random_latent_vectors = tf.random.normal(
            shape=(self.num_doinu, self.latent_dim)
        )
        generated_doinuak = self.model.generator(random_latent_vectors)
        generated_doinuak.numpy()

        for i in range(self.num_doinu):
            matrix = np.array(generated_doinuak[i])
            matrix = matrix.astype(np.uint8) * 255
            image_path = os.path.join("OUTPUT", "doinu_{}.png".format(i))
            imwrite(image_path, matrix)

