#!/usr/bin/env python
#! -*- encoding=utf-8
from itsdangerous import URLSafeTimedSerializer, BadData, SignatureExpired
from flask import request, current_app
from EasyMeeting.common.url import change_get_args

'''
File: identity.py
Author: Xu Xinran <xxr3376@gmail.com>
Description: provide functions that generate URL with identity \
        and validate identity from URL
'''

WEIXIN_IDENTITY_KEY= '_ts_wid'
URL_SECRET = 'iam thuskate developer'
EXPIRE_TIME = 720 #in second'
SALT = 'we really love skate'

signer = None
def get_signer():
    global signer
    if signer is None:
        signer = URLSafeTimedSerializer(URL_SECRET, salt=SALT)
    return signer

def gen_identity(id_):
    # TODO should AES encrypt id_
    signer = get_signer()
    return signer.dumps(id_)

class BadIdentity(Exception):
    pass
class IdentityExpired(BadIdentity):
    pass

def load_identity():
    signed = request.args.get(WEIXIN_IDENTITY_KEY, None)
    if signed is None:
        return None
    signer = get_signer()
    expire = EXPIRE_TIME
    if current_app.config['DEBUG']:
        expire = 1e8
    try:
        return signer.loads(signed, max_age=expire)
    except SignatureExpired:
        raise IdentityExpired()
    except BadData:
        raise BadIdentity()

def raw_url_add_identity(url, id_):
    """
        url: a absolute URL
        id_: a ASCII string that represent a identity (in fact support any JSONable date)
    """
    def callback(query_dict):
        query_dict.update({WEIXIN_IDENTITY_KEY: gen_identity(id_)})
        return query_dict
    return change_get_args(url, callback)
