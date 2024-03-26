import os
from job import Job
from dotenv import load_dotenv


load_dotenv() 


USER = os.getenv("UM_USERNAME")

import subprocess
def scheduleJob(name,id,task,opt):
    if(type(name) is Job):
        newJob = name
    else:
        newJob = Job(name,id,task,opt)
    newJob.sbatchGen()
    subprocess.run(["sbatch",newJob.getLocation()], capture_output = True, user = USER)

def scheduleJob(job):
    if(type(job) is Job):
        newJob = job
    newJob.sbatchGen()
    subprocess.run(["sbatch",newJob.getLocation()], capture_output = True, user = USER)