---
date: 2022-02-10
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

This tutorial assumes that the user has access to all nodes (workers)
and that the Raspberry Pi OS is v10 (Buster).


**Learning Objectives**

* Learn how to run a script to install SLURM on a Pi Cluster
* Test SLURM on the cluster after burning

**Topics covered**

{{% table_of_contents %}}

{{% /pageinfo %}}

## 1. Introduction

There exists yet no convenient way to configure a SLURM cluster for
Raspberry Pis without little effort. Our work integrates two efforts
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
have a number appended to the NAME.  For our tutorial we have chosen
the hostname `red` for the manager. Thus, the workers are named by an
incremental naming schema, such as `red01`, `red02`, `red03`, `red04`,
and so on. In case you have hundreds of Pis you can adjust the naming
scheme accordingly with more leading zeros in the number.

Currently, the script only works with Raspberry
Pi OS version `10`, codename Buster.

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

## 2. Pre-requisites

For a list of hardware parts for different Pi cluster configurations, 
please see our links at
[piplanet.org](https://cloudmesh.github.io/pi/docs/hardware/parts/).

You will need the following:

* Computer/Laptop with Windows 10, macOS, or Linux, which we refer to as
the host computer
* Pi you dedicate as a manager, which we will name `red`, and cloudmesh 
  installed (with Python version >= 3.9, and Raspbian OS version v10 (Buster))
* Any number of worker Pis with Raspbian OS version v10 Buster
* The cluster of manager Pi and worker Pi(s) must be preconfigured
  with login access to each node; they must also have Internet access

At present, we require Raspberry Pi OS v10 (Buster) as SLURM is
easiest to install on it.

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

## 3. Installing Cloudmesh on the Manager

To start, we install cloudmesh, which significantly simplifies the 
installation:

If you already have a configured cluster that can log in to each node,
but you do not have cloudmesh installed, simply login to your manager
Pi and issue this command after you SSH into it:

```bash
(ENV3) you@yourhostcomputer $ ssh red
pi@red $ curl -Ls http://cloudmesh.github.io/get/pi | sh -
```

## 4. Installing SLURM

Next, we will install SLURM. First, 
`ssh` into the manager node (in our case, `red`) via this command:

```bash
(ENV3) you@yourhostcomputer $ ssh red
```

Now we must download the script through the cloudmesh repository. We
will run this script several times after necessary reboots of the 
cluster. First, to download and execute the scripts, run these commands:

```bash
(ENV3) pi@red:~ $ curl -L http://cloudmesh.github.io/get/pi/slurm/install --output install_slurm.py
(ENV3) pi@red:~ $ chmod +x install_slurm.py
(ENV3) pi@red:~ $ ./install_slurm.py
```

The first step will prompt the user to input the worker Pis' naming
schema. For example, if the setup has three workers named `red01`,
`red02`, and so on, then the user would input `red0[1-3]`. Then the
script will install needed packages such as ntpdate and reboot at the
end. Once the reboot is executed, wait two minutes for the cluster to
come back online, `ssh` into manager again, and rerun script:

```bash
(ENV3) you@yourhostcomputer $ ssh red
(ENV3) pi@red:~ $ ./install_slurm.py
```

This will run the second step, which will prompt the user to insert a
blank USB in the top, blue USB3.0 port of the manager Pi. The user
must also input the correct path to the USB from the list shown. Then,
the script will format the USB. **Everything on the USB will be
deleted. Make sure there is nothing important on it.** The script will
create a shared file system with the USB for all the Pis.

Furthermore, Step 2 retrieves the UUID of the USB and edits system
config files so it mounts on boot. It also downloads the packages for
nfs server and points the workers to the private IP address of the
manager, where the nfs is located.

After reboot completes, `ssh` into manager again and rerun script:

```bash
(ENV3) you@yourhostcomputer $ ssh red
(ENV3) pi@red:~ $ ./install_slurm.py
```

This will run the third step, which starts the nfs service and uses
the nfs to copy Slurm configuration files which are already set up
with the list of workers (red01, red02, red03) and the manager
(red). This step also starts munge (slurm's authentication service)
and slurm services.

After reboot completes, ssh into manager again and rerun script for
the last step:

```bash
(ENV3) you@yourhostcomputer $ ssh red
(ENV3) pi@red:~ $ ./install_slurm.py
```

Step 4 copies the munge key and reboots the cluster. 

`ssh` back into the manager Pi and try to run slurm by issuing command
`srun --nodes=3 hostname` (or the number for --nodes can be changed
according to the number of workers). If slurm runs successfully, the
output should have the names of the workers, in any order:

```bash
red02
red01
red03
```

If this does not happen, wait a few seconds in case the other nodes
are still booting. Once they become available, SLURM should detect the
newly allocated resources and proceed with printing the
hostnames. This may take a minute.

## 5. Using SLURM

Now we want to demonstrate how to use your new cluster. For this we
introduce you to the commands `srun` and `sbatch`.

### 5.1 Using `srun`

The `srun` command is a SLURM functionality which runs a command on a
certain number of nodes. It has the `--nodes` parameter, which
specifies how many worker nodes to run the command on. As an example,
we can run an `srun` command to get the hostnames of all the worker
nodes:

```bash
(ENV3) pi@red:~ $ srun --nodes=3 hostname | sort
red01
red02
red03
```

### 5.2 Using `sbatch`

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
if you have more than or less than 3 workers. We use the nano editor
as it is available on the Raspberry Pi OS. If you need to edit the nodes
parameter, issue `sudo nano sort.slurm`. The file is as follows:

```bash
#!/bin/sh
#SBATCH -p mycluster
#SBATCH --time=1
#SBATCH --nodes=3

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

### 5.3 Using `sbatch` in a for loop

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

### 5.4 Using `squeue`

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

### 5.5 Using MPI with SLURM

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


## 6. Known Issues

In case you have limited network bandwidth or the code mirrors are
busy, the script may encounter issues downloading packages. However,
if you can repeatedly attempt to run the script, you will eventually
succeed. The script is specifically built to retry until success.

We also know that there could be an issue resulting from our use of
static IP configuration as discussed in this thread:
<https://forums.raspberrypi.com/viewtopic.php?t=123260#p991054>

The script still works despite this issue.

## 7. Timing and Benchmark

The SLURM installation script takes around 28 minutes. The Internet speed was 30 Mbps for
download and 2.5 Mbps for upload.

Most of the time results from the retrying of downloading packages in
the fourth step, as mentioned in the Known Issues section.

TODO: can we not put a loop for the download and have some check that things are downloaded. I do such things for example in other projects.

e.g. implement

while not downloaded
   do the downoad
   if download complete
      downloaded = True

## 8. References 

[^mills]: Building a Raspberry Pi Cluster, 
Garrett Mills <https://glmdev.medium.com/building-a-raspberry-pi-cluster-784f0df9afbd>

[^mpi]: MPI with Python, Gregor von Laszewski, Fidel Leal, and Jacques Fleischer
<https://cloudmesh.github.io/cloudmesh-mpi//report-mpi.pdf>
