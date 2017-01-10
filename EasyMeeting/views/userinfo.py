#! encoding=utf-8
from flask import Blueprint, request, make_response, abort, render_template, g
import datetime
from EasyMeeting.foundation import CONST
import hashlib
from .weixin_util.request import WeixinRequest, WeixinReply
from .weixin_util import NotMatch
from .weixin_op import ops
from EasyMeeting.models.User import User
import json
import logging
import json
import os
import io
from flask.ext.login import current_user
from EasyMeeting.foundation import db
from EasyMeeting.models import User
from werkzeug.utils import secure_filename

userinfo = Blueprint('userinfo', __name__, template_folder='../frontend')
logger = logging.getLogger(__name__)

@userinfo.route('/modify', methods = ['POST'])
def modify():
    #try:
    user = User.get_by_id(current_user.id)
    query = request.get_json()
    user.modify(query)
    #except:
        #return json.dumps({'errorcode':500})
    return json.dumps({'errorcode':200})

@userinfo.route('/upload', methods = ['POST'])
def upload():
    f = request.files['image']
    f.filename = secure_filename(str(current_user.id) + '.png')
    f.save(os.path.join('EasyMeeting', 'frontend', 'image', 'user', f.filename))
    user = User.get_by_id(current_user.id)
    user.avator = '/image/user/' + str(current_user.id) + '.png'
    db.session.commit()
    return json.dumps({'errorcode':200})

@userinfo.route('/detail', methods = ['GET'])
def detail():
    #try:
    user_id = request.args.get('user_id')
    user = User.get_by_id(user_id)
    result = user.getdetail()
    return json.dumps(result)
    #except:
    #return json.dumps({'errorcode':500})
@userinfo.route('/getme', methods = ['GET'])
def getme():
    try:
        result = {'id':current_user.id, 'avator': current_user.avator, 'intro': current_user.intro, 'username': current_user.name}
        return json.dumps(result)
    except:
        return json.dumps({'id':0})
