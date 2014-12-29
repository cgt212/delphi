from flask import abort
from flask import Flask
from flask import request
import json
from resources.redisstore import RedisStore
from werkzeug.routing import BaseConverter

app = Flask(__name__)

@app.route("/<path:path>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def api(path):
    app.logger.debug("New Request: {0}".format(request.form))
    app.logger.debug("Request method: {0}".format(request.method))
    store = RedisStore()
    if request.method == 'GET':
        val = store.get(path)
        if val is None:
            return '', 404
        else:
            return "{0}\n".format(val)
    elif request.method == 'POST':
        app.logger.debug("Got POST Request")
        #Check to see if that value exists, POST is write once - use PUT to update
        val = store.get(path)
        app.logger.debug("Pulled value {0} from the store".format(val))
        if val is None:
            #This means that there was nothing found, so we can add a value
            data = json.loads(request.form['data'])['value']
            app.logger.debug("No value for {0}, so creating value: {1}".format(path, data))
            store.put(path, data)
            return "{0}\n".format(data), 201
        else:
            app.logger.debug("Found value for {0}: {1}".format(path, val))
            abort(409)
    elif request.method == 'PUT':
        #As stated in POST, here we can just overwrite any existing value
        data = json.loads(request.form['data'])['value']
        store.put(path, data)
        return "{0}\n".format(data), 201
    elif request.method == 'DELETE':
        store.delete(path)
        #There is no value to return, so just abort and return the deleted code
        return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
