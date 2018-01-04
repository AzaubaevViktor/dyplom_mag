from marshmallow import Schema, fields, post_load

from .models import VkApp


class VkAppSchema(Schema):
    app_id = fields.Integer()
    key = fields.Str()
    expire = fields.DateTime()

    @post_load
    def make_vk_app(self, data):
        return VkApp(**data)
