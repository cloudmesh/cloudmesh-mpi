# Introduction to Slurm

Slurm is an open-source job scheduler for Linux machines. It stands for **S**imple **L**inux **U**tility for **R**esource **M**anagement.
This scheduler is especially helpful for individuals with many machines available to run tasks such as Python programs. To submit a job for
execution, the user runs the `srun` command. Not only can Slurm handle jobs submitted individually, but it can handle a *batch* of jobs using 
the `sbatch` command for maximum efficiency.

Further Slurm commands include the `scancel` command for cancelling jobs, `squeue` command for showing the current list of jobs to be done, `sinfo`
command to show the status of the machines (also referred to as nodes), `smap` command for showing an overview of the jobs and nodes, and `scontrol`
for modifying jobs and further control of the cluster (which is a term that refers to the machines as a whole). [^www-iastate]

