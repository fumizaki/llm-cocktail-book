import os
from dotenv import load_dotenv
from redis import Redis

load_dotenv()

REDIS_HOST = os.environ.get('REDIS_HOST', "localhost")
REDIS_PORT = os.environ.get('REDIS_PORT', "6379")

class RedisSessionClient:

    def __init__(self) -> None:
        self.client = Redis(
            host=REDIS_HOST,
            port=int(REDIS_PORT),
            decode_responses = True
        )

    def set(self, key: str, value: dict, exp: int | None = 3600) -> None:
        self.client.hmset(key, value)
        self.client.expire(key, exp)


    def get(self, key: str) -> dict:
        return self.client.hgetall(key)
