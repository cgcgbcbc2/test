CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = ''
SQLALCHEMY_POOL_RECYCLE = 10
#SERVER_NAME = ""
try:
    # SAE
    from mysql import MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
    SQLALCHEMY_POOL_RECYCLE = 10
    #SERVER_NAME = "thuskatemp.sinaapp.com"
except:
    #MYSQL_USER = 'root'
    #MYSQL_PASS = ''
    #MYSQL_HOST = '127.0.0.1'
    #MYSQL_PORT = '3306'
    #MYSQL_DB = 'thuskatemp'
    #SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    #SERVER_NAME = "127.0.0.1:5000"

DOMAIN = "http://183.172.177.33"

PASSWORD_SECRET = 'UGUGUGUGUDUFU'

current_semester = 20152
