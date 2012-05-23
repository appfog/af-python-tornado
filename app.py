from tornado import web
from tornado import database
from tornado.options import options, define

define("port", default=8000, help="http port", type=int)
define("cookie_secret", default="not-much-of-a-secret")
define("debug", default=False, help="debug mode", type=bool)
define("db_host", default="localhost", help="mysql server")
define("db_name", default="tornadoze", help="database name")
define("db_user", default="root", help="database user")
define("db_pass", default="", help="database password")

class Home(web.RequestHandler):
    def get(self):
        try:
            dbconn = self.settings['db']
            tables = [t.values()[0] for t in dbconn.query("show tables")]
            dbname = dbconn.database
        except KeyError:
            tables = []
            dbname = "(no database connected)"
        self.render("home.html", dbname=dbname, tables=tables)

settings = dict(
    template_path="templates",
    static_path="static",
    xsrf_cookies=True,
    cookie_secret=options.cookie_secret,
    debug=options.debug,
)

routes = [
    (r"/", Home),
]

