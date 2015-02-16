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

from configobj import ConfigObj
import pprint

class Config:

    def __init__(self, file):
        self.file = file
        self.config = ConfigObj(file)

    def __str__(self):
        res = ''
        pp = pprint.PrettyPrinter(indent=4)
        res += "{0}\n".format("*"*13)
        res += "Config Object\n"
        res += "{0}\n".format("*"*13)
        res += "File: {0}\n".format(self.file)
        res += pp.pformat(self.config)
        res += "{0}\n".format("*"*13)
        res += "Config Object\n"
        res += "{0}\n".format("*"*13)
        return res

    def get(self, key):
        return self.config[key]

    def getConfig(self):
        return self.config
