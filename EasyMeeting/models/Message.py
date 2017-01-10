#! encoding=utf-8
from EasyMeeting.foundation import db
from datetime import datetime
import random
import hashlib
from flask import current_app
from EasyMeeting.models import User

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text)
    send_time = db.Column(db.DateTime)
    creator_id = db.Column(db.Integer)
    receiver_id = db.Column(db.Integer)
    status = db.Column(db.Integer)
    NEW,HAVEREAD,DELETED = range(3)
    def __init__(self,**args):
        for k,v in args.items():
            setattr(self,k,v)
        if not args.has_key("status"):
            self.status = Message.NEW
    def read(self):
    	self.status = HAVEREAD
    def delete(self):
        self.status = DELETED
    def getdetail(self):
        details = {}
        details['send_time'] = self.start_time
        details['creator_name'] = User.get_by_id(self.creator_id).getname()
        details['content'] = self.content
        details['status'] = self.status
        return details
    @staticmethod
    def get_by_id(id):
        return Message.query.filter_by(id = id).first()
    @staticmethod
    def get_by_creator_id(id):
        return Message.query.filter_by(creator_id = id)
    @staticmethod
    def get_by_receiver_id(id):
        return Message.query.filter_by(receiver_id = id,status = NEW)
    @staticmethod
    def newMessage(content, send_time, creator_id, receiver_id):
        message = Message(content = content,send_time = send_time,creator_id = creator_id, receiver_id = target_id)
        db.session.add(message)
        db.session.commit()
