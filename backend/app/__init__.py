from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config.from_object('app.config.Debug')
api = Api(application)
db = SQLAlchemy(application)
migrate = Migrate(application, db)

from .views import *
