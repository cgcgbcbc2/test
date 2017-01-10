#! encoding=utf-8
from EasyMeeting.foundation import db
from datetime import datetime
import random
import hashlib
from datetime import datetime
from flask import current_app
import json


class Members(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    activity_id = db.Column(db.Integer,db.ForeignKey('activity.id') )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Integer)
    PATICIPATIED,PASSED,REFUSED,CREATE = range(4)
    def delete(self):
        print("del mem")
        db.session.delete(self)
        db.session.commit()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    weixin_id = db.Column(db.Integer, db.ForeignKey('weixin_user.id'))
    loginkey_id = db.relationship("LoginKey", backref="User", uselist = False)
    activities = db.relationship('Members',backref="user",lazy='dynamic')
    username = db.Column(db.String(64), index = True, unique = True)
    intro = db.Column(db.String(64), default = "")
    password = db.Column(db.String(64))
    last_seen = db.Column(db.DateTime)
    name = db.Column(db.String(64), default = "")
    email = db.Column(db.String(64), default = "")
    mobile = db.Column(db.String(11), default = "")
    avator = db.Column(db.String(64), default = "/image/user/default.png")
    join_time = db.Column(db.DateTime)
    status = db.Column(db.Integer)

    @staticmethod
    def get_by_mobile(mobile):
        if not mobile:
            return None
        return User.query.filter_by(mobile = mobile).first()
    @staticmethod
    def get_by_name(name):
        return User.query.filter_by(status = User.MEMBER).filter_by(name = name).first()
    @staticmethod
    def get_by_id(id):
        print(id)
        return User.query.filter_by(id = id).first()
    def getname(self):
        return self.name
    def getdetail(self):
        details = {}
        details['name'] = self.name
        details['email'] = self.email
        details['mobile'] = self.mobile
        details['introduction'] = self.intro
        parti_list = []
        for i in self.get_participate_activities():
            parti_list.append(i.activity.getdetail())
        passed_list = []
        for i in self.get_passed_activities():
            passed_list.append(i.activity.getdetail())
        refused_list = []
        for i in self.get_refused_activities():
            refused_list.append(i.activity.getdetail())
        created_list = []
        for i in self.get_created_activities():
            created_list.append(i.activity.getdetail())
        details['avator'] = self.avator
        details['participated'] = parti_list
        details['passed'] = passed_list
        details['refused'] = refused_list
        details['created'] = created_list
        return details
    def modify(self,query):
        self.name = query.get('name')
        print(self.name)
        self.email = query.get('email')
        print(self.email)
        self.mobile = query.get('mobile')
        print(self.mobile)
        self.intro = query.get('introduction')
        print(self.intro)
        db.session.commit() 
    def get_activities(self):
        return self.activities.all()
    def get_created_activities(self):
        return db.session.query(Members).join(User).filter(Members.status == Members.CREATE, User.id==self.id)
    def get_participate_activities(self):
        return db.session.query(Members).join(User).filter(Members.status == Members.PATICIPATIED, User.id==self.id)
    def get_refused_activities(self):
        return db.session.query(Members).join(User).filter(Members.status == Members.REFUSED, User.id==self.id)
    def get_passed_activities(self):
        return db.session.query(Members).join(User).filter(Members.status == Members.PASSED, User.id==self.id)
    def get_id(self):
        return self.id
