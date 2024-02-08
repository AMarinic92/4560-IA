from bs4 import BeautifulSoup

class HtmlParser:
    def __init__(self,html) :
        self.soup = BeautifulSoup(html, 'html.parser')


    def get_image_tags(self):
         return self.soup.find_all("img")
