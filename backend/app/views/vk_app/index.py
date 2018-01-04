from flask import request
from flask_restful import Resource

from app import db
from app.views.responces import Resp
from .models import VkApp
from .schema import VkAppSchema


class VkAppView(Resource):
    def get(self, app_id=-1):
        schema = VkAppSchema()
        if -1 == app_id:
            vk_apps = VkApp.query.all()
            result = schema.dump(vk_apps, many=True)
            return result.data
        else:
            vk_app = VkApp.query.get(app_id)
            result = schema.dump(vk_app)
            return result.data

    def post(self):
        schema = VkAppSchema()
        vk_app, errors = schema.load(request.json)
        if not errors:
            db.session.add(vk_app)
            db.session.commit()

        return Resp.ok()
