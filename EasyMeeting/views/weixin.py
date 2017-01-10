#! encoding=utf-8
from flask import Blueprint, request, make_response, abort, render_template, g
import datetime
from EasyMeeting.foundation import CONST
import hashlib
from .weixin_util.request import WeixinRequest, WeixinReply
from .weixin_util import NotMatch
from .weixin_op import ops
import logging

weixin = Blueprint('weixin', __name__, template_folder='template')
logger = logging.getLogger(__name__)

@weixin.route('/api', methods = ['GET', 'POST'])
def api():
    if request.method == 'GET':
        token = CONST['token']
        query = request.args  # GET 参数
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        if ( hashlib.sha1(s.encode('utf-8')).hexdigest() == signature ):
            return make_response(echostr)
        abort(500)
    else:
        rq = WeixinRequest(request.data)
        if rq.vaild():
            reply = dispatch(rq, ops)
            return make_response(reply.makeReply().encode('utf-8'))

        abort(500)

def dispatch(request, ops):
    try:
        for op in ops:
            try:
                result = op._reply(request)
                if not isinstance(result, WeixinReply):
                    abort(500)
                return result
            except NotMatch:
                pass
        abort(403)
    except:
        logger.exception('unknown')
        abort(403)
