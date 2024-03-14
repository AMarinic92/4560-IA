from aiohttp import web
import socketio
import json as Json

sio = socketio.AsyncServer(async_mode='aiohttp',cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)

@sio.on('parse')
def another_event(sid, json):
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

    

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__=='__main__':
    web.run_app(app, host='0.0.0.0', port=5000)
