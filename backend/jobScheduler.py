# Schedules a slurm job using the file created by job.py.
from job import Job
import subprocess
def scheduleJob(name,id,task,opt):
    if(type(name) is Job):
        newJob = name
    else:
        newJob = Job(name,id,task,opt)
    newJob.sbatchGen()
    subprocess.run(["sbatch",newJob.getLocation()],capture_output=True)

def scheduleJob(job):
    if(type(job) is Job):
        newJob = job
    newJob.sbatchGen()
    subprocess.run(["sbatch",newJob.getLocation()],capture_output=True)