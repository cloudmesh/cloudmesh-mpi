# NEW: Installing Slurm on a Raspberry Pi Cluster

## 1. Introduction

Slurm stands for **S**imple **L**inux **U**tility for **R**esource **M**anagement. It is an open-source job scheduler
for a compute cluster to carry out tasks efficiently and in a particular order while using the cluster's resources. Slurm supports batch jobs but also allows the use of resources in interactive mode.
Slurm is a popular batch queueing system used on many advanced supercomputers. However, 
it is possible
to install and use Slurm on a cluster of Raspberry Pis.

This tutorial will use a cluster of four Raspberry Pi 4 Model B computers running Raspbian OS 10 (codename buster). We use 
64 GB SD cards on each of the Pis. In addition, also use a single USB stick connected to the manager Pi, which serves as shared storage
between all of the Pis. This USB stick can be a standard flash drive, a USB SD card adapter with an SD card inside, or it
can even be replaced by a NAS box connected to the network. 
All that matters is that it must be mountable, and it must be greater than 34 MB so we can share the configuration files.  For simplicity, we use a USB card or dongle with 8GB and ensure we do not run out of space.. 
We must also have a power supply to power these Pis, a network switch, and ethernet cables to connect them to the switch, and a host computer used to access the cluster via the network switch. 
Details about how to set up and what hardware you need are documented at <http://piplanet.org> [^www-piplanet]

In this tutorial, the host computer used to connect and issue commands to this cluster is a Windows 10 PC using Git Bash, but other computers 
should be able to follow along because the Git Bash commands and Pi commands will be the same. We will be using cloudmesh burn to set up a preconfigured cluster for you, so you do not have to worry about the details. Other computers as a cluster with cloudmesh and is documented at <http://piplanet.org>.

## 2. Preparation

The first task we conduct is to burn the Pis. Burning them using cloudmesh is much easier than configuring each Pi manually. Our tutorial
for burning the Pis' SD cards using for different operating systems can be found at 

Windows: <https://cloudmesh.github.io/pi/tutorial/raspberry-burn-windows/>
Raspberry Pi OS : <https://cloudmesh.github.io/pi/tutorial/raspberry-burn/> 
Ubuntu <https://cloudmesh.github.io/pi/tutorial/ubuntu-burn/>
MacOs <https://cloudmesh.github.io/pi/tutorial/sdcard-burn-pi-headless/>. 

Please, decide which burn host you like to use and follow the instructions to set up a cluster

This tutorial assumes that your manager node's hostname is `red` and your worker nodes' hostnames are `red01`, `red02`, and `red03`. You may have
additional workers; be sure to alter this tutorial's commands accordingly (e.g. instead of `red,red0[1-3]` perhaps you have `red,red0[1-4]` if
you have five Pis total instead of four). Following this naming schema will make this tutorial run more smoothly.

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

We must install the `ntpdate` package because SLURM and Munge run most efficiently when the cluster is
on the same page when it comes to the time. Software for job scheduling such as SLURM must run on computers
that have the correct time. Let us set up `ntpdate` as follows, which may take around three minutes:

```bash
(ENV3) you@yourhostcomputer $ cms host ssh red,red0[1-3] "'sudo apt-get update'"
(ENV3) you@yourhostcomputer $ cms host ssh red,red0[1-3] "'sudo apt install ntpdate -y'"
```

When the command has finished and the output says `True` under the success column reboot the Pis:

```bash
(ENV3) you@yourhostcomputer $ cms host reboot "red,red0[1-3]"
``` 

### 3.2 Prepare Shared Storage

We will use a USB SD Card adapter with an 8 GB SanDisk Memory Stick Pro Duo card inserted. It really does not matter
what type of storage is used as long as it is sufficiently fast, readable, and mountable. We can use a regular USB drive
or even a NAS device, but this tutorial will follow USB storage.

**TODO: VERIFY:
 We plug in the USB storage in the top most blue USB Port blue of the manager PI called red** 

Ensure that the USB storage is connected to red, the manager Pi. Then, ssh into red: 

