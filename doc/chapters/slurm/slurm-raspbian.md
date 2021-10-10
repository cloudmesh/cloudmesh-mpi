# Installing Slurm on a Raspberry Pi Cluster

## 1. Introduction

Slurm stands for **S**imple **L**inux **U**tility for **R**esource **M**anagement. It is an open-source job scheduler
for a group of computers (otherwise referred to as cluster) to carry out tasks efficiently and in a particular order. It is possible
to install Slurm on a cluster of Raspberry Pis.

This tutorial will use a cluster of four Raspberry Pi 4 Model B computers running Raspbian OS 10 (codename buster).
They have 64 GB SD cards; we also use a USB stick that is connected to the manager Pi, which serves as shared storage
between all of the Pis. This USB stick can be a standard flash drive, an USB SD card adapter with an SD card inside, or it
can even be replaced by a NAS box connected to the network. All that matters is that it must be mountable and it must have 
at least 100 MB free (after this tutorial only 34 MB is used in this shared storage, but we should have more space just to be safe).
We must also have a power supply box to turn on these Pis and a network switch box with ethernet cables to connect them (the host
computer which issues commands to these Pis must also be connected to the network switch box).

In this tutorial, the host computer used to connect and issue commands to this cluster is a Windows 10 PC using Git Bash, but other computers 
should be able to follow along because the Git Bash commands and Pi commands will be the same.

We give credit to the original tutorial <https://blog.llandsmeer.com/tech/2020/03/02/slurm-single-instance.html> which we
have heavily edited to use cloudmesh commands and to be more efficient overall.

## 2. Preparation

The first thing we do is burn the Pis. Burning them using cloudmesh is much easier than configuring each Pi manually. Our tutorial
for burning the Pis' SD cards using a Windows host computer can be found at <https://cloudmesh.github.io/pi/tutorial/raspberry-burn-windows/>
while the tutorial for Raspberry Pi OS can be found at <https://cloudmesh.github.io/pi/tutorial/raspberry-burn/> and the tutorial for
Ubuntu at <https://cloudmesh.github.io/pi/tutorial/ubuntu-burn/>. Follow one of these tutorials fully.

This tutorial assumes that your manager node's hostname is red and your worker nodes' hostnames are red01, red02, and red03. You may have
additional workers; be sure to alter this tutorial's commands accordingly (e.g. instead of `red,red0[1-3]` perhaps you have `red,red0[1-4]` if
you have five Pis total instead of four). Following this naming schema will make following this tutorial run more smoothly.

## 3. Installation

### 3.1 Verify Proper Cluster Setup

Turn on your Pis and wait for them to boot. To be sure that `cms` is installed properly from the burn tutorial, issue this command in Git
Bash on the host computer:

```
(ENV3) you@yourhostcomputer $ eval `ssh-agent`
(ENV3) you@yourhostcomputer $ eval `ssh-add`
```

Enter your ssh password and then issue command:

```
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

We must install the ntpdate package because SLURM and Munge run most efficiently when the cluster is
on the same page when it comes to the time. Software for job scheduling such as SLURM must run on computers
that have the correct time, so lets update apt-get and install ntpdate, which may take around three minutes:

```
(ENV3) you@yourhostcomputer $ cms host ssh red,red0[1-3] "'sudo apt-get update'"
(ENV3) you@yourhostcomputer $ cms host ssh red,red0[1-3] "'sudo apt install ntpdate -y'"
```

When the output says True under the success column and it has finished, then reboot the Pis:

```
(ENV3) you@yourhostcomputer $ cms host reboot "red,red0[1-3]"
``` 

### 3.2 Prepare Shared Storage

We will use a USB SD Card adapter with an 8 GB SanDisk Memory Stick Pro Duo card inserted. It really does not matter
what type of storage is used as long as it is sufficiently fast, readable, and mountable. We can use a regular USB drive
or even a NAS device, but this tutorial will follow USB storage.

Ensure that the USB is connected to red, the manager Pi. Then, ssh into red: `(ENV3) you@yourhostcomputer $ ssh red`

Then issue command 
```
(ENV3) pi@red:~ $ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda           8:0    1  7.5G  0 disk
└─sda1        8:1    1  7.4G  0 part
mmcblk0     179:0    0 59.7G  0 disk
├─mmcblk0p1 179:1    0  256M  0 part /boot
└─mmcblk0p2 179:2    0 59.4G  0 part /
```

This USB's partition is shown to be `/dev/sda1` but it may differ. Note the name of the USB, which can be identified by the SIZE
column (as long as you remember what the size is of your device). Make sure there is no important information on this drive because
we will now format it and erase everything:

`(ENV3) pi@red:~ $ sudo mkfs.ext4 /dev/sda1`

Ensure you enter this command perfectly because you can accidentally erase your Pi otherwise.

Create the mount directory by issuing these commands:
```
(ENV3) pi@red:~ $ sudo mkdir /clusterfs
(ENV3) pi@red:~ $ sudo chown nobody.nogroup -R /clusterfs
(ENV3) pi@red:~ $ sudo chmod 777 -R /clusterfs
(ENV3) pi@red:~ $ blkid
```

Take note of the UUID of your USB device (identifiable by the partition name you have identified such as `/dev/sda1`). We must edit a
system file so that the device is automatically mounted on boot for convenience:

```
(ENV3) pi@red:~ $ sudo nano /etc/fstab
```

>Convenient tips for using the nano editor include the `Ctrl + Insert` keyboard shortcut to Copy and the `Shift + Insert` shortcut
>to paste. These also work for the Git Bash console. Use the arrow keys for navigating through the file.

Create a new line underneath the last PARTUUID line by moving your cursor with the arrow keys right before the # line and pressing `Enter`.
Then, type this line: `UUID=65077e7a-4bd6-47ea-8014-01e06655cc31 /clusterfs ext4 defaults 0 2` and edit the UUID to be the one of your USB
device.

The file should look like this when finished:

```
GNU nano 3.2           /etc/exports
  
