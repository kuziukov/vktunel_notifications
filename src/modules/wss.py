import json


class WSSessionData:

    def __get__(self, obj, objtype):
        if obj._data is None:
            data = notification_store.get(obj.key)
            if data is not None:
                obj._data = json.loads(data)
        return obj._data

    def __set__(self, obj, value):
        obj._data = value


class WSSession(object):

    data = WSSessionData()

    def __init__(self, store, key):
        self._key = key
        self.data = None
        self._notification_store = store

    async def get_data(self):
        data = await self._notification_store.get(self._key)
        if data is not None:
            response = json.loads(data)
        return response

    async def is_exists(self):
        return await self._notification_store.exists(self.key)

    async def destroy(self):
        return await self._notification_store.delete(self.key)

    @property
    def key(self):
        return self._key.decode('utf-8') if isinstance(self._key, bytes) else self._key
