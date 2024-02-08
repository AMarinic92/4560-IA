from read import Read
from htmlparser import HtmlParser


html = Read.read_web_page("https://www.geeksforgeeks.org/how-to-import-a-class-from-another-file-in-python/")
parse = HtmlParser(html)

print(parse.get_image_tags())
