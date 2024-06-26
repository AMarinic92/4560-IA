import socketio
import asyncio

sio = socketio.AsyncSimpleClient()


async def main():
    await sio.connect('http://localhost:5000')
    
    await sio.emit('parse',{"website":"https://fancy-khapse-c03d84.netlify.app"})
    event = await sio.receive()
    print(f'received event: "{event[0]}" with arguments {event[1:]}')
    await sio.disconnect()

asyncio.run(main())
