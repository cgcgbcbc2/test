#coding=utf8  
from coverage import coverage
from flask_testing import TestCase
from EasyMeeting.foundation import db
import unittest
import time
import os
import io
import tempfile
import json
from manage import manager
import xml.etree.ElementTree as ET

cov = coverage(branch = True, omit = ['flask/*', 'tests.py'])
cov.start()

def createXML(openId, content):
    return '<xml><ToUserName><![CDATA[toUser]]></ToUserName><FromUserName><![CDATA['+openId+']]></FromUserName><CreateTime>'+str(int(time.time()))+'</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA['+content+']]></Content><MsgId>1</MsgId></xml>'

def createXMLButton(openId, event):
    return '<xml><ToUserName><![CDATA[toUser]]></ToUserName><FromUserName><![CDATA['+openId+']]></FromUserName><CreateTime>'+str(int(time.time()))+'</CreateTime><MsgType><![CDATA[event]]></MsgType><Event><![CDATA[CLICK]]></Event><EventKey><![CDATA['+event+']]></EventKey><Content><![CDATA[抢票]]></Content><MsgId>1</MsgId></xml>'

def parse_msg_xml(response):
    root_elem = ET.fromstring(response.data)
    msg = dict()
    if root_elem.tag == 'xml':
        for child in root_elem:
            msg[child.tag] = child.text
    return msg

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
    	#db.drop_all()
    	self.db_fd, manager.app.config['DATABASE'] = tempfile.mkstemp()
    	manager.app.config['TESTING'] = True
    	self.app = manager.app.test_client()
    	db.create_all()

    def tearDown(self):
    	db.drop_all()
    	os.close(self.db_fd)
    	os.unlink(manager.app.config['DATABASE'])  

    def login(self,openid):
        rv = self.app.post('/weixin/api', data=createXML(openid, '登录'), content_type='application/xml')
        key = (str(parse_msg_xml(rv)['Content'][4:]))
        data = json.dumps({'user_key': key})
        rv = self.app.post('/api/validate/login', data=data, content_type='application/json')
        return json.loads(rv.data.decode())

    def logout(self):
        rv = self.app.post('/api/validate/logout')
        return json.loads(rv.data.decode())

    def create_act(self):
    	self.login("123456789")
    	data = json.dumps({'title':'SellXiao111','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'SellXiao222','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'SellXiao333','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')

    def create_more_act(self):
    	self.login("123456789")
    	data = json.dumps({'title':'111','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'222','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'333','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'444','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'555','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'666','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'777','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'888','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'999','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'1010','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'1111','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'1212','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'1313','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'1414','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'1515','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'1616','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'1717','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	data = json.dumps({'title':'1818','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')

    def test_validate_login(self):
    	data  = json.dumps({'user_key':"1234596"})
    	rv = self.app.post('/api/validate/login',data=data,content_type='application/json')
    	assert 500 == (json.loads(rv.data.decode())['errorcode'])
    	res = self.login("123456789")
    	assert 1 == res['user_id']
    	res = self.logout()
    	assert 200 == res['errorcode']

    def test_getme(self):    	
    	rv = self.app.get('/api/userinfo/getme')    	
    	assert 0 == json.loads(rv.data.decode())['id']
    	self.login("123456789")  	
    	rv = self.app.get('/api/userinfo/getme')    	
    	assert 1 == json.loads(rv.data.decode())['id']

    def test_userinfo_avator_upload(self):
    	self.login("123456789")
    	filecontent = open('222.jpg','rb')
    	data = {}
    	data['image'] = (io.BytesIO(filecontent.read()),'test_avator.png')
    	rv = self.app.post('/api/userinfo/upload',data = data,content_type="multipart/form-data")
    	filecontent.close()
    	assert 200 == json.loads(rv.data.decode())['errorcode']

    def test_userinfo_modify_and_detail(self):
    	self.login("123456789")
    	data = json.dumps({'name':'VAN DARK HOLME','email':'MyShoudler@gym.com','mobile':'110','introduction':'Deep Dark Fantasy'})
    	rv = self.app.post('/api/userinfo/modify',data=data,content_type='application/json')
    	assert 200 == json.loads(rv.data.decode())['errorcode']
    	rv = self.app.get('/api/userinfo/detail?user_id=1')
    	assert "VAN DARK HOLME" == json.loads(rv.data.decode())['name']

    #def test_userinfo_detail_after_modify(self):    	
    #	rv = self.app.get('/api/userinfo/detail?user_id=1')
    #	assert "VAN DARK HOLME" == json.loads(rv.data.decode())['name']
    #	assert "MyShoudler@gym.com" == json.loads(rv.data.decode())['email']
    #	assert "110" == json.loads(rv.data.decode())['mobile']
    #	assert "Deep Dark Fantasy" == json.loads(rv.data.decode())['introduction']
    #	assert '/image/user/1.png' == json.loads(rv.data.decode())['avator']

    def test_validate_brutelogin_error(self):
    	self.login("123456789")
    	self.logout()
    	rv = self.app.get('/api/validate/brutelogin?user_id=0')
    	assert 500 == json.loads(rv.data.decode())['errorcode']

    def test_validate_brutelogin_sucess(self):
    	self.login("123456789")
    	self.logout()
    	rv = self.app.get('/api/validate/brutelogin?user_id=1')
    	assert 200 == json.loads(rv.data.decode())['errorcode']

    def test_activity_create(self):
    	self.login("123456789")
    	data = json.dumps({'title':'SellXiao','brief':'SX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/create',data=data,content_type='application/json')
    	assert 200 == json.loads(rv.data.decode())['errorcode']

    def test_activity_image_upload(self):
    	self.login("123456789")
    	filecontent = open('222.jpg','rb')
    	data = {}
    	data['image'] = (io.BytesIO(filecontent.read()),'test_picture.png')
    	rv = self.app.post('/api/activity/upload',data = data,content_type="multipart/form-data")
    	filecontent.close()
    	assert 200 == json.loads(rv.data.decode())['errorcode']

    def test_activity_modify_and_detail(self):
    	self.create_act()
    	data = json.dumps({'act_id':1,'title':'LuoChuiXiao','brief':'LCX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/modify',data=data,content_type='application/json')
    	assert 200 == json.loads(rv.data.decode())['errorcode'] 
    	rv = self.app.get('api/activity/detail?id=1',content_type='application/json')
    	assert 'LuoChuiXiao' == json.loads(rv.data.decode())['name']
    	assert 'LCX' == json.loads(rv.data.decode())['brief_desc']

    def test_activity_list_page(self):
    	self.create_more_act()
    	rv = self.app.get('/api/activity/list/pages?page=1')
    	assert [{'count':18,'page':1}] == json.loads(rv.data.decode())['page_info']
    	assert '888' == json.loads(rv.data.decode())['result_list'][0]['name']
    	assert '777' == json.loads(rv.data.decode())['result_list'][1]['name']
    	assert '666' == json.loads(rv.data.decode())['result_list'][2]['name']
    	assert '555' == json.loads(rv.data.decode())['result_list'][3]['name']

    def test_activity_list_created(self):
    	self.create_act()
    	rv = self.app.get('/api/activity/list/created?user_id=1')
    	assert 'SellXiao111' == json.loads(rv.data.decode())['result_list'][0]['name']
    	assert 'SellXiao222' == json.loads(rv.data.decode())['result_list'][1]['name']
    	assert 'SellXiao333' == json.loads(rv.data.decode())['result_list'][2]['name']

    def test_activity_operate_and_list_joined(self):
    	self.create_act()
    	self.logout()
    	self.login("6789")
    	data = json.dumps({'operate_mode':1,'activity_id':1,'user_id':2})
    	rv = self.app.post('/api/activity/operate',data=data,content_type='application/json')
    	assert 200 == json.loads(rv.data.decode())['errorcode']
    	data = json.dumps({'operate_mode':1,'activity_id':2,'user_id':2})
    	rv = self.app.post('/api/activity/operate',data=data,content_type='application/json')
    	assert 200 == json.loads(rv.data.decode())['errorcode']

    	rv = self.app.get('/api/activity/list/joined?user_id=2')
    	assert 'SellXiao111' == json.loads(rv.data.decode())['result_list'][0]['name']
    	assert 'SellXiao222' == json.loads(rv.data.decode())['result_list'][1]['name']

    	data = json.dumps({'operate_mode':3,'activity_id':1,'user_id':2})
    	rv = self.app.post('/api/activity/operate',data=data,content_type='application/json')
    	assert 200 == json.loads(rv.data.decode())['errorcode']

    	data = json.dumps({'operate_mode':2,'activity_id':2,'user_id':2})
    	rv = self.app.post('/api/activity/operate',data=data,content_type='application/json')
    	assert 200 == json.loads(rv.data.decode())['errorcode']

    	rv = self.app.get('/api/activity/list/joined?user_id=2')
    	assert 'SellXiao222' == json.loads(rv.data.decode())['result_list'][0]['name']

    def test_activity_list_new(self):
    	self.create_act()
    	rv = self.app.get('/api/activity/list/new')
    	assert 'SellXiao333' == json.loads(rv.data.decode())['result_list'][0]['name']
    	assert 'SellXiao222' == json.loads(rv.data.decode())['result_list'][1]['name']
    	assert 'SellXiao111' == json.loads(rv.data.decode())['result_list'][2]['name']

    def test_activity_list_refer(self):
    	self.create_act()
    	rv = self.app.get('/api/activity/list/refer')
    	assert json.loads(rv.data.decode())['result_list'][0]['name'] in ['SellXiao111','SellXiao222','SellXiao333']
    	assert json.loads(rv.data.decode())['result_list'][1]['name'] in ['SellXiao111','SellXiao222','SellXiao333']
    	assert json.loads(rv.data.decode())['result_list'][2]['name'] in ['SellXiao111','SellXiao222','SellXiao333']

    def test_activity_delete(self):
    	self.create_act()
    	data = json.dumps({'act_id':2})
    	rv = self.app.post('api/activity/delete',data=data,content_type='application/json')
    	assert 200 == json.loads(rv.data.decode())['errorcode']
    	data = json.dumps({'act_id':2,'title':'LuoChuiXiao','brief':'LCX','info':'SXtoLuo','startTime':'12345678','endTime':'12345678','members':100,'place':'412','host':'trj','contact':'110','type':'orz'})
    	rv = self.app.post('api/activity/modify',data=data,content_type='application/json')
    	assert 500 == json.loads(rv.data.decode())['errorcode']

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
    cov.stop()
    cov.save()
    print("\n\nCoverage Report:\n")
    cov.report()
    print("HTML version: " + os.path.join(basedir, "tmp/coverage/index.html"))
    cov.html_report(directory = 'tmp/coverage')
    cov.erase()