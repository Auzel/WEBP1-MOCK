from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from datetime import datetime


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stream = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
