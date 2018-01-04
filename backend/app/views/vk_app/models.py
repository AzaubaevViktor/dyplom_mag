from app import db


class VkApp(db.Model):
    app_id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), nullable=True)
    expire = db.Column(db.TIMESTAMP(timezone=True))
