from flask.ext.script import Server, Shell, Manager, prompt_bool
from EasyMeeting import create_app
from EasyMeeting.foundation import db
from EasyMeeting.models import User, WeixinUser
manager = Manager(create_app(debug = True))

manager.add_command("runserver", Server('0.0.0.0',port=8080))

def _make_context():
    return dict(db=db)
manager.add_command("shell", Shell(make_context=_make_context))

def _addUser(username, password, is_admin, status):
    user = User(username=username, password=password, is_admin = is_admin, status = status)
    db.session.add(user)
    db.session.commit()

@manager.command
def createall():
    "Creates database tables"
    db.create_all()

@manager.command
def dropall():
    "Drops all database tables"
    if prompt_bool("Are you sure ? You will lose all your data !"):
        db.drop_all()

if __name__ == "__main__":
    manager.run()

