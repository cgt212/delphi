from redis import Redis

class RedisStore():
    def __init__(self, **kwargs):
        self.db = Redis(**kwargs)
        print "{0}".format(self.db)

    def get(self, key):
        return self.db.get(key)

    def put(self, key, value):
        return self.db.set(key, value)

    def post(self):
        pass

    def delete(self, path):
        self.db.delete(path)
