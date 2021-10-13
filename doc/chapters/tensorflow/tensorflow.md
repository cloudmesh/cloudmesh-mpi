# Preparing a Raspberry Pi 4 with Tensorflow 2.5.0 on Ubuntu 20.04

## Introduction
To get tensorflow 2.5.0 running on a Raspberry Pi is not quite as easy as using a single pip command - it requires a fair bit of setup to get installed.
This documentation will attempt to simplify the process outlined by authors at qengineering.eu [^ref1] by providing shell scripts to make the process more automatic.
We will be using Ubuntu 20.04 on a Raspberry Pi 4 with 64gb SD card.

## Installation

### Burn Ubuntu 20.04 onto an SD card
For this we will use the official Raspberry Pi Imager [^ref2].

Simply install the software, use an SD card reader for your device, and burn the following OS to the card from the options in the program:
Ubuntu Server 20.04 LTS (RPi 3/4) 64-bit for arm64 architectures

Once completed, insert it into the Pi and turn it on, going through any necessary preliminary setup.

### Download installation scripts
Once the Pi with ubuntu 20.04 is up and running and we are prepared in the home directory, we can collect the bash scripts for installation:
```
$ wget https://github.com/cloudmesh/cloudmesh-mpi/blob/main/doc/chapters/tensorflow/dependencies.html
$ wget https://github.com/cloudmesh/cloudmesh-mpi/blob/main/doc/chapters/tensorflow/cmake.html
$ wget https://github.com/cloudmesh/cloudmesh-mpi/blob/main/doc/chapters/tensorflow/tensorflow.html
```
then rename them with 
```
$ mv dependencies.html dependencies.sh
$ mv cmake.html cmake.sh
$ mv tensorflow.html tensorflow.sh
```

### Use the scripts

The install process is split into 3 bash scripts which we just downloaded.
First, we set up the developer machine and install OpenCV.
```
$ bash dependencies.sh
```

Next, we build cmake.
```
$ bash cmake.sh
```

Finally, we install tensorflow from custom wheels.
```
$ bash tensorflow.sh
```
NOTE: If this script ends with an error 'cant find gdown', then the device probably needs to be restarted. ```sudo reboot``` the pi and then run the following commands:
```
# download the wheel
gdown https://drive.google.com/uc?id=1I1H2xMs4BTm-UQhBPuLgqnLgmE0ATRl5
# install TensorFlow 2.5.0
sudo -H pip3 install tensorflow-2.5.0-cp38-cp38-linux_aarch64.whl
```

### Verify installation
To verify tensorflow installation, try the following:
```
$ python3
>>> import tensorflow as tf
>>> tf.__version__
>>> exit()
```
it should show version 2.5.0.

## References

[^ref1]: https://qengineering.eu/install-ubuntu-20.04-on-raspberry-pi-4.html
[^ref2]: https://www.raspberrypi.com/software/
