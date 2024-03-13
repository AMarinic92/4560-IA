import socketio


sio = socketio.AsyncServer()

app = socketio.ASGIApp(sio )


@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)

@sio.on('parse')
def another_event(sid, json):
    print("obj:", json)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

