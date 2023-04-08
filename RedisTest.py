import redis


class RedisAgent:

    def __init__(self, host='...', port=123, db=0, password='123'):
        self._redis = redis.StrictRedis(host, port, db, password)

    def get(self, key):
        return self._redis.get(key)

    def set(self, key, value):
        self._redis.set(key, value)

    def scan_redis_string(self, match=None, count=None):
        return self._redis.scan_iter(match=match, count=count)

    def hget(self, key, field):
        return self._redis.hget(key, field)

    def hset(self, key, field, value):
        return self._redis.hset(key, field, value)

    def flush(self):
        return self._redis.flushdb()

    def delete(self, key):
        return self._redis.delete(key)


if __name__ == '__main__':
    test = RedisAgent()

