from tensorflow import keras
from tensorflow.keras import layers, Model


def get_discriminator():
    inputs = layers.Input(shape=(32, 32, 1))
    x = Conv2D(inputs, filters=128, kernel_size=3, strides=2, dropout=0.25)
    x = Conv2D(x, filters=128, kernel_size=3, strides=2, dropout=0.25)
    x = layers.Flatten()(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dense(1, activation="sigmoid")(x)
    outputs = x

    return Model(inputs=inputs, outputs=outputs, name="discriminator")


def get_generator(latent_dim, num_proto):
    inputs = layers.Input(shape=(latent_dim))
    x = layers.Dense(4 * 4 * num_proto)(inputs)
    x = layers.LeakyReLU(alpha=0.2)(x)
    x = layers.Reshape((4, 4, num_proto))(x)
    x = Conv2DTrans(x, filters=64, kernel_size=2, strides=2, dropout=0.0)
    x = layers.Dense(64)(x)
    x = layers.LeakyReLU(alpha=0.2)(x)
    x = layers.Dense(64)(x)
    x = layers.LeakyReLU(alpha=0.2)(x)
    x = Conv2DTrans(x, filters=128, kernel_size=4, strides=2, dropout=0.0)
    x = layers.Dense(128)(x)
    x = layers.LeakyReLU(alpha=0.2)(x)
    x = layers.Dense(128)(x)
    x = layers.LeakyReLU(alpha=0.2)(x)
    x = Conv2DTrans(x, filters=256, kernel_size=4, strides=2, dropout=0.0)
    x = layers.Dense(256)(x)
    x = layers.LeakyReLU(alpha=0.2)(x)
    x = layers.Dense(256)(x)
    x = layers.LeakyReLU(alpha=0.2)(x)
    x = layers.Conv2D(filters=1, kernel_size=6, padding="same", activation="sigmoid")(x)
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

