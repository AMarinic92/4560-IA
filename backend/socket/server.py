from aiohttp import web
import socketio

sio = socketio.AsyncServer(async_mode='aiohttp',cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

@sio.event
async def connect(sid, environ, auth):
    print('connect ', sid)
    await sio.enter_room(sid,sid)



@sio.on('parse')
async def another_event(sid, json):
    print("obj:", json)
   # await sio.enter_room(sid,json["website"])
    await sio.emit("reply","response",room=sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__=='__main__':
    web.run_app(app, host='0.0.0.0', port=5000)
