# Installing Slurm on a Raspberry Pi Cluster using Python Script

## 1. Introduction

Slurm stands for **S**imple **L**inux **U**tility for **R**esource **M**anagement. It is an open-source job scheduler
for a compute cluster to carry out tasks efficiently and in a particular order while using the cluster's resources. 
Slurm supports batch jobs but also allows the use of resources in interactive mode. Slurm is a popular batch queueing 
system used on many advanced supercomputers. However, it is possible to install and use Slurm on a cluster of 
Raspberry Pis.

This tutorial will use a cluster of four Raspberry Pi 4 Model B computers running Raspbian OS 10 (codename buster). We 
use 64 GB SD cards on each of the Pis. In addition, we also use a single USB stick connected to the manager Pi, which 
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

* Windows: <https://cloudmesh.github.io/pi/tutorial/raspberry-burn-windows/>
* Raspberry Pi OS: <https://cloudmesh.github.io/pi/tutorial/raspberry-burn/>
* Ubuntu: <https://cloudmesh.github.io/pi/tutorial/ubuntu-burn/>
* macOS: <https://cloudmesh.github.io/pi/tutorial/sdcard-burn-pi-headless/>

Please, decide which burn host you like to use and follow the instructions to set up a cluster

This tutorial assumes that your manager node's hostname is `red` and your worker nodes' hostnames are `red01`, `red02`, 
and `red03`. You may have additional workers, which is okay because the script is scalable. All that matters is that
the user must enter the workers naming schema accordingly. For example, someone with four workers (`red01`, `red02`,
`red03`, and `red04`) will enter `red0[1-4]` at the beginning of the script's execution, when prompted.

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

## 4. Using SLURM

### 4.1 Creating a Job

To make a job in Slurm, we must first create the submission script. On the manager pi (red), issue command

```bash
(ENV3) pi@red:~ $ sudo nano submit.sh
```

Then copy and paste the following into nano (use `Shift+Insert` to paste and press `Ctrl+X`, `y`, and `Enter`):
```bash
#!/bin/bash
#
#SBATCH --job-name=test
#SBATCH --output=res.txt
#
#SBATCH --ntasks=1
#SBATCH --time=1:00
#SBATCH --mem-per-cpu=1

srun hostname
srun sleep 10
```

The SBATCH parameters specify varying aspects of the job, including the time reserved for the job on the node as well as the MB of RAM per CPU (in this
case, only 1). [^www-ceci-hpc]

We can start the job by executing command

```bash
(ENV3) pi@red:~ $ sbatch submit.sh
```

### 4.2 Status of queue

TODO: explain how queue start works here.

### 4.3 Killing the job

TODO: explain how to kill job in slurm

## 5.0 SLURM Variables

Some common slurm variables include

| Slurm Environment Variable | Description  |
| --- | --- | 
| SLURM_CLUSTER_NAME        | Name of the cluster on which the job is  executing. |
| SLURM_CPUS_ON_NODE        | Number of CPUs on the allocated node.    |
| SLURM_CPUS_PER_TASK       | Number of CPUs requested per task.       |
| SLURM_GPUS                | Number of GPUs requested.                |
| SLURM_GPUS_PER_NODE       | Requested GPU count per allocated node.  |
| SLURM_GPUS_PER_TASK       | Requested GPU count per allocated task.  |
| SLURM_JOB_ID              | The ID of the job allocation.            |
| SLURM_JOB_CPUS_PER_NODE   | Count of processors available to the job |on this node.                            |
| SLURM_JOB_NAME            | Name of the job.                         |
| SLURM_JOB_NODELIST        | List of nodes allocated to the job.      |
| SLURM_JOB_NUM_NODES       | Total number of nodes in the job's       resource allocation.                     |
| SLURM_JOB_PARTITION       | Name of the partition in which the job   is running.                              |
| SLURM_MEM_PER_CPU         | Minimum memory required per allocated    CPU.                                     |
| SLURM_MEM_PER_GPU         | Requested memory per allocated GPU.      |
| SLURM_MEM_PER_NODE        | Total amount of memory per node that the job needs                              |
| SLURM_NODELIST            | List of nodes allocated to the job.      |
| SLURM_NPROCS              | Total number of CPUs allocated           |
| SLURM_NTASKS              | Maximum number of MPI tasks/processes                              |
| SLURM_NTASKS_PER_CORE     | Number of tasks requested per core.      |
| SLURM_NTASKS_PER_GPU      | Number of tasks requested per GPU.       |
| SLURM_NTASKS_PER_NODE     | Number of tasks requested per node.      |
| SLURM_PRIO_PROCESS        | The scheduling priority (nice value) at  the time of job submission. This value   |is propagated to the spawned processes.  |
| SLURM_PROCID              | The MPI rank (or relative process ID) of the current process.                     |
| SLURM_SUBMIT_DIR          | The directory from which SBATCH was invoked.                                 |
| SLURM_SUBMIT_HOST         | The Hostname of the computer from which SBATCH was invoked.                      |
| SLURM_TASK_PID            | The process ID of the corresponding task.                                    |

# Acknowledgment

This work is based on a tutorial published at [^www-slurm]. However, it is heavily modified to leverage the much more convenient cluster set up of cloudmesh, as well as the much more convenient configuration of Slurm that hides many of the setup complexity.

# References 

[^www-piplanet]: Piplanet <http://piplanet.org>

[^www-slurm]: Running SLURM locally on Ubuntu 18.04, The Weekend Writeup Blog, 
<https://blog.llandsmeer.com/tech/2020/03/02/slurm-single-instance.html>

[^www-iastate]: Slurm basics, Iowa State University <https://researchit.las.iastate.edu/slurm-basics>

[^www-ceci-hpc]: Slurm Quick Start Tutorial, Consortium des ??quipements de Calcul Intensif <https://support.ceci-hpc.be/doc/_contents/QuickStart/SubmittingJobs/SlurmTutorial.html>



