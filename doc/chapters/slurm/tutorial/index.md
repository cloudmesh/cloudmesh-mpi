---
date: 2022-06-21
title: "Installing SLURM on Pre-configured Pi Cluster"
linkTitle: "SLURM on Pi Cluster"
description: "A comprehensive tutorial to install SLURM on a connected Pi Cluster"
author: Jacques Fleischer [github.com/jpfleischer](https://github.com/jpfleischer), Gregor von Laszewski ([laszewski@gmail.com](mailto:laszewski@gmail.com)) [laszewski.github.io](https://laszewski.github.io)
draft: True
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
---

{{< imgproc image Fill "600x300" />}}

{{% pageinfo %}}

In this tutorial, we explain how to automatically install SLURM with a
script on a pre-configured Pi Cluster.

The cluster is preconfigured with our convenient burn tool that
sets up the cluster by first writing to the SD cards of the Pis.

This tutorial assumes that the user has access to all nodes (workers).


**Learning Objectives**

* Learn how to run a script to install SLURM on a Pi Cluster
* Test SLURM on the cluster after burning

**Topics covered**

{{% table_of_contents %}}

{{% /pageinfo %}}

## 1.0 Introduction

There exists yet no convenient way to configure a SLURM cluster for
Raspberry Pis with little effort. Our work integrates two efforts
that will, in combination, make the installation of a SLURM cluster on
Raspberry Pis easy.

The first effort is the creation of a cluster of Pi nodes that are
integrated in a network and in which each node can communicate with
each other.

The second effort is to use our newly developed script to deploy a
SLURM cluster in the nodes with little effort. We have chosen SLURM as
it is a popular, open-source job scheduler and workload
manager. It is common on many academic supercomputers. Hence, our Pi
cluster can also be used as an on-ramp to more complex hardware.

The script is meant to automate an arduous process of logging in and
switching back and forth from manager to worker, with many commands
along the way and benefits from inspiration we took from work
conducted by others.[^mills]

As we use our Raspberry Pi cluster burning tool, we can assume that
the user has access and can log in to all nodes. We also assume that
we have one Pi that is the manager. To replicate a common naming
scheme we will have the manager node have a NAME, while all workers
have a number appended to the NAME. For our tutorial we have chosen
the hostname `red` for the manager. Thus, the workers are named by an
incremental naming schema, such as `red01`, `red02`, `red03`, `red04`,
and so on. In case you have hundreds of Pis you can adjust the naming
scheme accordingly with more leading zeros in the number.

We utilize SSH to issue commands to the Pi workers and leverage libraries
that are developed as part of cloudmesh to issue them on multiple Pis.

In particular, the script does the following:

* Updates needed packages on each Pi,
* Installs ntpdate package for time synchronization,
* Configures shared storage for sharing configuration files across the
  cluster,
* Installs the SLURM workload manager and daemons,
* Dynamically writes configuration files based on IP addresses and
  hostnames of the Pis, and
* Installs MUNGE authentication service for security.

After SLURM is successfully installed, it can be used as a job manager
for running intensive computations through MPI (Message Passing
Interface) and for forays into artificial intelligence. 
To find out more about MPI we have written a separate
tutorial.[^mpi]

## 2.0 Pre-requisites

For a list of hardware parts for different Pi cluster configurations, 
please see our links at
[piplanet.org](https://cloudmesh.github.io/pi/docs/hardware/parts/).

You will need the following:

* Computer/Laptop with Windows 10, macOS, or Linux, which we refer to as
the host computer
* Pi you dedicate as a manager, which we will name `red`
* Any number of worker Pis with Raspbian OS
* The cluster of manager Pi and worker Pi(s) must be preconfigured
  with login access to each node; they must also have Internet access

If you have not yet set up your cluster to communicate with each other
and would like an automated process, please see the following Windows tutorial
at <https://cloudmesh.github.io/pi/tutorial/raspberry-burn-windows/> for
automated burning of SD cards to create a quick configured cluster.
Burning such a cluster can also be done from Linux and macOS at the
following link: <https://cloudmesh.github.io/pi/tutorial/raspberry-burn/>

We strongly recommend using the burn program to configure the cluster
because it will automate the process and enable the SLURM script to
work without having to input SSH passwords for each node at every
step.

## 3.0 Installation

The installation takes around an hour on a cluster of four Raspberry
Pi 4 Model B computers.

To use the cloudmesh SLURM command, one must have cloudmesh installed
by using the following commands.

We assume you are in a venv Python environment. Ours is called (ENV3)

```bash
(ENV3) you@yourlaptop $ mkdir ~/cm
(ENV3) you@yourlaptop $ cd ~/cm
(ENV3) you@yourlaptop $ pip install cloudmesh-installer
(ENV3) you@yourlaptop $ cloudmesh-installer get pi
```

Initialize the cms command:

```bash
(ENV3) you@yourlaptop $ cms help
```

Then clone the cloudmesh-slurm repository:

```bash
(ENV3) you@yourlaptop $ cd ~/cm
(ENV3) you@yourlaptop $ cloudmesh-installer get cmd5
(ENV3) you@yourlaptop $ git clone https://github.com/cloudmesh/cloudmesh-slurm.git
(ENV3) you@yourlaptop $ cd cloudmesh-slurm
(ENV3) you@yourlaptop $ pip install -e .
(ENV3) you@yourlaptop $ cms help
```

You may proceed if `slurm` shows in the documented commands.

After following [the burn
tutorial](https://cloudmesh.github.io/pi/tutorial/raspberry-burn-windows/)
and ensuring that the cluster is online, you have two methods of
installing SLURM.

## 4.0 Method 1 - Install from Host

You can install SLURM on a cluster by executing commands from the host
computer. The host computer is the same computer that is previously
burned your SD Cards and is referred to as `you@yourlaptop`. This
machine can be used to `ssh` into each of the Pis.


To install it, use the command:

```bash
(ENV3) you@yourlaptop $ cms slurm pi install as host --hosts=red,red0[1-4]
```

The `--hosts` parameter needs to include the hostnames of your
cluster, including manager and workers, separated by comma using a
parameterized naming scheme.

The user can also specify a `--partition` parameter, as in
`--partition=mycluster`, to personalize the name of the partition.

The command will take a long time to finish. It may appear to not
progress at certain points, but please be patient. However they will
last hopefully not longer than 45 minutes. The reason this takes such
a long time is that at time of writing of this tutorial, the prebuilt
SLURM packages did not work, so we compile it from source.

Once the script completes, you can check if SLURM is installed by
issuing on the manager:

`(ENV3) pi@red:~ $ srun --nodes=4 hostname`

and replacing the `--nodes` parameter with the number of workers.

You will see an output similar to

```bash
(ENV3) you@yourlaptop $ ssh red
(ENV3) pi@red:~ $ srun --nodes=4 hostname
red01
red02
red03
red04
```

The nodes may be out of order. That is okay and normal.

## 5.0 Method 2 - Install on Manager

### 5.1 Install cloudmesh

This method involves the user logging into the manager via `ssh` and 
first installing cloudmesh in the manager with:

```bash
(ENV3) you@yourhostcomputer $ ssh red
pi@red $ curl -Ls http://cloudmesh.github.io/get/pi | sh -
```

This output is printed upon successful installation.

```bash
Please activate with

    source ~/ENV3/bin/activate

Followed by a reboot
```

After activating venv with the source command and rebooting 
via `sudo reboot`, issue the commands:

```bash
(ENV3) you@yourhostcomputer $ ssh red
pi@red:~ $ cd ~/cm
pi@red:~/cm $ git clone https://github.com/cloudmesh/cloudmesh-slurm.git
pi@red:~/cm $ cd cloudmesh-slurm
pi@red:~/cm/cloudmesh-slurm $ pip install -e .
pi@red:~/cm/cloudmesh-slurm $ cms help
```

The slurm command should appear in the list.

### 5.2 Install SLURM Directly on Pi

Run this command to begin SLURM installation:

```bash
pi@red:~/cm/cloudmesh-slurm $ cms slurm pi install --workers=red0[1-4]
```

The user can also specify a `--partition` parameter, as in
`--partition=mycluster`, to personalize the name of the partition.

The user must `ssh` back into the manager after the cluster reboots
and perform the last command (cms slurm pi install...) 3 more
times. The script will inform the user when this is no longer
necessary and SLURM is fully installed.

You can check if SLURM is installed by issuing on the manager:

`srun --nodes=4 hostname`

and replacing the `--nodes` parameter with the number of workers.

You will see an output similar to

```bash
(ENV3) pi@red:~ $ srun --nodes=4 hostname
red01
red02
red03
red04
```

The nodes may be out of order. That is okay and normal.

## 6.0 Install Single-Node

To make job management simple, we can install SLURM on one computer.
This one computer has no workers and is a manager to its own self.
The user can make and automate jobs for simplicity's sake, and the
same computer will carry out those jobs.

Single-node installation, which is a SLURM cluster with only one node,
can be easily configured by using the host command with the manager
and workers listed as the same hostname. In the following example,
`red` is the single-node.

```bash
cms slurm pi install as host --hosts=red,red
```

## 7. Using SLURM

Now we want to demonstrate how to use your new cluster. For this we
introduce you to the commands `srun` and `sbatch`.

### 7.1 Using `srun`

The `srun` command is a SLURM functionality which runs a command on a
certain number of nodes. It has the `--nodes` parameter, which
specifies how many worker nodes to run the command on. As an example,
we can run an `srun` command to get the hostnames of all the worker
nodes:

```bash
(ENV3) pi@red:~ $ srun --nodes=4 hostname | sort
red01
red02
red03
red04
```

### 7.2 Using `sbatch`

`sbatch` is for predefined tasks to be run in "batches". This way, the
user does not have to run numerous `srun` commands and can simply use
a text file to run jobs.

To test `sbatch`, download our batch file named `sort.slurm`. Take note
that the filename nor the file extension do not really matter. We are
simply retrieving a file with text inside. 

```bash
(ENV3) pi@red:~ $ curl -L http://cloudmesh.github.io/get/pi/slurm/example/sort.slurm --output sort.slurm
```

You can also change the number after `--nodes=` accordingly
if you have more than or less than 4 workers. We use the nano editor
as it is available on the Raspberry Pi OS. If you need to edit the nodes
parameter, issue `sudo nano sort.slurm`. The file is as follows:

```bash
#!/bin/sh
#SBATCH -p mycluster
#SBATCH --time=1
#SBATCH --nodes=4

srun hostname | sort
```

You can execute the batch script by running the
following:

```bash
(ENV3) pi@red:~ $ sbatch sort.slurm
```

Then, ssh into your first worker node (in our case, it is `red01`) and
view the contents. The name of the output file will depend on the
number of the batch job. Issue `ls` command, as seen in the following
code, to see what the file name is.

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

### 7.3 Using `sbatch` in a for loop

For a more extensive script with a for loop, which will execute
numerous `srun` commands, download our Python script `forloop.py` by
issuing the following:

```bash
(ENV3) pi@red:~ $ curl -L http://cloudmesh.github.io/get/pi/slurm/example/forloop.py --output forloop.py
```

`forloop.py` has the following contents, which run numerous `sbatch` commands
that, in and of themselves, run `sort.slurm`:

```python
import os
count = 5
scriptname = "sort.slurm"
for i in range(count):
    os.system(f"sbatch {scriptname}")
```

Issue `python3 forloop.py` and the outputs will be available on
the first worker node.

### 7.4 Using `squeue`

The user can identify jobs in progress or that have yet to run by
issuing the `squeue` command:

```bash
pi@red01:~ $ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
                20 mycluster sort.slu       pi PD       0:00      4 (PartitionNodeLimit)
                21 mycluster sort.slu       pi PD       0:00      4 (PartitionNodeLimit)
```

As seen in the previous output, jobs 20 and 21 have failed to run
because they do not have enough workers to perform the job (in this
configuration, there were only 3 workers when the job needs 4).

### 7.5 Using MPI with SLURM

MPI, which stands for Message Passing Interface, takes advantage of the
cores of the computer to run parallel computing. We can extend this
functionality further by using MPI in conjunction with SLURM, which
leads to efficient, faster workloads.

TODO: explanation missing

* run with srun 
* run with sbatch

To test MPI with SLURM, run the following command:

```bash
# Allocate a Slurm job with 4 nodes and run your MPI application in it
(ENV3) pi@red:~ $ salloc -N 4 mpiexec python -m mpi4py.bench helloworld
salloc: Granted job allocation 26
Hello, World! I am process 0 of 4 on red01.
Hello, World! I am process 1 of 4 on red02.
Hello, World! I am process 2 of 4 on red03.
Hello, World! I am process 3 of 4 on red04.
salloc: Relinquishing job allocation 26
```

To make use of our many MPI examples, download our cloudmesh-mpi repository
by executing the following commands:

```bash
# if you do not already have a cm folder, you can make one by issuing $ sudo mkdir cm
(ENV3) pi@red:~ $ cd cm
(ENV3) pi@red:~/cm $ git clone https://github.com/cloudmesh/cloudmesh-mpi.git
# once it is done, cd to folder
(ENV3) pi@red:~/cm $ cd cloudmesh-mpi/
(ENV3) pi@red:~/cm/cloudmesh-mpi $ cd examples
```

## 8.0 Timing and Benchmark

The SLURM installation script takes around an hour on a cluster of four Pis.
The Internet speed was 30 Mbps for download and 2.5 Mbps for upload.

## 9.0 References 

[^mills]: Building a Raspberry Pi Cluster, 
Garrett Mills <https://glmdev.medium.com/building-a-raspberry-pi-cluster-784f0df9afbd>

[^mpi]: MPI with Python, Gregor von Laszewski, Fidel Leal, and Jacques Fleischer
<https://cloudmesh.github.io/cloudmesh-mpi//report-mpi.pdf>
