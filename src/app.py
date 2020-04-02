from aiohttp import web
import asyncio
from web_sockets import (
    setup_socket_routes
)
from extentions import (
    setup_redis
)
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)


async def create_app(loop):
    app = web.Application()

    setup_socket_routes(app)
    await setup_redis(app, loop)
    app['sockets'] = {}
    app['tasks'] = {}

    return app


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(create_app(loop))
    web.run_app(app, port=8083)
