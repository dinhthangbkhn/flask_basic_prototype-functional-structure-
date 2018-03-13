from flask import Flask

# import config.default as cf_obj

app = Flask(__name__)
app.config.from_object('config.default')

from application.views import home
from application.views import about

app.register_blueprint(home.mod)
app.register_blueprint(about.mod)

from application.database import db_session
from application.models import User, Google, Yahoo


