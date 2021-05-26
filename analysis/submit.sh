#!/bin/bash

#SBATCH --job-name=hothaloacc
#SBATCH --partition=skx-normal
#SBATCH --nodes=1
#SBATCH --ntasks=48
#SBATCH --time=6:00:00
#SBATCH --output=/scratch/03057/zhafen/hot_accretion_data/logs/trove.out
#SBATCH --error=/scratch/03057/zhafen/hot_accretion_data/logs/trove.err
#SBATCH --mail-user=zhafen@u.northwestern.edu
#SBATCH --mail-type=begin
#SBATCH --mail-type=fail
#SBATCH --mail-type=end

# Config path
CONFIG=$1

trove clean $CONFIG
trove evaluate $CONFIG
trove execute $CONFIG
