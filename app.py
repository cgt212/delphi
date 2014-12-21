from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class SplitConverter(BaseConverter):
    def __init__(self, url_map):
        super(SplitConverter, self).__init__(url_map)
        self.regex = "(?:.*)"

    def to_python(self, value):
        return value.split(u"/")

    def to_url(self, value):
        return u"/".join(value)

app.url_map.converters['split'] = SplitConverter

@app.route("/<split:args>")
def api(args):
    print "{0} Args".format(len(args))
    print "The zone is {0}".format(args[0])
    print "URL Components: {0}".format(args)
    return "Value: "

if __name__ == '__main__':
    app.run()
