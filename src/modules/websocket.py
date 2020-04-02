import aiohttp


async def websocket_echo_handler(ws):
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                try:
                    await ws.send_str(msg.data + '/answer')
                except Exception:
                    await ws.close()
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    return ws
