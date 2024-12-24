import os
from dotenv import load_dotenv
from redis import Redis

load_dotenv()

KVS_HOST = os.environ.get('KVS_HOST', "localhost")
KVS_PORT = os.environ.get('KVS_PORT', "6379")

class RedisSessionClient:

    def __init__(self) -> None:
        self.client = Redis(
            host=KVS_HOST,
            port=int(KVS_PORT),
            decode_responses = True
        )

    def set(self, key: str, value: dict, exp: int | None = 3600) -> None:
        self.client.hmset(key, value)
        self.client.expire(key, exp)


    def get(self, key: str) -> dict:
        return self.client.hgetall(key)
