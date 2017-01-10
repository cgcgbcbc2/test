#! encoding=utf-8
from flask import Blueprint, request, make_response, abort, render_template, g
import datetime
from EasyMeeting.foundation import CONST
import hashlib
from .weixin_util.request import WeixinRequest, WeixinReply
from .weixin_util import NotMatch
from EasyMeeting.models.LeftMessage import LeftMessage
from .weixin_op import ops
import logging

messages = Blueprint('messages', __name__, template_folder='template')
logger = logging.getLogger(__name__)

@messages.route('/create', methods = ['POST'])
def create():
	try:
		query = request.get_json()
		sender_id = query.get('sender_id')
		receiver_id = query.get('receiver_id')
		content = query.get('content')
		send_time = query.get('send_time')
		Message.newMessage(content,send_time,sender_id,receiver_id)
	except Exception,e:
		return json.dumps([{'errorcode':500}])
	return json.dumps([{'errorcode':200}])

@messages.route('/detail', ['message_id'], methods = ['GET'])
def detail(**args):
	try:
		message = Message.get_by_id(args['message_id'])
		message.read()
		result = [message.getdetail()]
		return json.dumps(result)
	except Exception,e:
		return json.dumps([{'errorcode':500}])
	return json.dumps([{'errorcode':200}])

@messages.route('/delete', ['message_id'], methods = ['POST'])
def delete(**args):
	try:
		message = Message.get_by_id(args['message_id'])
		message.delete()
	except Exception,e:
		return json.dumps([{'errorcode':500}])
	return json.dumps([{'errorcode':200}])

@messages.route('/list',['user_id'], methods = ['GET'])
def get_message_list(**args):
	try:
		message_list = Message.get_by_receiver_id(args['user_id'])
		result_list = []
		for i in message_list:
			if i.status < 2:
				result_list.append(i.getdetail())
		return json.dumps(result_list)
	except Exception,e:
		return json.dumps([{'errorcode':500}])
	return json.dumps([{'errorcode':200}])

