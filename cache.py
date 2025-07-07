# app/services/cache.py
import redis.asyncio as redis
import json
from app.config.settings import settings

class RedisCache:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.REDIS_HOST,  # type: ignore
            port=settings.REDIS_PORT,  # type: ignore
            decode_responses=True
        )

    async def get(self, key: str):
        value = await self.client.get(key)
        if value:
            return json.loads(value)
        return None

    async def set(self, key: str, value: dict, expire: int):
        await self.client.setex(key, expire, json.dumps(value))

    async def close(self):
        await self.client.close()