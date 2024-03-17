#This class creates an accessibility error, and creates a message to output. 

class accessError:
    def __init__(self,name,type,res):
        self.name = name
        self.type = type
        self.res = res # resources say a dict with a src link and alt text for image 
    
    def __str__(self):
        return 'Acessibility Error '+self.name+': '+self.type+' Identifier:'+str(self.res)+'\n'