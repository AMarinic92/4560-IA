import socketio
import asyncio

sio = socketio.AsyncSimpleClient()


async def main():
    await sio.connect('http://localhost:5001')
    await sio.disconnect()


asyncio.run(main())
