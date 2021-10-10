# Installing Slurm on a Raspberry Pi Cluster

## Introduction

Slurm stands for **S**imple **L**inux **U**tility for **R**esource **M**anagement. It is an open-source job scheduler
for a group of computers (otherwise referred to as cluster) to carry out tasks efficiently and in a particular order. It is possible
to install Slurm on a cluster of Raspberry Pis which have 32-bit armv7l (also called armhf) processors.

This tutorial will use a cluster of four Raspberry Pi 4 Model B (2018) computers running Raspbian OS 10 (codename buster).
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

## Preparation

The first thing we do is burn the Pis. Burning them using cloudmesh is much easier than configuring each Pi manually. Our tutorial
for burning the Pis' SD cards using a Windows host computer can be found at <https://cloudmesh.github.io/pi/tutorial/raspberry-burn-windows/>
while the tutorial for Raspberry Pi OS can be found at <https://cloudmesh.github.io/pi/tutorial/raspberry-burn/> and the tutorial for
Ubuntu at <https://cloudmesh.github.io/pi/tutorial/ubuntu-burn/>.

This tutorial assumes that your manager node's hostname is red and your worker nodes' hostnames are red01, red02, and red03. You may have
additional workers; be sure to alter this tutorial's commands accordingly (e.g. instead of `red0[1-3]` perhaps you have `red0[1-4]` if
you have five Pis total instead of four). Following this name schema will make following this tutorial run more smoothly.


`$ sudo apt install munge`

```
$ munge -n | unmunge
STATUS:           Success (0)
[...]
```

```
$ sudo apt install mariadb-server
$ sudo mysql -u root
create database slurm_acct_db;
create user 'slurm'@'localhost';
set password for 'slurm'@'localhost' = password('slurmdbpass');
grant usage on *.* to 'slurm'@'localhost';
grant all privileges on slurm_acct_db.* to 'slurm'@'localhost';
flush privileges;
exit
```

`$ sudo apt install slurmd slurm-client slurmctld`

Now we encounter some difficulties.

This configurator <https://slurm.schedmd.com/configurator.html> is meant for latest version of slurm, however we have just installed an earlier
version of slurm. We know that we have installed an earlier version of slurm because `dpkg -l | grep slurm` gives us 18.08.5.2-1+deb10u2

We try to use the configurator meant for latest version of slurm anyways. cluster is set as Cluster Name, red is set as SlurmctldHost, and red is set as NodeName
as per tutorial instructions. Process ID Logging section must be filled out first by issuing command `cat /lib/systemd/system/slurmd.service` to know where PIDFile
is. We find it is in

/run/slurmd.pid

So we enter for SlurmctldPidFile `/run/slurmctld.pid` and for SlurmdPidFile `/run/slurmd.pid`

We hit submit at bottom of form, select all, and then copy. Issue command `sudo nano /etc/slurm-llnl/slurm.conf` and paste the copied text and save file.
REMEMBER if you need to delete everything if something is already within this file, set cursor to beginning of document and set Mark by Command + Shift + 6 
then scroll to bottom and press Ctrl + K (you should now recopy the text that the configurator produced and now shift + insert into nano to paste it.
Then save this file slurm.conf)

Now we issue command `sudo nano /etc/slurm-llnl/cgroup.conf` and ensure the following is pasted in:

```
CgroupAutomount=yes
CgroupReleaseAgentDir="/etc/slurm/cgroup"
ConstrainCores=yes
ConstrainDevices=yes
ConstrainRAMSpace=yes
```

and restart daemons:
```
sudo systemctl restart slurmctld
sudo systemctl restart slurmd
```

Now we find an error:
Job for slurmd.service failed because the control process exited with error code.
See "systemctl status slurmd.service" and "journalctl -xe" for details.

Issuing `systemctl status slurmd.service` gives:
```
Oct 08 09:52:16 red slurmd[1380]: error: Couldn't find the specified plugin name for select/cons_tres looking at all files
Oct 08 09:52:16 red slurmd[1380]: error: cannot find select plugin for select/cons_tres
Oct 08 09:52:16 red slurmd[1380]: fatal: Can't find plugin for select/cons_tres
```

This slurm documentation suggests it is because slurm is outdated <https://lists.schedmd.com/pipermail/slurm-users/2020-April/005206.html>
