from read import Read
from htmlparser import HtmlParser
from accesError import accessError

html = Read.read_web_page("https://www.w3schools.com/python/python_comments.asp")
parse = HtmlParser(html)

parse.check_alt_text()
Dict = dict({'best': '1', 'boy': '2'})
test = accessError("test","mc-test", Dict)
print(test)