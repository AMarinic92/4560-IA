from read import Read
from htmlparser import HtmlParser
class accessMl:
    def __init__(self,website):
        self.web = website
        self.html = Read().read_web_page(self.web)
        self.parser = HtmlParser(self.html)
    
    def get_missing_alt(self):
            out = self.parser.get_missing_alt_text()

    def get_captions(self):
        missing = get_missing_alt()
        toCaption = []
        asArg = ""
        if(missing != None):
            for image in missing:
                src = image.get("img",-1)
                if(src != -1):
                    toCaption.append(src)
                    asArg += " "+src

