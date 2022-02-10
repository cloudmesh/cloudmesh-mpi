---
date: 2022-02-10
title: "DRAFT: Installing SLURM on Pre-configured Pi Cluster"
linkTitle: "DRAFT: SLURM on Pi Cluster"
description: "A comprehensive tutorial to install SLURM on a connected Pi Cluster"
author: Jacques Fleischer [github.com/jpfleischer](https://github.com/jpfleischer), Gregor von Laszewski ([laszewski@gmail.com](mailto:laszewski@gmail.com)) [laszewski.github.io](https://laszewski.github.io)
draft: True
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---

{{< imgproc image Fill "600x300" />}}

{{% pageinfo %}}

In this tutorial, we explain how to run a Python script that automatically installs SLURM on a pre-configured Pi
Cluster. This tutorial assumes that the user has access to all nodes (workers) and that the Pi OS is Buster.

**Learning Objectives**

* Learn how to run a Python script to install SLURM on a Pi Cluster
* Test SLURM on the cluster after burning

**Topics covered**

{{% table_of_contents %}}

{{% /pageinfo %}}

## 1. Introduction

There exists yet no automatic script to install SLURM, an open-source job scheduler and workload manager, on a cluster
of Raspberry Pis. Thus, we have developed a Python script that automatically installs SLURM on any number of worker
nodes.

The script is meant to automate an arduous process of logging in and switching back and forth from manager to worker,
with many commands along the way. The script takes inspiration from preexisting tutorials such as those written by
Garrett Mills. [^mills]

We assume that the user has access and can log in to all nodes; we also assume that manager has the hostname `red`
and that the workers follow an incremental naming schema, such as `red01`, `red02`, `red03`, `red04`, and so on,
with any number of workers possible. Furthermore, due to latest version incompatibility, the script only works with
Raspberry Pi OS version `10`, codename Buster.

We enable automation of using SSH to issue commands to multiple Pis at a time through the cloudmesh libraries. Thus,
cloudmesh must be installed on the manager Pi before proceeding.

This script does the following:

* Updates packages on each Pi,
* Installs ntpdate package for time synchronization,
* Configures shared storage for sharing configuration files across the cluster,
* Installs the SLURM workload manager and daemons,
* Dynamically writes config files based on IP addresses and hostnames of the Pis,
* Installs MUNGE authentication service for security.

After SLURM is successfully installed, it can be used as a sophisticated manager for running intensive computations
through MPI (Message Passing Interface) and for forays into artificial intelligence, for example.

## 2. Pre-requisites

* Computer/Laptop with Windows 10, macOS, or Linux
* A manager Pi with hostname `red` and cloudmesh installed (with Python version >= 3.9, and OS version Buster)
* Any number of worker Pis with OS version Buster
* The cluster of manager Pi and worker Pi(s) must be preconfigured with login access to each node; they must also have Internet access

If you have not yet set up your cluster to communicate with each other and would like an automated process, please see
[cloudmesh.github.io](https://cloudmesh.github.io/pi/tutorial/raspberry-burn-windows/#2-pre-requisites) for automated
burning of SD cards to create a quick configured cluster.

For parts for different Pi cluster configurations, please see our links on [piplanet.org](https://cloudmesh.github.io/pi/docs/hardware/parts/)

If you already have a configured cluster that can log in to each node, but you do not have cloudmesh installed, simply
login to your manager Pi and issue this command after you SSH into it:

```bash
(ENV3) you@yourhostcomputer $ ssh red
pi@red $ curl -Ls https://raw.githubusercontent.com/cloudmesh/get/main/pi/index.html | sh -
```

## 3. Download and Run Scripts

ssh into the manager node (in our case, `red`) via this command:

```bash
(ENV3) you@yourhostcomputer $ ssh red
```

Now download and run the script (make sure that cloudmesh is installed on the Pi, perhaps by following this tutorial: <https://cloudmesh.github.io/pi/tutorial/raspberry-burn-windows/#64-installing-cms-on-a-pi>):

```bash
(ENV3) pi@red:~ $ curl -L https://raw.githubusercontent.com/cloudmesh/get/main/pi/slurm/index.html --output slurm.py
(ENV3) pi@red:~ $ python3 slurm.py
```

The first step will prompt the user to input the worker Pis' naming schema. For example, if the setup has three workers named `red01`, `red02`, and so on, then the user would input `red0[1-3]`. Then the script will install needed packages such as ntpdate and reboot at the end. Once the reboot is executed,
wait two minutes for the cluster to come back online, ssh into manager again, and rerun script:

```bash
(ENV3) you@yourhostcomputer $ ssh red
(ENV3) pi@red:~ $ python3 slurm.py
```

This will run the second step, which will prompt the user to insert a blank USB in the top, blue USB3.0 port
of the manager Pi. The user must also input the correct path to the USB from the list shown. Then, the script will format the USB.
**Everything on the USB will be deleted. Make sure there is nothing important on it.**
The script will create a shared file system with the USB for all of the Pis.

Furthermore, step 2 retrieves the UUID of the USB and edits system config files so it mounts on boot. It also downloads
the packages for nfs server and points the workers to the private IP address of the manager, where the nfs is located.

After reboot completes, ssh into manager again and rerun script:

```bash
(ENV3) you@yourhostcomputer $ ssh red
(ENV3) pi@red:~ $ python3 slurm.py
```

This will run the third step, which starts the nfs service and uses the nfs to copy Slurm configuration files which
are already set up with the list of workers (red01, red02, red03) and the manager (red). This step also starts
munge (slurm's authentication service) and slurm services.

After reboot completes, ssh into manager again and rerun script for the last step:

```bash
(ENV3) you@yourhostcomputer $ ssh red
(ENV3) pi@red:~ $ python3 slurm.py
```

Step 4 copies the munge key and reboots the cluster. 

`ssh` back into the manager Pi and try to run slurm by issuing command `srun --nodes=3 hostname` (or the number for --nodes can be changed according to the number of workers). If slurm runs successfully, the output should have the names of the workers, in any order:

```bash
red02
red01
red03
```

If this does not happen, wait a few seconds in case the other nodes are still booting. Once they become available, SLURM should detect the newly allocated resources and proceed with printing the hostnames. This may take a minute.

## 4. Testing SLURM by Running a Batch Script

Create a new file called `sort.slurm`. Take note that the filename nor the file extension do not really matter. We are simply creating a file with text inside.

```bash
(ENV3) pi@red:~ $ sudo nano sort.slurm
```

Paste the following contents inside the nano interface by copying the following and then by pressing `Shift + Insert` inside the terminal. You can also change the number after `--nodes=` accordingly if you have more than or less than 3 workers.

```
#!/bin/sh
#SBATCH -p mycluster
#SBATCH --time=1
#SBATCH --nodes=3

srun hostname | sort
```

After pasting the contents, exit nano by using `Ctrl + X` and type `y` and press `Enter`.
You can execute the batch script by running the following:

```bash
(ENV3) pi@red:~ $ sbatch sort.slurm
```

Then, ssh into your first worker node (in our case, it is `red01`) and view the contents. The name of the output file will depend on the number of the batch job. Issue `ls` command, as seen in the following code, to see what the file name is.

```bash
(ENV3) pi@red~ $ exit
(ENV3) you@yourhostcomputer~ $ ssh red01
(ENV3) pi@red01~ $ ls
slurm-23.out
(ENV3) pi@red01~ $ cat slurm-23.out
red01
red02
red03
```

More extensive example 

for loop with multiple sbatch jobs

## squeue

list 

## look at mpi program 

run with srun 
run with sbatch

add ref to mpi manual (ours)

* <https://cloudmesh.github.io/cloudmesh-mpi//report-mpi.pdf> 

add link to how we set things up on windows ... (make sure its exactly what you did).


## References 