proc                   /proc           proc    defaults          0       0
PARTUUID=90f4d157-01  /boot           vfat    defaults          0       2
PARTUUID=90f4d157-02  /               ext4    defaults,noatime  0       1
UUID=2d112ab1-8948-4e7b-a690-587f3470d0f2 /clusterfs ext4 defaults 0 2
# a swapfile is not a swap partition, no line here
#   use  dphys-swapfile swap[on|off]  for that
```

Press `Ctrl + X` and then type `y` to confirm that you want to save the modified buffer (you may have to press `Enter` after `y`).

Then mount the drive by issuing `(ENV3) pi@red:~ sudo mount -a`.

> NOTE: There may be an error upon trying to mount the drive: `mount: /clusterfs: can't find UUID`. For whatever reason, the UUID
> may have spontaneously changed. Simply issue `blkid` command again, take note of the new UUID, and re-edit fstab through command
> `sudo nano /etc/fstab`. Then try remounting through command `sudo mount -a`.

Issue these commands to change the permissions of the drive and to install the Network File Sharing server:

```
(ENV3) pi@red:~ $ sudo chown nobody.nogroup -R /clusterfs
(ENV3) pi@red:~ $ sudo chmod -R 766 /clusterfs
(ENV3) pi@red:~ $ sudo apt install nfs-kernel-server -y
```

Lets confirm the private IP address of our manager pi, red. Issue command `ifconfig`. Scroll up to find the `eth0` configuration.
We are looking for the `inet` in the following line. The IP address used in this tutorial is `10.1.1.1`, but it may be different.
Note this number.

We must now export the NFS share by first editing `/etc/exports` through command:

```
(ENV3) pi@red:~ $ sudo nano /etc/exports
```

Add a new line at the bottom depending on the IP address you identified: `/clusterfs 10.1.1.1/24(rw,sync,no_root_squash,no_subtree_check)`
The file should look like:

```
  GNU nano 3.2                      /etc/exports

# /etc/exports: the access control list for filesystems which may be exported
#               to NFS clients.  See exports(5).
#
# Example for NFSv2 and NFSv3:
# /srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_sub$
#
# Example for NFSv4:
# /srv/nfs4        gss/krb5i(rw,sync,fsid=0,crossmnt,no_subtree_check)
# /srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)
#
/clusterfs 10.1.1.1/24(rw,sync,no_root_squash,no_subtree_check)
```

The parameters we set ensure read/write access, immediate updating of the file upon modifying, root access across all Pis of the
cluster, and prevent an error caused by simultaneous editing (these characteristics are respective to each parameter).

Issue commands 

```
(ENV3) pi@red:~ $ sudo exportfs -a
(ENV3) pi@red:~ $ exit
```

Now we are back on our host computer.

### 3.3 Mount the USB on Worker Pis

For convenience, we can utilize the `cms host ssh` command to execute the same command across all of our worker Pis.
We must install the NFS client on our workers:

```
(ENV3) you@yourhostcomputer $ cms host ssh red0[1-3] "'sudo apt install nfs-common -y'"
```

The success column should read True for all workers.

Now, you must repeat the following process for each worker Pi by ssh into each one and issuing these commands:

```
pi@red01:~ $ sudo mkdir /clusterfs
pi@red01:~ $ sudo chown nobody.nogroup /clusterfs
pi@red01:~ $ sudo chmod -R 777 /clusterfs
pi@red01:~ $ sudo nano /etc/fstab
```

In nano, add the line (altered to whatever your actual manager Pi IP address is):

`10.1.1.1:/clusterfs    /clusterfs    nfs    defaults   0 0`

... so the document should look like:

```
  GNU nano 3.2                       /etc/fstab

proc            /proc           proc    defaults          0       0
PARTUUID=47e92ff7-01  /boot           vfat    defaults          0       2
PARTUUID=47e92ff7-02  /               ext4    defaults,noatime  0       1
10.1.1.1:/clusterfs    /clusterfs    nfs    defaults   0 0
# a swapfile is not a swap partition, no line here
#   use  dphys-swapfile swap[on|off]  for that
```

Once you have repeated this process for every Pi, issue:

