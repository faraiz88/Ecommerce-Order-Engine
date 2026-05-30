import json
import redis
from os import getenv


client = redis.Redis.from_url(
    getenv("REDIS_URL"),
    decode_responses=True
)


def get_cache(key):

    value = client.get(key)

    if value:
        return json.loads(value)

    return None


def set_cache(
    key,
    value,
    ttl=60
):

    client.setex(
        key,
        ttl,
        json.dumps(value)
    )