#!/bin/bash
#
# [hellslurm.sbatch]
#
#SBATCH --job-name=hello              # Job name
#SBATCH --output=hello.out            # Output file name 
#SBATCH --export=ALL                  # Export all environment variables
#SBATCH --time=00:01:00               # Set max runtime of job = 1 minute
#SBATCH --mem=4G                      # Request 4 gigabytes of memory
#SBATCH --mail-type=BEGIN,END,FAIL    # Send email notifications
#SBATCH --mail-user=ummarin9@myumanitoba.ca # email TO
#SBATCH --partition=LongQ         # Specify the partition to submit the job to



python main.py                 # Run the script using the loaded Python module
