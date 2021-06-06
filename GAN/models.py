from tensorflow import keras
from tensorflow.keras import layers, Model


def get_discriminator():
    inputs = layers.Input(shape=(64, 64, 3))
    x = Conv2D(inputs, filters=64, kernel_size=4, strides=2, dropout=0.0)
    x = Conv2D(x, filters=128, kernel_size=4, strides=2, dropout=0.0)
    x = Conv2D(x, filters=128, kernel_size=4, strides=2, dropout=0.0)
    x = layers.Flatten()(x)
    x = layers.Dropout(0.2)(x)
    x = layers.Dense(1, activation="sigmoid")(x)
    outputs = x

    return Model(inputs=inputs, outputs=outputs, name="discriminator")


def get_generator(latent_dim):
    inputs = layers.Input(shape=(latent_dim))
    x = layers.Dense(8 * 8 * latent_dim)(inputs)
    x = layers.Reshape((8, 8, latent_dim))(x)
    x = Conv2DTrans(x, filters=128, kernel_size=4, strides=2, dropout=0.0)
    x = Conv2DTrans(x, filters=256, kernel_size=4, strides=2, dropout=0.0)
    x = Conv2DTrans(x, filters=512, kernel_size=4, strides=2, dropout=0.0)
    x = layers.Conv2D(filters=3, kernel_size=5, padding="same", activation="sigmoid")(x)
    outputs = x

    return Model(inputs=inputs, outputs=outputs, name="generator")


def Conv2D(x, filters, kernel_size, strides, dropout):
    x = layers.Conv2D(filters, kernel_size, strides, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.LeakyReLU(alpha=0.2)(x)
    x = layers.Dropout(dropout)(x)

    return x


def Conv2DTrans(x, filters, kernel_size, strides, dropout):
    x = layers.Conv2DTranspose(filters, kernel_size, strides, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.LeakyReLU(alpha=0.2)(x)
    x = layers.Dropout(dropout)(x)

    return x