```bash
(ENV3) you@yourhostcomputer $ ssh red
```

Then issue command 
```bash
(ENV3) pi@red:~ $ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda           8:0    1  7.5G  0 disk
└─sda1        8:1    1  7.4G  0 part
mmcblk0     179:0    0 59.7G  0 disk
├─mmcblk0p1 179:1    0  256M  0 part /boot
└─mmcblk0p2 179:2    0 59.4G  0 part /
```

The USB partition is listed here and shown to be `/dev/sda1`, but it may differ. Note the name of the USB, which can be identified by the SIZE
column (as long as you remember what the size is of your device is and it is unique). Make sure there is no important information on this drive because
we will now format it and erase everything:

```bash
(ENV3) pi@red:~ $ sudo mkfs.ext4 /dev/sda1
```

Ensure you enter this command precisely because you can accidentally erase your Pi otherwise. You can certainly place the USB storage in another USB port, but  make appropriate changes, 

Create the mount directory by issuing these commands:
```bash
(ENV3) pi@red:~ $ sudo mkdir /nfs
(ENV3) pi@red:~ $ sudo chown nobody.nogroup -R /nfs
(ENV3) pi@red:~ $ sudo chmod guo+rw -R /nfs
(ENV3) pi@red:~ $ blkid
```

Take note of the UUID of your USB device (identifiable by the partition name you have identified such as `/dev/sda1`). We must append a
system file so that the device is automatically mounted on boot for convenience. Change the UUID in this command accordingly and issue it:

```bash
(ENV3) pi@red:/nfs $ echo "UUID=55d94f07-0c1f-445c-860c-87fc9fc348be /nfs ext4 defaults 0 2" | sudo tee /etc/fstab -a
```

**TODO: we can automatize this step in future while probing the UUID automatically and using it in a dynamic script. THis should also fix the issue reported in the next section.**

Then mount the drive by issuing `(ENV3) pi@red:~ sudo mount -a`.

