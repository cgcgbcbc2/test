#! encoding=utf-8
from flask import Blueprint, request, make_response, abort, render_template, g
import datetime
import time
import os
from EasyMeeting.foundation import CONST
import hashlib
from .weixin_util.request import WeixinRequest, WeixinReply
from .weixin_util import NotMatch
from .weixin_op import ops
from EasyMeeting.models.activity import Activity
from EasyMeeting.models.User import User,Members
from flask.ext.login import current_user
from werkzeug.utils import secure_filename

import logging
import json

activity = Blueprint('activity', __name__, template_folder='../frontend')
logger = logging.getLogger(__name__)

@activity.route('/upload', methods = ['POST'])
def upload():
    f = request.files['image']
    query = request.get_json()
    currtime = time.mktime(datetime.datetime.now().timetuple())
    f.filename = secure_filename(str(currtime) + '.png')
    filePath = os.path.join('EasyMeeting', 'frontend', 'image', 'activity', f.filename)
    f.save(filePath)
    return json.dumps({"errorcode":200, 'pic_url': '/image/activity/' + f.filename})

@activity.route('/create', methods = ['POST'])
def create():
	try:
		query = request.get_json()
		newact = Activity.newActivity(query)
	except:
		return json.dumps({'errorcode':500})
	return json.dumps({'errorcode':200})

@activity.route('/modify', methods = ['POST'])
def modify():
	try:
		query = request.get_json()
		act_id = query.get('act_id')
		act = Activity.get_by_id(act_id)
		act.modify(query)
	except:
		return json.dumps({'errorcode':500})
	return json.dumps({'errorcode':200})


@activity.route('/delete', methods = ['POST'])
def delete():
	try:
		query = request.get_json()
		act_id = query.get('act_id')
		act = Activity.get_by_id(act_id)
		Activity.deleteActivity(act_id)
	except:
		return json.dumps({'errorcode':500})
	return json.dumps({'errorcode':200})

@activity.route('/detail', methods = ['GET'])
def detail():
	#try:
	act = Activity.get_by_id(request.args.get('id'))
	if not act:
		return json.dumps({'errorcode':500})		
	result = act.getdetail()
	return json.dumps(result)		

@activity.route('/list/pages', methods = ['GET'])
def get_list_by_page():
	pagenumber = request.args.get('page')
	if pagenumber == None:
		pagenumber = 0
	pagenumber=int(pagenumber)
	act_num = Activity.get_act_num()
	result_list = []
	for i in range(pagenumber*10+1,pagenumber*10+11):
		if (act_num-i>=0):
			act = Activity.get_by_id(act_num-i+1)
		else:
			break
		if (act!=None):
			result_list.append(act.getdetail())
	page_info = []
	page_info.append({'count':Activity.get_act_num(),'page':pagenumber})
	return json.dumps({'result_list':result_list,'page_info':page_info})		

@activity.route('/list/refer', methods = ['GET'])
def get_list_refer():
	try:
		result_list = [] 
		result_list = Activity.get_random(5)
		return json.dumps({'result_list':result_list})				
	except:
		return json.dumps({'errorcode':500})

@activity.route('/list/new', methods = ['GET'])
def get_list_new():
	act_num = Activity.get_act_num()
	result_list = []
	if act_num <= 5:
		act_num1 = 1
	else:
		act_num1 = act_num-4
	for i in range(act_num1,act_num+1):
		act = Activity.get_by_id(act_num+act_num1-i)
		if (act!=None):
			result_list.append(act.getdetail())
	return json.dumps({'result_list':result_list})

@activity.route('/list/created', methods = ['GET'])
def get_created_list():
	act_list = Activity.get_by_creator_id(int(request.args.get('user_id')))
	result_list = []
	num = 0
	for i in act_list:
		result_list.append(i.getdetail())
		num = num + 1
		if (num == 5):
			break
	return json.dumps({'result_list':result_list})

@activity.route('/list/joined', methods = ['GET'])
def get_joined_list():
	joiner = User.get_by_id(int(request.args.get('user_id')))
	act_list = joiner.get_activities()
	result_list = []
	num = 0
	for i in act_list:
		if i.status == Members.PATICIPATIED or i.status==Members.PASSED:
			result_list.append(Activity.get_by_id(i.activity_id).getdetail())
			num = num + 1
			if (num == 5):
				break
	return json.dumps({'result_list':result_list})

@activity.route('/operate',methods = ['POST'])
def operate():
	query = request.get_json()
	activity_id = query.get('activity_id')
	user_id = query.get('user_id')
	print(user_id)
	user = User.get_by_id(user_id)
	activity = Activity.get_by_id(activity_id)
	operate_mode = query.get('operate_mode')
	if (operate_mode == 1):
		activity.participate(user)
	if (operate_mode == 2):
		activity.passed(user)
	if (operate_mode == 3):
		activity.refuse(user)
	return json.dumps({'errorcode':200})

@activity.route('/search',methods = ['GET'])
def search():
	try:
		search_text = request.args.get('text')
		if (search_text != None):
			activitylist = Activity.search_by_name(search_text)
		resultlist = []
		num = 0
		for i in activitylist:
			resultlist.append(i.getdetail())
			num = num + 1
			if (num == 10):
				break
		return json.dumps({'num':num,'activitylist':resultlist})
	except:
		return json.dumps({'errorcode':500})
