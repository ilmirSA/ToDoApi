from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dataclasses import dataclass
from . import db



@dataclass
class Task(db.Model):
    id:int
    title:str
    description:str
    created_at:datetime
    updated_at:datetime

    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
