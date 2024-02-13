from bs4 import BeautifulSoup
from accesError import accessError

class HtmlParser:
    def __init__(self,html) :
        self.soup = BeautifulSoup(html, 'html.parser')


    def get_image_tags(self):
         return self.soup.find_all("img")
    
    def get_missing_alt_text(self):
         return self.soup.find_all("img", attrs={"alt": False})

    def get_blank_alt_text(self):
         return self.soup.find_all("img", attrs={"alt": ""})
    
    def check_alt_text(self):
         out = []
         image_tags = self.get_image_tags()
         for image in image_tags:
              if(image['src'] == "" ):
                    print("Image found with missing source, discarding")
                    out.insert(accessError("Alt text with no source","Image or Alt Text",image))
              elif(image.has_attr('alt')):
                    print("Alt text found on:",image['src']," with alt text:", image['alt'])
              elif(image.has_attr('alt') and image['alt'] == ""):
                    print("alt attribute present but blank check for decorative")
                    out.insert(accessError("Alt text blank, may be decroative","Image or Alt Text",image))
              elif(not(image.has_attr('alt'))):
                    print("MISSING ALT TEXT ATTRIBUTE",image)
                    out.insert(accessError("Alt attribute missing, maybe decroative","Image or Alt Text",image))
         return out