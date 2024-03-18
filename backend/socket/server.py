import sys 
sys.path.insert(0,'./cmds')
from aiohttp import web
import socketio
from accessML import accessMl
import subprocess

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
    checker = accessMl(web_url)
    if(checker.get_missing_alt()==None):
        response = {"response":[]}
    else:
        checker.get_captions()
    # server response example
    # where id is unique
    # image url is image the image url
    # type is type of alt text issue
    # suggestion
    
    """
    response = {
        "response":[
            {
                "id":0,
                "imageUrl":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/40._Schwimmzonen-_und_Mastersmeeting_Enns_2017_100m_Brust_Herren_USC_Traun-9897.jpg/1024px-40._Schwimmzonen-_und_Mastersmeeting_Enns_2017_100m_Brust_Herren_USC_Traun-9897.jpg",
                "type":"bad alt txt",
                "message":"",
                "suggestion":"guy swimming in a pool"

            },
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
