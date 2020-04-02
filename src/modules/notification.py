import asyncio
import logging


async def notification_echo_handler(store, ws, topic):
    try:
        channel, *_ = await store.subscribe(topic)
        while await channel.wait_message():
            try:
                message = await channel.get_json()
                for i in ws:
                    await i.send_json(message)
            except Exception:
                pass
    except asyncio.CancelledError:
        logging.error('CancelledError exception received. Unsubscribe from: %s', topic)
        await store.unsubscribe(topic)
        for i in ws:
            await i.close()

