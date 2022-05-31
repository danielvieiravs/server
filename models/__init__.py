import uuid

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.Model):
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String())
    content = db.Column(db.String())
    published = db.Column(db.String())
    url = db.Column(db.String(), unique=True)
