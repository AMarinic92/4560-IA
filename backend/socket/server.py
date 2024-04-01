import sys

from cache.cache import cache_response , create_cache , get_cached_response
sys.path.insert(0,'./cmds')
from aiohttp import web
import socketio
from accessML import accessMl
from presentation.mlpresentation import image_analysis
from presentation.mlpresentation import link_analysis

sio = socketio.AsyncServer(async_mode='aiohttp',cors_allowed_origins='*', ping_timeout=300)
app = web.Application()
sio.attach(app)

@sio.event
async def connect(sid, environ, auth):
    print('connect ', sid)
    

@sio.on('parse')
async def another_event(sid, json):
    web_url = json.get("website",-1)
    response_db = get_cached_response(web_url)
    if response_db:
        await sio.emit("reply",response_db ,room = sid)
        return
    response = await image_analysis(web_url)
    response = await response["response"].append(link_analysis(web_url))
  # response["response"].append({"url":web_url})
  #  print(response)
    cache_response(response ,web_url)
    await sio.emit("reply",response ,room = sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__=='__main__':
    create_cache()
    web.run_app(app, host='0.0.0.0', port=5000)
