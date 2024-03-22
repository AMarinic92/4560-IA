import sys 
sys.path.insert(0,'./cmds')
from aiohttp import web
import socketio
from accessML import accessMl
from presentation.mlpresentation import image_analysis

sio = socketio.AsyncServer(async_mode='aiohttp',cors_allowed_origins='*', ping_timeout=300)
app = web.Application()
sio.attach(app)

@sio.event
async def connect(sid, environ, auth):
    print('connect ', sid)
    

@sio.on('parse')
async def another_event(sid, json):
    web_url = json.get("website",-1)
    response = await image_analysis(web_url)
    print(response)
    await sio.emit("reply",response ,room = sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__=='__main__':
    web.run_app(app, host='0.0.0.0', port=5000)
