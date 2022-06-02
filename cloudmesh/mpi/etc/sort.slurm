#!/bin/sh
#SBATCH -p mycluster
#SBATCH --time=1
#SBATCH --nodes=3

srun hostname | sort