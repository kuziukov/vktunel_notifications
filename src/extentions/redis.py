import aioredis
from config import (
    NOTIFICATION_STORE_URI
)


async def setup_redis(app, loop):
    notification_store = await aioredis.create_redis_pool(NOTIFICATION_STORE_URI, loop=loop)

    async def close_redis(app):
        notification_store.close()
        await notification_store.wait_closed()

    app.on_cleanup.append(close_redis)
    app.notification_store = notification_store
