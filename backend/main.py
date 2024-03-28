# Creates a slurm job to run backend in docker

from read import Read
from htmlparser import HtmlParser
from job import Job
from jobScheduler import schduleJob
import os.path

errors = []
html = Read.read_web_page("https://fancy-khapse-c03d84.netlify.app/")
parse = HtmlParser(html)

errors = parse.check_alt_text()


# html = Read.read_web_page("https://legacy.winnipeg.ca/interhom/accessibility/default.stm")
# parse = HtmlParser(html)

# errors += parse.check_alt_text()


for error in errors:
    print(error)
test = Job("helloslurm",12,"docker run html-image",dict(time="12:0:0",output="words.json",mailtype="BEGIN,END,FAIL",mem="4G",mailuser="ummarin9@myumanitoba.ca"))
print(test.sbatchString())
print(os.path.isfile("test.txt"))
schduleJob(test)
