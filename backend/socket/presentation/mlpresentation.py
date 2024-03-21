from accessML import accessMl
import json as js
sys.path.insert(0,'./cmds')



async def image_analysis(web_url):
    checker = accessMl(web_url)
    if(checker.get_missing_alt()==None):
       # print("Alt text appears good for job",sid)
        response = {"response":[]}
    else:
      # print("Finding caption for alt text for job: ",sid)
       results = checker.get_captions()
       results = results.split("},")
       response = {"response":[]}
       x = 0
       for result in results:
            if(x<len(results)-1):
                result +="}"
            else:
                result = result[:-1]
            print(result)
            x += 1
            #This area here appears to be broken the JSON string received from the docker
            #Does not parse correctly and I get an error I am not sure why
            js_obj = js.loads(result)
            response.get("response").append(js_obj)

    print(response)
    return response