There may be an error upon trying to mount the drive: `mount: /nfs: can't find UUID`. For whatever reason, the UUID
may have spontaneously changed. Simply issue `blkid` command again, take note of the new UUID, and reissue the aforementioned echo command
with the correct UUID. Then try remounting through command `sudo mount -a'.

Issue these commands to change the permissions of the drive and to install the Network File Sharing server:

```bash
(ENV3) pi@red:~ $ sudo chown nobody.nogroup -R /nfs
(ENV3) pi@red:~ $ sudo chmod -R 766 /nfs
(ENV3) pi@red:~ $ sudo apt install nfs-kernel-server -y
```

Let us confirm the private IP address of our manager pi, `red`. Issue command `ifconfig`. Scroll up to find the `eth0` configuration.
We are looking for the `inet` in the following line. The IP address used in this tutorial is `10.1.1.1`, but it may be different.
Note this number and make sure that it is the one belonging to your ethernet connection to the switch box (eth0).

**TODO: Not documented how to do that via commandline**

We must now export the NFS share by first appending `/etc/exports` through command (edit it to change `10.1.1.1` to whatever your
IP address is):

```bash
(ENV3) pi@red:/nfs $ echo "/nfs 10.1.1.1/24(rw,sync,no_root_squash,no_subtree_check)" | sudo tee /etc/exports -a
```

The parameters we set ensure read/write access, immediate updating of the file upon modifying, root access across all Pis of the
cluster, and prevent an error caused by simultaneous editing (these characteristics are respective to each parameter).

Issue commands 

```bash
(ENV3) pi@red:~ $ sudo exportfs -a
(ENV3) pi@red:~ $ exit
```

Now we are back on our host computer.

### 3.3 Mount the USB on Worker Pis

For convenience, we can utilize the cloudmesh `cms host ssh` command to execute the same command in across all of our worker Pis.
To install install the NFS client on all of our workers use:

```bash
(ENV3) you@yourhostcomputer $ cms host ssh red0[1-3] "'sudo apt install nfs-common -y'"
```

The success column should read `True` for all workers.

Now, you must repeat the following process for each worker Pi by ssh into each one and issuing these commands
(make sure that the last command's IP address is edited to be your manager Pi's IP address):

**TODO: in future we will have a single script for this and execute the script on each worker. We will likely use the cms host command to make it simple.**

```bash
pi@red01:~ $ sudo mkdir /nfs
pi@red01:~ $ sudo chown nobody.nogroup /nfs
pi@red01:~ $ sudo chmod -R 777 /nfs
pi@red01:~ $ echo "10.1.1.1:/nfs    /nfs    nfs    defaults   0 0" | sudo tee /etc/fstab -a
```

Once you have repeated this process for every Pi, issue:

```bash
pi@red03:~ $ exit
(ENV3) you@yourhostcomputer $ cms host reboot "red,red0[1-3]"
``` 

and wait for the Pis to come back online. Once fully back online (wait at least two minutes), issue:

```bash
(ENV3) you@yourhostcomputer $ cms host ssh red0[1-3] "'sudo mount -a'"
```

Success column should read True for each worker Pi.

### 3.4 Configure Manager Pi Node

We will be designating `red` as the manager node. Thanks to `cms` burn, we have already automatically edited the hosts file
of every Pi to have the IPs and hostnames of each one. This allows the Pis to ssh into each other.

Issue the commands:

```bash
(ENV3) you@yourhostcomputer $ ssh red
(ENV3) pi@red:~ $ sudo apt install slurm-wlm -y
(ENV3) pi@red:~ $ cd /etc/slurm-llnl/
(ENV3) pi@red:/etc/slurm-llnl $ sudo cp /usr/share/doc/slurm-client/examples/slurm.conf.simple.gz .
(ENV3) pi@red:/etc/slurm-llnl $ sudo gzip -d slurm.conf.simple.gz
(ENV3) pi@red:/etc/slurm-llnl $ sudo mv slurm.conf.simple slurm.conf
```

These commands will set up the default SLURM configuration file for the cluster. We must now edit the file to further
specify parameters such as our manager Pi's hostname and which nodes we will use to delegate jobs. Open nano by issuing:

**TODO: In future we will eplace the editing of the commands with a imple python script conducting the modificatin from the commandline.**

```bash
(ENV3) pi@red:/etc/slurm-llnl $ sudo nano slurm.conf
```

> Convenient tips for using the nano editor include the `Ctrl + Insert` keyboard shortcut to Copy and the `Shift + Insert` shortcut
> to paste. These also work for the Git Bash console. Use the arrow keys for navigating through the file.

SlurmctldHost should be set to red(10.1.1.1) or whatever IP address your manager has, as in:

```
...
SlurmctldHost=red(10.1.1.1)
#SlurmctldHost=
...
```

Next, we must add the nodes at the very bottom of the document and change the partition name. The bottom of the document 
should look as follows, following our particular IP addressing schema (yours may differ, you can confirm by issuing command 
`ifconfig` on each Pi):

```
# COMPUTE NODES
NodeName=red01 NodeAddr=10.1.1.2 CPUs=4 State=UNKNOWN
NodeName=red02 NodeAddr=10.1.1.3 CPUs=4 State=UNKNOWN
NodeName=red03 NodeAddr=10.1.1.4 CPUs=4 State=UNKNOWN
PartitionName=mycluster Nodes=red0[1-3] Default=YES MaxTime=INFINITE State=UP
```

Exit nano via `Ctrl + X` and press `y' and `Enter` to save changes. Then issue command:

```
(ENV3) pi@red:/etc/slurm-llnl $ sudo nano cgroup.conf
```

Paste this into the file cgroup.conf in nano:

```
CgroupMountpoint="/sys/fs/cgroup"
CgroupAutomount=yes
CgroupReleaseAgentDir="/etc/slurm-llnl/cgroup"
AllowedDevicesFile="/etc/slurm-llnl/cgroup_allowed_devices_file.conf"
ConstrainCores=no
TaskAffinity=no
ConstrainRAMSpace=yes
ConstrainSwapSpace=no
ConstrainDevices=no
AllowedRamSpace=100
AllowedSwapSpace=0
MaxRAMPercent=100
MaxSwapPercent=100
MinRAMSpace=30
```

