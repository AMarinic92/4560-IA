from read import Read
from htmlparser import HtmlParser

html = Read.read_web_page("https://www.lingscars.com/")
parse = HtmlParser(html)

errors = parse.check_alt_text()
for error in errors:
    print(error)