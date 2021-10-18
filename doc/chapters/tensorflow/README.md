# Preparing a Single Raspberry Pi 4 with Tensorflow 2.5.0 on Ubuntu 20.04

Duration: 2 hours 40 minutes

## Introduction
To get tensorflow 2.5.0 running on a single Raspberry Pi, we have created an automated installation process consisting of 2 scripts.
Requirements:
- Raspberry Pi 4
- 64gb SD card
- SD card reader + computer to run Pi Imager application
- access to internet

## Prepare Ubuntu on the Pi

Duration: 20 minutes

For this we will use the official Raspberry Pi Imager [^ref1].

Simply install the software, use an SD card reader for your device, and burn the following OS to the card from the options in the program:
Ubuntu Server 20.04 LTS (RPi 3/4/400) 64-bit for arm64 architectures

Once completed, insert it into the Pi and turn it on, going through any necessary preliminary setup.

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

### Verify installation
To verify tensorflow installation, try the following:

```
$ python3 -c "import tensorflow; print(tensorflow.__version__)"
```
it should show version 2.5.0.

## References
[^ref1]: https://www.raspberrypi.com/software/
