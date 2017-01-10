#! encoding=utf-8
from flask.ext.login import current_user
from EasyMeeting.foundation import db
from EasyMeeting.models.User import User,Members
import datetime
import random

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64),default = "")
    act_type = db.Column(db.Text,default = "")
    brief_desc = db.Column(db.Text,default = "")
    pic_url = db.Column(db.String(64),default="/image/activity/default.png")
    desc = db.Column(db.Text,default = "")
    start_time = db.Column(db.String(64))
    end_time = db.Column(db.String(64))
    loc = db.Column(db.Text,default = "")
    status = db.Column(db.Integer)
    host = db.Column(db.Text)
    contact = db.Column(db.Text)
    creator_id=db.Column(db.Integer)
    member_maxcount = db.Column(db.Integer,default=0)
    member_participatied_count = db.Column(db.Integer, default=0)
    member_passed_count = db.Column(db.Integer,default=0)
    member_denied_count = db.Column(db.Integer,default=0)
    WAIT,FINISH = range(2)
    NORMAL,FINISHED,DELETED = range(3)
    members = db.relationship('Members',backref="activity", lazy = "dynamic")
    def __init__(self,**args):
        for k,v in args.items():
            setattr(self,k,v)
    @staticmethod
    def get_current_activity_by_name(name):
        return Activity.query.filter_by(status = Activity.NORMAL).filter_by(name = name).first()
    def has_user(self,user):
        if not user.is_authenticated():
            return False
        return self.get_member(user.id)
    def get_participate_member(self):
        result=[]
        for i in self.members.filter_by(status = Members.PATICIPATIED):
            result.append({
                'UID':i.user_id,
                'UName':i.user.name,
                'UAvator':i.user.avator
                })
        return result
    def get_refuse_member(self):
        result=[]
        for i in self.members.filter_by(status = Members.REFUSED):
            result.append({
                'UID':i.user_id,
                'UName':i.user.name,
                'UAvator':i.user.avator
                })
        return result
    def get_passed_member(self):
        result=[]
        for i in self.members.filter_by(status = Members.PASSED):
            result.append({
                'UID':i.user_id,
                'UName':i.user.name,
                'UAvator':i.user.avator
                })
        return result
    def get_member(self,id):
        return self.members.filter_by(user_id = id).first()
    @staticmethod
    def get_act_num():
        return Activity.query.count()
    @staticmethod
    def search_by_name(searchname):
        return Activity.query.filter(Activity.name.contains(searchname))
    def create(self,user):
        member = self.get_member(user.id)
        if not member:
            member = Members(activity_id = self.id,user_id = user.id,status = Members.CREATED)
            db.session.add(member)
            db.session.commit()     
    def participate(self,user):
        member = self.get_member(user.id)
        if not member:
            member = Members(activity_id = self.id,user_id = user.id,status = Members.PATICIPATIED)
            self.member_participatied_count += 1
            db.session.add(member)
            db.session.commit()
    def refuse(self,user):
        member = self.get_member(user.id)
        if member.status == Members.PATICIPATIED:
            member.status=Members.REFUSED
            self.member_denied_count += 1
            self.member_participatied_count -= 1
            db.session.commit()
    def passed(self,user):
        member = self.get_member(user.id)
        if member.status == Members.PATICIPATIED:
            member.status=Members.PASSED
            self.member_passed_count += 1
            self.member_participatied_count -= 1
            db.session.commit()
    def getdetail(self):
        details = {}
        details['name'] = self.name
        details['brief_desc'] = self.brief_desc
        details['desc'] = self.desc
        details['start_time'] = self.start_time
        details['end_time'] = self.end_time
        details['member_maxcount'] = self.member_maxcount
        details['member_passed_count'] = self.member_passed_count
        details['member_denied_count'] = self.member_denied_count
        details['member_participatied_count'] = self.member_participatied_count
        details['type'] = self.act_type
        details['image'] = self.pic_url
        details['loc'] = self.loc
        details['host'] = self.host
        details['contact'] = self.contact
        u = User.get_by_id(self.creator_id)
        details['uName']=u.name
        details['uAvator']=u.avator
        details['uID']=self.creator_id
        details['ID']=self.id
        details['member_passed'] = self.get_passed_member()
        details['member_denied'] = self.get_refuse_member()
        details['member_participatied'] = self.get_participate_member()
        return details
    def modify(self,query):
        self.name = query.get('title')
        self.brief_desc = query.get('brief')
        self.desc = query.get('info')
        self.start_time = query.get('startTime')
        self.end_time = query.get('endTime')
        self.member_maxcount = query.get('members')
        self.loc = query.get('place')
        self.host = query.get('host')
        self.act_type = query.get('type')
        self.pic_url = query.get('image')
        db.session.commit()
    @staticmethod
    def get_by_id(id):
        return Activity.query.filter_by(id = id).first()
    @staticmethod
    def get_by_creator_id(id):
        return Activity.query.filter_by(creator_id = id)
    @staticmethod
    def get_by_joiner_id(id):
        return Activity.query.filter_by()
    @staticmethod
    def newActivity(query):
        name = query.get('title','')
        old_activity = Activity.query.filter_by(name = name).first()
        if not old_activity:
            act = Activity(
                name = name,
                brief_desc = query.get('brief',''),
                desc = query.get('info',''),
                start_time = str(query.get('startTime','')),
                end_time = str(query.get('endTime','')),
                member_maxcount = query.get('members'),
                loc = query.get('place'),
                host = query.get('host'),
                contact = query.get('contact'),
                act_type = query.get('type'),
                creator_id = current_user.id,
                pic_url = query.get('image'),
            )
            db.session.add(act)
            db.session.commit()
            mem = Members(activity_id=act.id,user_id=current_user.id,status=Members.CREATE)
            db.session.add(mem)
            db.session.commit()
            return act
        return old_activity
    @staticmethod
    def get_random(n):
        result_list = []
        act_num = Activity.get_act_num()
        ran_list = range(1,act_num+1)
        ran_list2 = []
        for i in ran_list:
            ran_list2.append(i)
        random.seed()
        random.shuffle(ran_list2)
        if (act_num <= n):
            for i in range(act_num):
                act = Activity.get_by_id(ran_list2[i])
                result_list.append(act.getdetail())
        else:
            for i in range(n):
                act = Activity.get_by_id(ran_list2[i])
                result_list.append(act.getdetail())
        return result_list
    @staticmethod
    def deleteActivity(did):
        for i in Members.query.all():
            db.session.delete(i)
        act = Activity.get_by_id(did)
        db.session.delete(act)
        db.session.commit()