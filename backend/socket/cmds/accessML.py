import os
from read import Read
from htmlparser import HtmlParser
from dotenv import load_dotenv
load_dotenv() 


USER = os.getenv("UM_USERNAME")

import subprocess
class accessMl:
    def __init__(self,website):
        self.web = website
        self.html = Read().read_web_page(self.web)
        self.parser = HtmlParser(self.html)
    
    def get_missing_alt(self):
            out = self.parser.check_alt_text()
            return out

    def get_captions(self):
        missing = self.get_missing_alt()
        #toCaption = ["python","dockerHelper.py"]
        toCaption = ["docker","run","--runtime=nvidia","--gpus","1","tensor-image", "python", "dockerHelper.py"]
        endOfCommand = len(toCaption)
        asArg = ""
        if(missing != None):
            for image in missing:
                src = image.get("img",-1)
                if(not self.isGif(src)):
                    if(src != -1):
                        toCaption.append(self.hasHttp(src))
                        asArg += " "+src
                    
            if(len(toCaption)>0):
                pass
        #print(toCaption)
        compProcess = subprocess.run(toCaption,capture_output=True, text=True,user= USER)
        out = compProcess.stdout
        return out
    
    def hasHttp(self,src):
        split_src = src.split("//")
        size = len(split_src)
        out = src
        if(size<2):
            split_site = self.web.split("//")
            out = split_site[0]+"//"
            split_src = split_site[1].split("/")
            out += split_src[0]+"/"+src
        return out
    
    def isGif(self,src):
        split_src = src.split("gif")
        out = False
        if(len(split_src)>1):
            out = True
        return out