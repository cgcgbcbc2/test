#! encoding=utf-8
from EasyMeeting.models import WeixinUser
import xml.etree.ElementTree as ET
import time
class WeixinRequest:
    def __init__(self, xmlString):
        self.__loaded = False
        if not xmlString:
            return
        #try:
        xml_recv = ET.fromstring(xmlString)
        self.__serverName = xml_recv.find("ToUserName").text  
        self.__user = xml_recv.find("FromUserName").text  
        self.__createTime = xml_recv.find("CreateTime").text
        self.__msgType = xml_recv.find("MsgType").text
        if self.__msgType == 'text':
            self.__content = xml_recv.find("Content").text
        elif self.__msgType == 'event':
            self.__event = xml_recv.find("Event").text
            if self.__event=="CLICK":
                self.__eventKey=xml_recv.find("EventKey").text
        WeixinUser.see(self.__user)
        self.__loaded = True
        #except:
        #    pass
    def vaild(self):
        return self.__loaded
    def getText(self):
        if self.__loaded and self.__msgType == "text":
            return self.__content.strip()
        else:
            raise TypeError
    def getEvent(self):
        if self.__loaded and self.__msgType == "event":
            return self.__event
        else:
            raise TypeError
    def getEventKey(self):
        if self.__loaded and self.__msgType == "event" and self.__event=="CLICK":
            return self.__eventKey
        else:
            raise TypeError
    
    def getType(self):
        return self.__msgType
    def getUser(self):
        return WeixinUser.query.filter_by(openid=self.__user).first_or_404()
    def getOpenid(self):
        return self.__user
    def getServerId(self):
        return self.__serverName
class WeixinReply:
    def __init__(self, request, replyType):
        if not replyType in ['text', 'news']:
            raise ValueError
        self.__type = replyType
        if not isinstance(request, WeixinRequest):
            raise TypeError
        self.__request = request
        if self.__type == 'news':
            self.__content = []
    def setText(self, text):
        if self.__type != 'text':
            raise TypeError
        self.__text = text
    def getText(self):
        return self.__text
    # item is a dict with key: title, description, picUrl, url
    def appendItem(self, item):
        if self.__type != 'news':
            raise TypeError
        self.__content.append(item)
    def generateXML(self, middlePart):
        reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType>"
        reply = reply % (self.__request.getOpenid(), self.__request.getServerId(), str(int(time.time())), self.__type )
        reply += middlePart
        reply += "</xml>"
        return reply

    def makeReply(self):
        if self.__type == 'text':
            reply = "<Content><![CDATA[%s]]></Content>" % (self.__text)
            return self.generateXML(reply)
        elif self.__type == 'news':
            if len(self.__content) == 0:
                raise ValueError
            reply = "<ArticleCount>%d</ArticleCount>" % (len(self.__content))
            reply += "<Articles>"
            for new in self.__content:
                fragment = "<item><Title><![CDATA[%s]]></Title><Description><![CDATA[%s]]></Description><PicUrl><![CDATA[%s]]></PicUrl><Url><![CDATA[%s]]></Url></item>"
                reply += (fragment % (new['title'], new['description'], new['picUrl'], new['url']))
            reply += "</Articles>"
            return self.generateXML(reply)
        raise TypeError
