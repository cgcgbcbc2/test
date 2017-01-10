#! encoding=utf-8
from EasyMeeting.foundation import db
from EasyMeeting.models.User import User
from datetime import datetime


class LoginKey(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    key = db.Column(db.String(64), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    endTime = db.Column(db.DateTime)

    def __repr__(self):
        return '<LoginKey %r>' % (self.key)

    @staticmethod
    def alreadyUsed(str):
        if not str:
            return True
        used = False
        for i in LoginKey.query.filter_by(key=str).all():
            if i.endTime < datetime.now():
                db.session.delete(i)
            else:
                used = True
        db.session.commit()
        return used

    @staticmethod
    def validate(str):
        for i in LoginKey.query.filter_by(key=str).all():
            if i.endTime < datetime.now():
                db.session.delete(i)
                print(i)
            else:
                db.session.commit()
                return i.user_id
        db.session.commit()
        return None