# Creates a slurm job to run backend in docker

from read import Read
from htmlparser import HtmlParser
from job import Job
from jobScheduler import scheduleJob
import os.path

test = Job("helloslurm",12,"docker run html-image",dict(time="12:0:0",output="words.json",mailtype="BEGIN,END,FAIL",mem="4G",mailuser="ummarin9@myumanitoba.ca"))
print(test.sbatchString())
print(os.path.isfile("test.txt"))
scheduleJob(test)