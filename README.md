simple tornado app suitable for AppFog deployment
ideally, connected to a mysql server

 - mkvirtualenv -p `which python2.7`
 - ``pip install -r requirements.txt``
 - python server.py --help
 - python server.py --db_host=localhost --db_name=somedb
 - salt to taste
 - ``af push <appname>`` will deploy wsgi.py
 
