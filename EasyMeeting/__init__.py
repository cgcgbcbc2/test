#! encoding=utf-8
from flask import Flask, g, render_template, request, redirect, abort
from EasyMeeting.foundation import db, login_manager
from EasyMeeting.models import WeixinUser
from EasyMeeting.models.User import User
from flask.ext.login import current_user, login_user
from datetime import datetime
from EasyMeeting import views
#from EasyMeeting import app

import logging
from EasyMeeting.common.identity import load_identity, BadIdentity, IdentityExpired, WEIXIN_IDENTITY_KEY
from EasyMeeting.common.url import change_get_args

import pymysql
pymysql.install_as_MySQLdb()

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console)

DEFAULT_APP_NAME = 'EasyMeeting'

DEFAULT_MODULES = [
    views.weixin,
    views.validate,
    views.index,
    views.frontend,
    views.activity,
    views.userinfo
]
DEBUG_MODULES = [
]

def create_app(debug = False):
    app = Flask(DEFAULT_APP_NAME)
    app.debug = debug
    app.config.from_object('config')
    configure_foundations(app)
    configure_blueprint(app, DEFAULT_MODULES,DEBUG_MODULES)
    configure_template_filter(app)
    return app

def configure_foundations(app):
    db.app = app
    db.init_app(app)
    @app.after_request
    def releaseDB(response):
        db.session.close()
        return response
    login_manager.init_app(app)
    login_manager.login_view = 'index.indexhtml'
    @login_manager.user_loader
    def load_user(id):
        try:
            return User.query.get(int(id))
        except Exception:
            return None
    @app.before_request
    def before_request():
        g.user = current_user
        if request.method == 'GET':
            # authrized by IDENTITY_KEY only when GET method
            try:
                wid = load_identity()
                if wid:
                    if not g.user.is_authenticated():
                        WeixinUser.see(wid)
                    def callback(query_dict):
                        query_dict.pop(WEIXIN_IDENTITY_KEY)
                        return query_dict
                    new_url = change_get_args(request.url, callback)
                    return redirect(new_url)
            except IdentityExpired:
                # TODO redirect to some page... or regenerate a new url
                pass
            except BadIdentity:
                abort(403)
        if g.user.is_authenticated():
            g.user.last_seen = datetime.utcnow()
            db.session.add(g.user)
            db.session.commit()

    errors = [404, 403, 500]
    for errorcode in errors:
        @app.errorhandler(errorcode)
        def not_found(error):
            return 
            #return render_template("mobile/error.html", error = error), errorcode
    
def configure_blueprint(app, modules, debug_modules):
    for module in modules:
        if module.name == "weixin" or module.name == 'index':
            app.register_blueprint(module,url_prefix="/%s" % (module.name))
        else:
            app.register_blueprint(module,url_prefix="/api/%s" % (module.name))
    if app.debug:
        for module in debug_modules:
            app.register_blueprint(module,url_prefix="/api/%s" % (module.name))
def configure_template_filter(app):
    from datetime import date
    @app.template_filter('dateint')
    def _jinja2_filter_dateint(dateint):
        return date.fromordinal(dateint).strftime('%Y-%m-%d')
    @app.template_filter('sexint')
    def _jinja2_filter_sexint(sexint):
        vals = {1:u"男",2:u"女"}
        return vals.get(sexint,"")
    @app.template_filter('replyint')
    def _jinja2_filter_replyint(ri):
        vals = {1:u"文本消息",2:u"链接消息",3:u"图文消息"}
        return vals.get(ri,"Unknown")
    @app.template_filter('semint')
    def _jinja2_filter_semint(sem):
        year = sem / 10
        s = [u"秋季学期",u"春季学期"]
        return u"%d年%s" % (year,s[sem%2])
    @app.template_filter('weekday')
    def _jinja2_filter_weekday(d):
        vals = {"3":u"周三", "5":u"周五", "6":u"周六"}
        s = str(d)
        for k,v in vals.items():
            s = s.replace(k,v)
        return s
    @app.template_filter("userstatus")
    def _jinja2_filter_userstatus(status):
        return User.STATUS_NAMES[status]
