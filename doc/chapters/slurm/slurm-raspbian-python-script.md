# NEW: Installing Slurm on a Raspberry Pi Cluster using Python Script

## 1. Introduction

Slurm stands for **S**imple **L**inux **U**tility for **R**esource **M**anagement. It is an open-source job scheduler
for a compute cluster to carry out tasks efficiently and in a particular order while using the cluster's resources. 
Slurm supports batch jobs but also allows the use of resources in interactive mode. Slurm is a popular batch queueing 
system used on many advanced supercomputers. However, it is possible to install and use Slurm on a cluster of 
Raspberry Pis.

This tutorial will use a cluster of four Raspberry Pi 4 Model B computers running Raspbian OS 10 (codename buster). We 
use 64 GB SD cards on each of the Pis. In addition, also use a single USB stick connected to the manager Pi, which 
serves as shared storage between all of the Pis. This USB stick can be a standard flash drive, a USB SD card adapter 
with an SD card inside, or it can even be replaced by a NAS box connected to the network. All that matters is that it 
must be mountable, and it must be greater than 34 MB so we can share the configuration files.  For simplicity, we use 
a USB card or dongle with 8GB and ensure we do not run out of space. We must also have a power supply to power these 
Pis, a network switch, and ethernet cables to connect them to the switch, and a host computer used to access the 
cluster via the network switch. Details about how to set up and what hardware you need are documented 
at <http://piplanet.org> [^www-piplanet]

In this tutorial, the host computer used to connect and issue commands to this cluster is a Windows 10 PC using 
Git Bash, but other computers should be able to follow along because the Git Bash commands and Pi commands will 
be the same. We will be using cloudmesh burn to set up a preconfigured cluster for you, so you do not have to 
worry about the details. Other computers as a cluster with cloudmesh and is documented at <http://piplanet.org>.

## 2. Preparation

The first task we conduct is to burn the Pis. Burning them using cloudmesh is much easier than configuring each Pi 
manually. Our tutorial for burning the Pis' SD cards using for different operating systems can be found at 

Windows: <https://cloudmesh.github.io/pi/tutorial/raspberry-burn-windows/>

Raspberry Pi OS: <https://cloudmesh.github.io/pi/tutorial/raspberry-burn/> 

Ubuntu: <https://cloudmesh.github.io/pi/tutorial/ubuntu-burn/>

macOS: <https://cloudmesh.github.io/pi/tutorial/sdcard-burn-pi-headless/>

Please, decide which burn host you like to use and follow the instructions to set up a cluster

This tutorial assumes that your manager node's hostname is `red` and your worker nodes' hostnames are `red01`, `red02`, 
and `red03`. You may have additional workers; be sure to alter the script accordingly (e.g. instead of 
`red,red0[1-3]` perhaps you have `red,red0[1-4]` if you have five Pis total instead of four).

## 2.1 Raspberry Pi OS Compatibility

Note: if you want to burn the 64 bit OS or a Legacy version of Raspberry OS use the following series of commands instead. This creates a default cluster configuration, and then changes the OS tag to latest-lite-64. For the legacy version use the latest-lite-legacy tag or latest-full legacy tag. Currently (12/16/21) the legacy version is based on Debian Buster while the latest version is based on Debian Bullseye. The Raspberry Pi team released the legacy OS to solve compatibility issues that arose during their upgrade to the Bullseye image. You must research to see which OS your application supports.

These commands are meant to be executed on Linux. Equivalent commands for setting the legacy tags for other operating systems are forthcoming.

```bash
cms burn image versions --refresh  
cms inventory add cluster "red,red0[1-4]"
cms inventory set "red,red0[1-4]" tag to latest-lite-64 --inventory="inventory-red.yaml"
cms burn raspberry "red,red0[1-4]" --device=/dev/sdb --inventory="inventory-red.yaml" 
```

Slurm is presently not easily run on Bullseye. It is more compatible with Buster.

