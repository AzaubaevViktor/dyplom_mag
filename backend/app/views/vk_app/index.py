from flask import request
from flask_restful import Resource

from app import db
from app.views.responces import Resp
from .models import VkApp
from .schema import VkAppSchema


class VkAppView(Resource):
    def __init__(self):
        super(VkAppView, self).__init__()
        self._actions = {
            'create': self._create,
            'update': self._update,
            'delete': self._delete
        }

    def get(self, app_id=-1):
        schema = VkAppSchema()
        if -1 == app_id:
            vk_apps = VkApp.query.all()
            result = schema.dump(vk_apps, many=True)
            return Resp.ok(items=result.data)
        else:
            vk_app = VkApp.query.get(app_id)
            result = schema.dump(vk_app)
            return Resp.ok(items=result.data)

    def post(self):
        schema = VkAppSchema()
        vk_app, errors = schema.load(request.json)

        if errors:
            return Resp.error(errors)

        action = request.json.get('action', 'create')
        f = self._actions.get(action, self._action_unknown)

        result = f(vk_app)

        db.session.commit()

        return result

    def _action_unknown(self, vk_app):
        return Resp.error({
            'action': "Unknown action. Action must be one of `{}`".format(
                "`, `".join(self._actions.keys())
            )
        })

    def _create(self, vk_app):
        db.session.add(vk_app)
        return Resp.ok()

    def _update(self, vk_app_update: VkApp):
        vk_app = VkApp.query.get(vk_app_update.app_id)  # type: VkApp
        VkApp.query.filter(
            VkApp.app_id == vk_app_update.app_id
        ).update(
            vk_app
        )

        return Resp.ok()

    def _delete(self, vk_app: VkApp):
        db.session.delete(vk_app)

        return Resp.ok()
