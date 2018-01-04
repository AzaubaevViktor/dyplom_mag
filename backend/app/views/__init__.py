from app import api
from .index import Status
from .vk_app import VkAppView

api.add_resource(index.Status, '/')
api.add_resource(vk_app.VkAppView, '/vk_app', '/vk_app/')
api.add_resource(vk_app.VkAppView,
                 '/vk_app/<int:app_id>',
                 endpoint="vkappview_id", methods=['GET'])

