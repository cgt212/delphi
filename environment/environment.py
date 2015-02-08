class Environment:
    def __init__(self, name, backend):
        self.name = name
        self.backends = backend

    def getPath(self, path):
        for db in self.backends:
            res = db.get(path)
            if res is not None:
                break
        return res

    def put(self, path, value):
        db = self.backends[0]
        if db is None:
            return None
        db.put(path, value)
