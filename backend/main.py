from read import Read
from htmlparser import HtmlParser


errors = []
html = Read.read_web_page("https://fancy-khapse-c03d84.netlify.app/")
parse = HtmlParser(html)

errors = parse.check_alt_text()


# html = Read.read_web_page("https://legacy.winnipeg.ca/interhom/accessibility/default.stm")
# parse = HtmlParser(html)

# errors += parse.check_alt_text()


for error in errors:
    print(error)