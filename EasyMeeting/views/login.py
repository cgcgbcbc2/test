#! encoding=utf-8
from flask import Blueprint, request, make_response, abort, render_template, g
import datetime
from EasyMeeting.foundation import CONST
import hashlib
from .weixin_util.request import WeixinRequest, WeixinReply
from .weixin_util import NotMatch
from .weixin_op import ops
import logging
from EasyMeeting.models.loginKey import LoginKey
from EasyMeeting.models.User import User
import json


from flask.ext.login import current_user, login_user, logout_user, login_required


validate = Blueprint('validate', __name__, template_folder='template')
logger = logging.getLogger(__name__)

@validate.route('/brutelogin', methods = ['GET'])
def brute_login():
	try:
		if request.method == 'GET':
			user_id = request.args.get('user_id')
			login_user(User.get_by_id(user_id))
			return json.dumps({'errorcode':200})
	except:
		return json.dumps({'errorcode':500})


@validate.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		query = request.get_json()
		user_key = query.get('user_key')
		user_id = LoginKey.validate(user_key) 
		if user_id == None:
			return json.dumps({'errorcode':500})
		else:
			login_user(User.get_by_id(user_id))
			return json.dumps({'user_id':user_id})

@validate.route('/logout', methods = ['POST'])
@login_required
def logout():
	logout_user()
	return json.dumps({'errorcode':200})