Save and exit nano as per usual and then issue command:

```bash
(ENV3) pi@red:/etc/slurm-llnl $ sudo nano cgroup_allowed_devices_file.conf
```

Paste this inside and then save and exit nano:

```
/dev/null
/dev/urandom
/dev/zero
/dev/sda*
/dev/cpu/*/*
/dev/pts/*
/nfs*
```

Issue this command to copy our configuration files to the shared storage so we can copy them to the worker Pis later:

```bash
(ENV3) pi@red:/etc/slurm-llnl $ sudo cp slurm.conf cgroup.conf cgroup_allowed_devices_file.conf /nfs
(ENV3) pi@red:/etc/slurm-llnl $ sudo cp /etc/munge/munge.key /nfs
```

Now we must start Munge, the authentication service for SLURM, as well as the SLURM controller service slurmctld:

```bash
(ENV3) pi@red:/etc/slurm-llnl $ sudo systemctl enable munge
(ENV3) pi@red:/etc/slurm-llnl $ sudo systemctl start munge
(ENV3) pi@red:/etc/slurm-llnl $ sudo systemctl enable slurmctld
(ENV3) pi@red:/etc/slurm-llnl $ sudo systemctl start slurmctld
(ENV3) pi@red:/etc/slurm-llnl $ exit
(ENV3) you@yourhostcomputer $ ssh red01
```

### 3.5 Configure Worker Pi Nodes

Next, we must repeat the following process for every worker Pi. These commands will install the SLURM client, copy the necessary
configuration files from the shared USB (or your storage of choice), and start Munge. Issue these commands on each worker
(so after performing the following on red01, do the same for red02 and red03 and others if you have more):

```bash
pi@red01:~ $ sudo apt install slurmd slurm-client -y
pi@red01:~ $ sudo cp /nfs/munge.key /etc/munge/munge.key
pi@red01:~ $ sudo cp /nfs/slurm.conf /etc/slurm-llnl/slurm.conf
pi@red01:~ $ sudo cp /nfs/cgroup* /etc/slurm-llnl
```

Issue `exit` command on your current worker until you are back on your host computer and issue these commands:

```bash
(ENV3) you@yourhostcomputer $ cms host ssh red0[1-3] "'sudo systemctl enable munge'"
(ENV3) you@yourhostcomputer $ cms host ssh red0[1-3] "'sudo systemctl start munge'"
(ENV3) you@yourhostcomputer $ cms host reboot "red,red0[1-3]"
```

Wait for the Pis to come back online (around two minutes to be safe).

When they are back online, try to  ssh into each worker and issuing this command to verify that Munge works 
(you may need to type `yes` and `Enter` if prompted to continue connecting):
```bash
pi@red01:~ $ ssh pi@red munge -n | unmunge
STATUS:           Success (0)
ENCODE_HOST:      red01 (127.0.1.1)
ENCODE_TIME:      2021-10-10 22:41:41 -0400 (1633920101)
DECODE_TIME:      2021-10-10 22:41:41 -0400 (1633920101)
TTL:              300
CIPHER:           aes128 (4)
MAC:              sha256 (5)
ZIP:              none (0)
UID:              pi (1000)
GID:              pi (1000)
LENGTH:           0
```

> Note: a different output with errors may be resolved by rebooting the Pis.

Start the SLURM daemon by issuing these commands:

```bash
pi@red03:~ $ exit
(ENV3) you@yourhostcomputer $ cms host ssh red0[1-3] "'sudo systemctl enable slurmd'"
(ENV3) you@yourhostcomputer $ cms host ssh red0[1-3] "'sudo systemctl start slurmd'"
```

### 3.6 Test Slurm

Now we can test SLURM by connecting to red through SSH and issuing commands:

```bash
(ENV3) you@yourhostcomputer $ ssh red
pi@red:~ $ sinfo
pi@red:~ $ srun --nodes=3 hostname
```

You should see an output similar to:

```
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

