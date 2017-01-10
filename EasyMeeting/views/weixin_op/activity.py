#! encoding=utf-8
from EasyMeeting.views.weixin_util import BaseOpr
from EasyMeeting.models import WeixinUser
from flask import url_for
from config import DOMAIN
class CreateActivity(BaseOpr):
    @classmethod
    def reply(cls, request, create_reply):
        try:
            if (request.getType() == 'text' and request.getText() == "创建活动") or (request.getEvent() == 'CLICK' and request.getEventKey() == "CREATE_ACTIVITY"):
                user = WeixinUser.see(request.getOpenid())
                reply = create_reply("news")
                createUrl  = DOMAIN+'/index/#!/wechat/check/'+str(user.id)+'/CREATEACT'
                picUrl = DOMAIN + "/static\\img\\banner.ed835a8.png"
                print(picUrl)
                reply.appendItem({"title":u"创建活动",
                    "picUrl":picUrl,
                    "url":createUrl,
                    "description":""})
                return reply
            else:
                cls.abort()
        except:
            cls.abort()

class ListAct(BaseOpr):
    @classmethod
    def reply(cls, request, create_reply):
        try:
            if (request.getType() == 'text' and request.getText() == "活动列表") or (
                    request.getEvent() == 'CLICK' and request.getEventKey() == "LIST_ACTIVITY"):
                user = WeixinUser.see(request.getOpenid())
                reply=create_reply("text")
                reply.setText("<a href='%s'>%s</a>" % (DOMAIN+'/index/#!/wechat/check/'+str(user.id)+'/LISTACT','活动列表'))
                return reply
            else:
                cls.abort()
        except:
            cls.abort()
