from flask_restful import Resource

from .responces import Resp


class Status(Resource):
    def get(self):
        return Resp.ok()
