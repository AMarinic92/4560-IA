import sys 
sys.path.insert(0,'./cmds')
from aiohttp import web
import socketio
from accessML import accessMl

import json as js
from presentation.mlpresentation import image_analysis

sio = socketio.AsyncServer(async_mode='aiohttp',cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

@sio.event
async def connect(sid, environ, auth):
    print('connect ', sid)
    



@sio.on('parse')
async def another_event(sid, json):
    web_url = json.get("website",-1)
    print(web_url)
    response = await image_analysis(web_url)
    # checker = accessMl(web_url)
    # if(checker.get_missing_alt()==None):
    #     print("Alt text appears good for job",sid)
    #     response = {"response":[]}
    # else:
    #    print("Finding caption for alt text for job: ",sid)
    #    results = checker.get_captions()
    #    results = results.split("},")
    #    response = {"response":[]}
    #    x = 0
    #    for result in results:
    #         if(x<len(results)-1):
    #             result +="}"
    #         else:
    #             result = result[:-1]
    #         print(result)
    #         x += 1
    #         #This area here appears to be broken the JSON string received from the docker
    #         #Does not parse correctly and I get an error I am not sure why
    #         js_obj = js.loads(result)
    #         response.get("response").append(js_obj)

    print(response)

    """
    response = {
        "response":[
            {
                "id":0,
                "imageUrl":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/40._Schwimmzonen-_und_Mastersmeeting_Enns_2017_100m_Brust_Herren_USC_Traun-9897.jpg/1024px-40._Schwimmzonen-_und_Mastersmeeting_Enns_2017_100m_Brust_Herren_USC_Traun-9897.jpg",
                "type":"bad alt txt","message":"", "suggestion":"guy swimming in a pool"},
            {
                "id":1,
                 "imageUrl":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/40._Schwimmzonen-_und_Mastersmeeting_Enns_2017_100m_Brust_Herren_USC_Traun-9897.jpg/1024px-40._Schwimmzonen-_und_Mastersmeeting_Enns_2017_100m_Brust_Herren_USC_Traun-9897.jpg",
                "type":"bad alt txt",
                "message":"",
                "suggestion":"guy swimming in a pool"

            }
        ]
    }
    """
    await sio.emit("reply",response ,room = sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__=='__main__':
    web.run_app(app, host='0.0.0.0', port=5000)
