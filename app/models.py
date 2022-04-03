from app import db
from sqlalchemy_utils import ChoiceType

from uuid import uuid4
import datetime, enum

# method to generate uuid
def generate_uuid():
    return str(uuid4())

class Instruction(db.Model):
    __tablename__ = "instructions"

    uuid = db.Column(db.String(255), nullable=False, unique=True, default=generate_uuid, primary_key=True)
    user = db.Column(db.String(255), nullable=False)
    step = db.Column(db.String(255), nullable=False)
    command = db.Column(db.String(255), nullable=False)
    tag = db.Column(db.String(255), nullable=False)
    target = db.Column(db.String(255), nullable=False)
    short_desc = db.Column(db.Text())
    
    created = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    

    def __init__(self, user, step, command, tag, short_desc,target):
        self.user = user
        self.step = step
        self.short_desc = short_desc
        self.command = command
        self.tag = tag
        self.target = target

class WhiteList(db.Model):
    __tablename__ = "whitelist"

    uuid = db.Column(db.String(255), nullable=False, unique=True, default=generate_uuid, primary_key=True)
    ip = db.Column(db.String(255), nullable=False)
    allowed = db.Column(db.String(2), nullable=False)
    
    created = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    

    def __init__(self, ip, allowed):
        self.ip = ip
        self.allowed = allowed