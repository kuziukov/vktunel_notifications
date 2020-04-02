import asyncio
import aiohttp
import logging

from modules import (
    websocket_echo_handler,
    notification_echo_handler
)
from modules.wss import WSSession


async def notification_ws_get(request):
    app = request.app
    store = request.app.notification_store
    topic = request.match_info.get('code', None)

    ws = aiohttp.web.WebSocketResponse()
    await ws.prepare(request)


    session = WSSession(store=store, key=topic)
    if not await session.is_exists():
        raise aiohttp.web.HTTPUnauthorized()

    data = await session.get_data()
    topic = data['user_id']
    await session.destroy()

    logging.debug('New websocket connection')

    if topic not in app['sockets']:
        app['sockets'][topic] = []
        task = asyncio.create_task(notification_echo_handler(store, app['sockets'][topic], topic))
        app['tasks'][topic] = task
    app['sockets'][topic].append(ws)

    try:
        await asyncio.gather(websocket_echo_handler(ws))
    finally:
        logging.debug('Connection closed')
        app['sockets'][topic].remove(ws)
        if len(app['sockets'][topic]) == 0:
            app['sockets'].pop(topic)
            task = app['tasks'].pop(topic)
            task.cancel()

    return ws


