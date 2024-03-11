import sys
sys.path.insert(0, '../backend')

from job import Job
from jobScheduler import scheduleJob
import os.path

from imageCaptioning import imageCaption

# test = Job("MLslurm",12,"docker run --runtime=nvidia --gpus 1 tensor-image",dict(time="12:0:0",output="ML.json",mailtype="BEGIN,END,FAIL",
# mem="48G",mailuser="ummarin9@myumanitoba.ca",gpus="1",gpumem="46068"))
# print(test.sbatchString())
# scheduleJob(test)

imageCaption('https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg')