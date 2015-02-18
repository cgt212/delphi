# delphi
RESTful key value store with the concept of environments.  

Generic key value store, currently backed by a Redis database.  The primary purpose is to have requests from different
environments be handled specific to that environment.  The initial idea for this came to have a single source of truth for 
multiple environments.  

<hr />

# Dependencies

The most current list of dependencies will be in the requirements.txt file included in the source.

# Examples

Using the sample configuration, there is a backend for the local (127.0.0.0/8) subnet and a different backend for the intranet subnet (192.168.0.0/16).  

Run the app ./app.py

Put some values into the backend:

curl -X PUT http://localhost:5000/dns/resolver -d 'data={ "value": "192.168.1.1" }'
curl -X PUT http://localhost:5000/dns/domain -d 'data={ "value": "whatbroke.com" }'

Now get some values back out:

Using the same source (127.0.0.1):
<pre><code>
curl localhost:5000/dns/
['domain', 'resolver']
</code></pre>

Using the other source (192.168.0.0):
<pre><code>
curl 192.168.1.4:5000/dns/
[]
</code></pre>

Getting the actual value back:
<pre><code>
curl localhost:5000/dns/resolver
192.168.1.1
</code></pre>

From the other source:
<pre><code>
curl 192.168.1.4:5000/dns/resolver
[]
</code></pre>

Add a value into the intranet backend:
<pre><code>
curl -X PUT http://192.168.1.4:5000/dns/resolver -d 'data={ "value": "192.168.1.2" }'
192.168.1.2
</code></pre>

Now there are 2 different values depending on the source:
<pre><code>
curl http://localhost:5000/dns/resolver
192.168.1.1
curl http://192.168.1.4:5000/dns/resolver
192.168.1.2
</code></pre>
