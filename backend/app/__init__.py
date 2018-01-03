from flask import Flask
from flask_restful import Api

application = Flask(__name__)
application.config.from_object('app.config.Debug')
api = Api(application)

from .views import *
