from aiohttp import web
import socketio

sio = socketio.AsyncServer(async_mode='aiohttp',cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)

@sio.on('parse')
def another_event(sid, json):
    print("obj:", json)
    sio.enter_room(sid,json["website"])
    sio.emit("reply","response",room=json["website"])


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__=='__main__':
    web.run_app(app, host='0.0.0.0', port=5000)
