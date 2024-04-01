import sys
from accessML import accessMl
import json as js
sys.path.insert(0,'./cmds')

async def link_analysis(web_url):
    response = {"response":[]}
    checker = accessMl(web_url)
    response.get["response"].append(checker.get_bad_links)
    return response