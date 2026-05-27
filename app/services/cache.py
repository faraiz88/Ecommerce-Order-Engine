import redis
import json


client = redis.Redis(
    host="redis",
    port=6379,
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