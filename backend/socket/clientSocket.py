import socketio

sio = socketio.AsyncSimpleClient()

async def connect():
    await sio.connect('http://localhost:5000')

connect()