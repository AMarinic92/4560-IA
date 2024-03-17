import socketio
import asyncio

sio = socketio.AsyncSimpleClient()


async def main():
    await sio.connect('http://localhost:5001')
    await sio.emit('parse',{"website":"google.com"})
    event = await sio.receive()
    print(f'received event: "{event[0]}" with arguments {event[1:]}')
    await sio.disconnect()

asyncio.run(main())
