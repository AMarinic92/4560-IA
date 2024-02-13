from read import Read
from htmlparser import HtmlParser


html = Read.read_web_page("https://www.w3schools.com/python/python_comments.asp")
parse = HtmlParser(html)

parse.check_alt_text()


