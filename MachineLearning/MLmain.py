from job import Job
from jobScheduler import schduleJob
import os.path

test = Job("MLslurm",12,"docker run testor-image",dict(time="12:0:0",output="ML.json",mailtype="BEGIN,END,FAIL",mem="4G",mailuser="noureevr@myumanitoba.ca"))
print(test.sbatchString())
print(os.path.isfile("test.txt"))
schduleJob(test)