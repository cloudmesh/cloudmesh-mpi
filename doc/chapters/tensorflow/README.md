# Preparing a Single Raspberry Pi 4 with TensorFlow 2.5.0 on Ubuntu 20.04

Duration: 2 hours 40 minutes

## Introduction
To get TensorFlow 2.5.0 running on a single Raspberry Pi, we will first burn Ubuntu to the Pi's SD card, then run an automated TensorFlow installation process consisting of 2 scripts.

Requirements:
- Raspberry Pi 4
- 64gb SD card
- SD card reader + computer to run Pi Imager application
- access to internet

## Prepare a Pi 4 running Ubuntu 20.04

Duration: 20 minutes

For this we will use the official Raspberry Pi Imager [^ref1].

Simply install the software, use an SD card reader for your device, and burn the following OS to the card from the options in the program:
Ubuntu Server 20.04 LTS (RPi 3/4/400) 64-bit for arm64 architectures

Once completed, insert the SD card into the Pi and turn it on, going through any necessary preliminary setup.

## Installation

Once the Pi with ubuntu 20.04 is up and running and we are prepared in the desired home directory, we can begin installation using our scripts.

Step 1:

Duration: 2 hours

```bash
$ curl -Ls http://cloudmesh.github.io/get/pi/tensorflow/step1 | sh
$ reboot
```

Step 2:

Duration: 20 minutes

```bash
$ curl -Ls http://cloudmesh.github.io/get/pi/tensorflow/step2 | sh
```

## Verify installation
To verify TensorFlow installation, try the following:

```
$ python3 -c "import tensorflow; print(tensorflow.__version__)"
```

it should show version 2.5.0.

## Example

To show TensorFlow 2 in action, we will use a basic example as presented in the official quickstart guide [^ref2] using the mnist dataset. Comments are provided to explain each step.

If you would like to test this on your own, you may save the following into a python script (i.e., example.py) and run it with ```python3 example.py```.

```
import tensorflow as tf

# load the mnist dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# feature scale the data, converting from integers to floating point numbers
x_train, x_test = x_train / 255.0, x_test / 255.0

# build our model with custom layers
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# choose our loss function
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# compile the model with our loss function and a selected optimizer strategy
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])
              
# train the model
model.fit(x_train, y_train, epochs=5)

# evaluate the model
model.evaluate(x_test,  y_test, verbose=2)
```

After 5 epochs of training, my Pi reported a final testing accuracy of 0.9768.

## References
[^ref1]: https://www.raspberrypi.com/software/
[^ref2]: https://www.tensorflow.org/tutorials/quickstart/beginner