## 3. Installation

Next, we will complete the setup, which uses the following steps:
(a) verify the cluster setup
(b) prepare the shared file space and make them accessible to the workers
(c) install and run Slurm.

### 3.1 Verify Proper Cluster Setup

Turn on your Pis and wait for them to boot. To be sure that `cms` is installed properly from the burn tutorial, issue this command in Git
Bash on the host computer:

```bash
(ENV3) you@yourhostcomputer $ eval `ssh-agent`
(ENV3) you@yourhostcomputer $ eval `ssh-add`
```

Enter your ssh password and then issue the command:

```bash
(ENV3) you@yourhostcomputer $ cms pi temp "red,red0[1-3]"
pi temp red,red0[1-3]
+--------+--------+-------+----------------------------+
| host   |    cpu |   gpu | date                       |
|--------+--------+-------+----------------------------|
| red    | 50.147 |  50.6 | 2021-10-10 20:27:49.670815 |
| red01  | 48.686 |  49.1 | 2021-10-10 20:27:48.991141 |
| red02  | 50.147 |  50.6 | 2021-10-10 20:27:49.007155 |
| red03  | 55.017 |  55   | 2021-10-10 20:27:52.193808 |
+--------+--------+-------+----------------------------+
Timer: 5.9208s Load: 0.2612s pi temp red,red0[1-3]
```

If some of the temperatures are 0 (zero), then there is likely an issue with connecting to
one of the Pis; if so, we suggest you reburn using the tutorials in the Preparation section of this tutorial.

### 3.2 Download and Run Scripts

ssh into the manager node (in our case, `red`) via this command:

```bash
(ENV3) you@yourhostcomputer $ ssh red
```

Now download and run the script:

```bash
(ENV3) pi@red:~ $ curl -L https://raw.githubusercontent.com/cloudmesh/get/main/pi/slurm/index.html --output slurm.py
(ENV3) pi@red:~ $ python slurm.py
```

The first step will install needed packages such as ntpdate and will reboot at the end. Once the reboot is executed,
wait two minutes for the cluster to come back online, ssh into manager again, and rerun script:

```bash
(ENV3) you@yourhostcomputer $ ssh red
(ENV3) pi@red:~ $ python slurm.py
```

This will run the second step, which will prompt the user to insert a blank USB in the top, blue USB3.0 port
of the manager Pi. Confirm that sda1 points to the correct device when prompted and the script will format the USB.
The script will create a shared file system with the USB for all of the Pis.

Furthermore, step 2 retrieves the UUID of the USB and edits system config files so it mounts on boot. It also downloads
the packages for nfs server and points the workers to the private IP address of the manager, where the nfs is located.

After reboot completes, ssh into manager again and rerun script:

```bash
(ENV3) you@yourhostcomputer $ ssh red
(ENV3) pi@red:~ $ python slurm.py
```

This will run the third step, which starts the nfs service and uses the nfs to copy Slurm configuration files which
are already set up with the list of workers (red01, red02, red03) and the manager (red). This step also starts
munge (slurm's authentication service) and slurm services.

After reboot completes, ssh into manager again and rerun script for the last step:

```bash
(ENV3) you@yourhostcomputer $ ssh red
(ENV3) pi@red:~ $ python slurm.py
```

Step 4 copies the munge key and attempts to run slurm. If slurm runs successfully, the output should have
the names of the workers, in any order:

```bash
red02
red01
red03
```

# Acknowledgment

This work is based on a tutorial published at [^www-slurm]. However, it is heavily modified to leverage the much more convenient cluster set up of cloudmesh, as well as the much more convenient configuration of Slurm that hides many of the setup complexity.

# References 

[^www-piplanet]: Piplanet <http://piplanet.org>

[^www-slurm]: Running SLURM locally on Ubuntu 18.04, The Weekend Writeup Blog, 
<https://blog.llandsmeer.com/tech/2020/03/02/slurm-single-instance.html>


