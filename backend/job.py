import os.path

class Job:
    def __init__(self,name,id,job,opt):
        self.name = name #name of job
        self.id = id #id of job (so we can have the same job type running multiple instances)
        self.opt = opt #opts will be a dictonary that I will use for all the options you want for the job. so for example if you wanted to use the email function youd 
        self.status = 0
        self.job = job

#generate a sbatch file string
    def sbatchString(self):
        sbatchString = "#!/bin/bash\n#\n# ["+self.name+str(self.id)+".sbatch]\n#\n#SBATCH --job-name="+self.name+str(self.id)+"\n"
        if(type(self.opt) is dict):
            #check for output option
            if(self.opt.get("output",-1) != -1):
                sbatchString += "#SBATCH --output="+self.opt.get("output")+"\n"
            else:
                sbatchString += "#SBATCH --output="+self.name+str(self.id)+".out\n#SBATCH --export=ALL\n"
            if(self.opt.get("time",-1) != -1):
                sbatchString += "#SBATCH --time="+str(self.opt.get("time"))+"\n"
            else:
                sbatchString += "#SBATCH --time=00:01:00\n"
            if(self.opt.get("mem",-1) != -1):
                sbatchString += "#SBATCH --mem="+self.opt.get("mem")+"\n"
            else:
                sbatchString += "#SBATCH --mem=4G\n"
            if(self.opt.get("mailtype",-1) != -1):
                sbatchString += "#SBATCH --mail-type="+self.opt.get("mailtype")+"\n"
            if(self.opt.get("mailuser",-1) != -1):
                sbatchString += "#SBATCH --mail-user="+self.opt.get("mailuser")+"\n"
            if(self.opt.get("partition",-1) != -1):
                sbatchString += "#SBATCH --partition="+self.opt.get("partition")+"\n"
            else:
                sbatchString += "#SBATCH --partition=LongQ\n"
            sbatchString += "\n\n\n"+self.job
                

        else:
            sbatchString += "#SBATCH --output="+self.name+str(self.id)+".out\n#SBATCH --export=ALL\n#SBATCH --time=00:01:00\n#SBATCH --mem=4G\n#SBATCH --partition=LongQ\n\n\n\n\n"+self.job
        
        return sbatchString
    

    # Function to open a new file with write mode, and write the sbatch file
    def sbatchGen(self):
        file = open(self.getLocation(),"w")
        file.write(self.sbatchString())
        
    # Returns the location where the sbatch file is stored. 
    def getLocation(self):    
        outstring = "/tmp/" 
        if(type(self.opt) is dict):
            if(self.opt.get("op",-1) != -1):
                outstring = str(self.opt.get("op"))+".sbatch"
            else:
                outstring += str(self.name)+str(self.id)+".sbatch"

        else:
            outstring += str(self.name)+str(self.id)+".sbatch"
        return outstring

       
        
        

