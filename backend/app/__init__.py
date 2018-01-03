import time
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

application = Flask(__name__)
application.config.from_object('app.config.Debug')
api = Api(application)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
CORS(application)

start_time = time.time()

from .views import *
