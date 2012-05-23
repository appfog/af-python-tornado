import os
import json
from tornado import wsgi
from tornado import database
from tornado.options import options
from app import routes, settings

services = json.loads(os.environ.get('VCAP_SERVICES', '{}'))
if services:
    creds = services['mysql-5.1'][0]['credentials']
    settings['db'] = database.Connection(
        creds['host'],
        creds['name'],
        user=creds['username'],
        password=creds['password']
        )
    
application = wsgi.WSGIApplication(routes, **settings)
