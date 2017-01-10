#! encoding=utf-8
from EasyMeeting.views.weixin_util import BaseOpr
from EasyMeeting.models import WeixinUser, LoginKey
from EasyMeeting.foundation import db
from datetime import datetime
from datetime import timedelta
from random import Random
from config import DOMAIN

class Login(BaseOpr):
    @classmethod
    def reply(cls, request, create_reply):
        try:
            if (request.getType()=='text' and request.getText() == "登录") or(request.getEvent()=='CLICK' and request.getEventKey()=="Login"):
                
                user = WeixinUser.see(request.getOpenid())
                str = ''
                randomLength = 6
                chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
                length = len(chars) - 1
                random = Random()
                while True :
                    for i in range(randomLength):
                        str += chars[random.randint(0, length)]
                    if not LoginKey.alreadyUsed(str):
                        key = LoginKey(key=str, user_id=user.id, endTime=(datetime.now() + timedelta(hours=10)))
                        db.session.add(key)
                        db.session.commit()
                        reply=create_reply("text")
                        reply.setText('登录秘钥'+str)
                        return reply
            else:
                cls.abort()
        except:
            cls.abort()
class UserIndex(BaseOpr):
    @classmethod
    def reply(cls, request, create_reply):
        try:
            print(request.getType() == 'text' and request.getText() == "个人主页")
            if (request.getType() == 'text' and request.getText() == "个人主页") or (request.getEvent() == 'CLICK' and request.getEventKey() == "User"):
                user = WeixinUser.see(request.getOpenid())
                reply=create_reply("text")
                reply.setText("<a href='%s'>%s</a>" % (DOMAIN+'/index/#!/wechat/check/'+str(user.id)+'/HOMEPAGE','个人主页'))
                return reply
            else:
                cls.abort()
        except:
            cls.abort()

