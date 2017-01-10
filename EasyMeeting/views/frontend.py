#! encoding=utf-8
from flask import Blueprint, request, make_response, abort, render_template, g
import datetime
from EasyMeeting.foundation import CONST
import hashlib
from .weixin_util.request import WeixinRequest, WeixinReply
from .weixin_util import NotMatch
from .weixin_op import ops
import logging

frontend = Blueprint('frontend', __name__, template_folder='../frontend')

@frontend.route('/')
def test():
	print("test")
@frontend.route('/index')
def index():
    return render_template("dist/index.html")