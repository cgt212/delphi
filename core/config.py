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
