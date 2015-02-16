"""
    This file is part of Delphi.

    Delphi is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Delphi is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Delphi.  If not, see <http://www.gnu.org/licenses/>.
"""

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
