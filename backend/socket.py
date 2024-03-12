import socketio

sio = socketio.Server()

app = socketio.ASGIApp(sio)


@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)