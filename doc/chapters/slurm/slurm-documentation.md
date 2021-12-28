# Introduction to Slurm

Slurm is an open-source job scheduler for Linux machines. It stands for **S**imple **L**inux **U**tility for **R**esource **M**anagement.
This scheduler is especially helpful for individuals with many machines available to run tasks such as Python programs. To submit a job for
execution, the user runs the `srun` command. Not only can Slurm handle jobs submitted individually, but it can handle a *batch* of jobs using 
the `sbatch` command for maximum efficiency.

Further Slurm commands include the `scancel` command for cancelling jobs, `squeue` command for showing the current list of jobs to be done, `sinfo`
command to show the status of the machines (also referred to as nodes), `smap` command for showing an overview of the jobs and nodes, and `scontrol`
for modifying jobs and further control of the cluster (which is a term that refers to the machines as a whole). [^www-iastate]

# Creating a Job

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


# References 

[^www-iastate]: Slurm basics, Iowa State University <https://researchit.las.iastate.edu/slurm-basics>

[^www-ceci-hpc]: Slurm Quick Start Tutorial, Consortium des Équipements de Calcul Intensif <https://support.ceci-hpc.be/doc/_contents/QuickStart/SubmittingJobs/SlurmTutorial.html>
