#! encoding=utf-8
from EasyMeeting.foundation import db
from datetime import datetime
from EasyMeeting.models.User import User
from flask import g
from flask.ext.login import login_user

NORMAL = 0
ADMIN = 1
BAN = 2

class WeixinUser(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    openid = db.Column(db.String(64), unique = True)
    nickname = db.Column(db.Text)
    describe = db.Column(db.Text)
    lastseen = db.Column(db.DateTime)
    mode = db.Column(db.Integer)
    user = db.relationship("User",backref="weixinUser",uselist = False)
    def __repr__(self):
        return '<Weixin %r - %r>' % (self.nickname, self.openid)

    @staticmethod
    def see(openid):
        if not openid:
            return None
        wuser = WeixinUser.query.filter_by(openid=openid).first()
        now = datetime.now()
        if wuser:
            wuser.lastseen = now
        else:
            wuser = WeixinUser(openid=openid, lastseen=now, mode = NORMAL)
            db.session.add(wuser)
        db.session.commit()
        if not wuser.user:
            user = User(weixin_id = wuser.id,
                    username = "wuser%d" % (wuser.id),
                    name = u"游客",
                    status = User.OTHERS,
                    is_admin = False)
            db.session.add(user)
            db.session.commit()
        login_user(wuser.user)
        return wuser.user

    def setNickname(self, nickname):
        user_has_samename = WeixinUser.query.filter_by(nickname=nickname).first()
        if not user_has_samename or user_has_samename.id is self.id:
            self.nickname = nickname
            return True
        else:
            return False
    def hasNickname(self):
        if self.nickname:
            return True
        else:
            g.user_state = 'no_nickname'
            return False
    def isAdmin(self):
        if self.mode & ADMIN == ADMIN:
            return True
        return False
    def isBan(self):
        if self.mode & BAN == BAN:
            return True
        return False
