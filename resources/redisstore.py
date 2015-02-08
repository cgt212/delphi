from redis import Redis

class RedisStore():
    def __init__(self, **kwargs):
        self.db = Redis(**kwargs)
        print "{0}".format(self.db)

    def get(self, key):
        ret = self.db.get(key)
        if ret is None:
            ret = []
            if key[-1] == '/':
                for child in self.db.scan_iter(key + '*'):
                    ret.append(child[len(key):])
        return ret

    def put(self, key, value):
        return self.db.set(key, value)

    def post(self):
        pass

    def delete(self, path):
        self.db.delete(path)
