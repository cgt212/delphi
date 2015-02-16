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
