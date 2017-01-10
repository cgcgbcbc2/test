#! encoding=utf-8
from .util import NotMatch
from .request import WeixinReply
from EasyMeeting.common.identity import raw_url_add_identity

class BaseOpr(object):
    @classmethod
    def reply(cls, request, create_reply):
        cls.abort()
    @classmethod
    def _reply(cls, request):
        def create_reply(type_):
            return WeixinReply(request, type_)
        return cls.reply(request, create_reply)
    @classmethod
    def abort(cls):
        raise NotMatch()

class QueryOpr(BaseOpr):
    @classmethod
    def _reply(cls, request):
        def create_reply(reply):
            data = reply.getData()
            if reply.type == reply.TEXT:
                res = WeixinReply(request, "text")
                res.setText(data["content"])
                return res
            elif reply.type == reply.URL:
                res = WeixinReply(request, "text")
                url = data["url"]
                if data["login_required"]:
                    url = raw_url_add_identity(url, request.getOpenid())
                res.setText("<a href='%s'>%s</a>" % (url,data["hint"]))
                return res
            else:
                res = WeixinReply(request, "news")
                for item in data["items"]:
                    url = item["url"]
                    if item["login_required"]:
                        url = raw_url_add_identity(url, request.getOpenid())
                    elm = {"title":item["title"],
                            "picUrl":item["img"],
                            "url":url,
                            "description":item["desc"]}
                    res.appendItem(elm)
                return res
        return cls.reply(request, create_reply)


class TextOpr(BaseOpr):
    """
    Opr that receive user's TEXT input,
    reply with any type of message
    """
    @classmethod
    def _reply(cls, request):
        if request.getType() != 'text':
            cls.abort()

        def create_reply(type_):
            return WeixinReply(request, type_)
        return cls.reply(request, create_reply)
