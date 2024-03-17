from aiohttp import web
import socketio

sio = socketio.AsyncServer(async_mode='aiohttp',cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

@sio.event
async def connect(sid, environ, auth):
    print('connect ', sid)
    



@sio.on('parse')
async def another_event(sid, json):
    print("obj:", json)
   
    responseEg = {
        "response":[
            {
                "id":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/40._Schwimmzonen-_und_Mastersmeeting_Enns_2017_100m_Brust_Herren_USC_Traun-9897.jpg/1024px-40._Schwimmzonen-_und_Mastersmeeting_Enns_2017_100m_Brust_Herren_USC_Traun-9897.jpg",
                "type":"bad alt txt",
                "message":"",
                "suggestion":"guy swimming in a pool"

            },
            {
                "id":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/40._Schwimmzonen-_und_Mastersmeeting_Enns_2017_100m_Brust_Herren_USC_Traun-9897.jpg/1024px-40._Schwimmzonen-_und_Mastersmeeting_Enns_2017_100m_Brust_Herren_USC_Traun-9897.jpg",
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
