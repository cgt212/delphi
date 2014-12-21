from flask.ext import restful
from redis import Redis

redis = Redis()

class RedisStore(restful.Resource):
    def get(self, path):
    def put(self):
    def post(self):
    def delete(self):