```
pi@red03:~ $ exit
(ENV3) you@yourhostcomputer $ cms host reboot "red,red0[1-3]"
``` 

and wait for the Pis to come back online. Once back on, issue:

```
(ENV3) you@yourhostcomputer $ cms host ssh red0[1-3] "'sudo mount -a'"
```

### 3.4 Configure Manager Pi Node

We will be designating red as the manager node. Thanks to cms, we have already automatically edited the hosts file
of every Pi to have the IPs and hostnames of each one. This allows the Pis to ssh into each other.

On red, issue commands:

```
(ENV3) pi@red:~ $ sudo apt install slurm-wlm -y
(ENV3) pi@red:~ $ cd /etc/slurm-llnl/
(ENV3) pi@red:/etc/slurm-llnl $ sudo cp /usr/share/doc/slurm-client/examples/slurm.conf.simple.gz .
(ENV3) pi@red:/etc/slurm-llnl $ sudo gzip -d slurm.conf.simple.gz
(ENV3) pi@red:/etc/slurm-llnl $ sudo mv slurm.conf.simple slurm.conf
```

These commands will set up the default SLURM configuration file for the cluster. We must now edit the file to further
specify parameters such as our manager Pi's hostname and which nodes we will use to delegate jobs. Open nano by issuing:

```
(ENV3) pi@red:/etc/slurm-llnl $ sudo nano slurm.conf
```

SlurmctldHost should be set to red(10.1.1.1) or whatever IP address your manager has, as in:

```
...
SlurmctldHost=red(10.1.1.1)
#SlurmctldHost=
...
```

Also, scroll down to the LOGGING AND ACCOUNTING section and change `ClusterName` if desired. We will set it as:

`ClusterName=cluster`

Next, we must add the nodes at the very bottom of the document and change the partition name. The bottom of the document 
should look as follows, following our particular IP addressing schema (yours may differ, you can confirm by issuing command 
`ifconfig` on each Pi):

```
# COMPUTE NODES
NodeName=red01 NodeAddr=10.1.1.2 CPUs=1 State=UNKNOWN
NodeName=red02 NodeAddr=10.1.1.3 CPUs=1 State=UNKNOWN
NodeName=red03 NodeAddr=10.1.1.4 CPUs=1 State=UNKNOWN
PartitionName=mycluster Nodes=red0[1-3] Default=YES MaxTime=INFINITE State=UP
```

Exit nano via `Ctrl + X` and press `y` and `Enter` to save changes. Then issue command:

```
(ENV3) pi@red:/etc/slurm-llnl $ sudo nano /etc/slurm-llnl/cgroup.conf
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

```
(ENV3) pi@red:/etc/slurm-llnl $ sudo nano /etc/slurm-llnl/cgroup_allowed_devices_file.conf
```

Paste this inside and then save and exit nano:

```
/dev/null
/dev/urandom
/dev/zero
/dev/sda*
/dev/cpu/*/*
/dev/pts/*
/clusterfs*
```

Issue this command to copy our configuration files to the shared storage so we can copy them to the worker Pis later:

```
(ENV3) pi@red:/etc/slurm-llnl $ sudo cp slurm.conf cgroup.conf cgroup_allowed_devices_file.conf /clusterfs
(ENV3) pi@red:/etc/slurm-llnl $ sudo cp /etc/munge/munge.key /clusterfs
```

Now we must start Munge, the authentication service for SLURM, as well as the SLURM controller service slurmctld:

```
(ENV3) pi@red:/etc/slurm-llnl $ sudo systemctl enable munge
(ENV3) pi@red:/etc/slurm-llnl $ sudo systemctl start munge
(ENV3) pi@red:/etc/slurm-llnl $ sudo systemctl enable slurmctld
(ENV3) pi@red:/etc/slurm-llnl $ sudo systemctl start slurmctld
```

### 3.5 Configure Worker Pi Nodes

We must repeat the following process for every worker Pi. These commands will start the SLURM client, copy the necessary
configuration files from the shared USB (or your storage of choice), and start Munge. Issue these commands on each worker:

```
pi@red01:~ $ sudo apt install slurmd slurm-client -y
pi@red01:~ $ sudo cp /clusterfs/munge.key /etc/munge/munge.key
pi@red01:~ $ sudo cp /clusterfs/slurm.conf /etc/slurm-llnl/slurm.conf
pi@red01:~ $ sudo cp /clusterfs/cgroup* /etc/slurm-llnl
pi@red01:~ $ sudo systemctl enable munge
pi@red01:~ $ sudo systemctl start munge
pi@red01:~ $ ssh pi@red munge -n | unmunge
```

You may need to type `yes` and `Enter` if prompted to continue connecting.

Start the SLURM daemon by issuing these commands on all workers:

```
sudo systemctl enable slurmd
sudo systemctl start slurmd
```

### 3.6 Test Slurm

Now we can finally test SLURM by connecting to red through SSH and issuing commands:

```
pi@red:~ $ sinfo
pi@red:~ $ srun --nodes=3 hostname
```

You should see an output similar to:

```
red02
red01
red03
```



