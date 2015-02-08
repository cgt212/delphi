from resources.redisstore import RedisStore

class Backend:
    def __init__(self, config):
        self.config = config
        self._loadStorage()

    def _loadStorage(self):
        if len(self.config) == 0:
            return
        self.backends = {}
        for backend in self.config:
            print "Loading backend {0} => {1}".format(backend, self.config[backend])
            self.backends[backend] = RedisStore(**self.config[backend])

    def getBackend(self, name):
        return self.backends.get(name, None)
