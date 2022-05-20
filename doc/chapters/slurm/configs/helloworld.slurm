#!/bin/bash
#SBATCH --job-name=myjob         # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --time=00:01:00          # total run time limit (HH:MM:SS)
#SBATCH --output=/home/YOUR_USER       # STDOUT

source ~/ENV3/bin/activate
mpiexec python -m mpi4py.bench helloworld
