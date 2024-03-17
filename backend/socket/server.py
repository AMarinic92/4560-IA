from aiohttp import web
import socketio
import json as Json

sio = socketio.AsyncServer(async_mode='aiohttp',cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

@sio.event
async def connect(sid, environ, auth):
    print('connect ', sid)
    



@sio.on('parse')
async def another_event(sid, json):
    print("obj:", json)
    asDict = Json.loads(json)
    url = asDict.get("url", -1)
    cmd = asDict.get("cmd", -1)
    if(url != -1 and cmd != -1):
        pass
        #do the ml command here perhaps loop while it is doing its thing with timeout
    else:
        pass
        #oopsie poopsie we need error handling

    

    # server response example
    # where id is unique
    # image url is image the image url
    # type is type of alt text issue
    # suggestion
    responseEg = {
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
    await sio.emit("reply",responseEg ,room = sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__=='__main__':
    web.run_app(app, host='0.0.0.0', port=5000)
