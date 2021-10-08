# INstall ubuntu on a rasberry PI

## Imager INSALL ON UBUNTU 20.04 SYSTEM

wget https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
sudo apt install ./imager_1.6.2_amd64.deb
rpi-imager

Burn ubuntu 20.04 64 bit server

plug pi into wired network (goal be able to login from your desktop/laptop to the pi)


her example on how to log in

ssh ubuntu@192.168.50.12

change password

# update

sudo apt-get update
sudo apt-get upgrade

# hostname

Change the hostname

``bash
$ hostnamectl set-hostname red
$ sudo reboot
```
# install stuff

sudo apt install -y emacs

# install slurm  

Install the desktop (techniaclly not needed, but the tutoial suggest to create the slurm config file with a browser ....

sudo apt-get install -y ubuntu-desktop

# slurm from

https://gist.github.com/ckandoth/2acef6310041244a690e4c08d2610423

sudo apt install -y slurm-wlm slurm-wlm-doc


browser file:///usr/share/doc/slurm-wlm/html/configurator.html


# PI lscpu

lscpu

```
lscpu
Architecture:                    aarch64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
CPU(s):                          4
On-line CPU(s) list:             0-3
Thread(s) per core:              1
Core(s) per socket:              4
Socket(s):                       1
Vendor ID:                       ARM
Model:                           3
Model name:                      Cortex-A72
Stepping:                        r0p3
CPU max MHz:                     1500.0000
CPU min MHz:                     600.0000
BogoMIPS:                        108.00
```
