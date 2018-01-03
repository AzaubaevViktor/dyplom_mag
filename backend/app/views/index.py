import time
from flask_restful import Resource

from app import start_time
from .responces import Resp


class Status(Resource):
    def get(self):
        return Resp.ok(uptime=time.time() - start_time)
