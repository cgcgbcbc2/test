#! encoding=utf-8

from EasyMeeting.models import Group,Config
from EasyMeeting.models.User import User
from EasyMeeting.foundation import db
import random

def variance(vals):
    s = sum(vals)
    if s == 0:
        return 0,999
    count = len(vals)
    avg = s / float(count)
    vs = 0
    for v in vals:
        vs += (v-avg)*(v-avg)
    mv = max(vals)
    vari = vs/mv/mv
    return avg,vari

def obj_func(users,groups):
    groups = filter(lambda x:x.basis == False,groups)
    res = {"bg":{},"major_count":{},"member_count":{},"basis":{}}
    for g in groups:
        us = filter(lambda u:u.group_id == g.id,users)
        boys = filter(lambda u:u.sex == User.MALE, us)
        girls = filter(lambda u:u.sex == User.FEMALE, us)
        g.bg = res["bg"][g.id] = float(len(boys)+0.01)/float(len(girls)+0.01)
        g.bgs = "%d/%d" % (len(boys),len(girls))
        majors = {}
        for u in us:
            majors[u.major] = 0
        g.major_count = res["major_count"][g.id] = len(majors)
        res["member_count"][g.id] = g.member_count = len(us)
        basis_count = len(filter(lambda u:u.basis == 1,us))
        res["basis"][g.id] = basis_count / float(g.member_count - basis_count + 0.01)
        g.basis_str = "%d/%d" % (basis_count,g.member_count - basis_count)
        
    for key,item in res.items():
        norm = []
        avg,vari = variance(item.values())
        res["%s_avg" % (key)] = avg
        res["%s_vari" % (key)] = vari
    res["choices"] = {}
    for u in users:
        res["choices"][u.id] = u.group_id
    bg = float(Config.get("arg_bg",1))
    count = float(Config.get("arg_member_count",1))
    major = float(Config.get("arg_major_count",1))
    basis = float(Config.get("arg_basis",1))
    res["score"] = bg*res["bg_vari"] + count * res["member_count_vari"] + major * res["major_count_vari"] + basis*res["basis_vari"]
    return res

def group_alg(users,groups, trys = 30, initial = None):
    if (len(groups)<1):
        return {"remain":len(users)}
    best = {"score":1e20,"res":{}}
    if initial:
        best["res"] = initial
        best["score"] = initial["score"]
    res = {}
    orig = {}
    for g in groups:
        orig[g.id] = g.member_count
    for i in range(trys):
        for g in groups:
            g.member_count = orig[g.id]
        remain = random_groups(users,groups)
        res = obj_func(users,groups)
        if res["score"]<best["score"]:
            best["score"] = res["score"]
            best["res"] = res
    res = best["res"]
    for u in users:
        u.group_id = res["choices"][u.id]
    for g in groups:
        g.member_count = res["member_count"].get(g.id,0)
    res["remain"] = remain
    return res

def random_groups(users,groups):
    random.seed()
    all_groups = groups
    gs = {}
    cur_mins = {}
    for b in [0,1]:
        groups = filter(lambda g:g.basis == b,all_groups)
        if (len(groups) == 0):
            continue
        key = "%d356" % (b)
        gs[key] = groups
        cur_mins[key] = min(map(lambda g:g.member_count,gs[key]))
        for i in ["3","5","6"]:
            key = "%d%s" % (b,i)
            gs[key] = filter(lambda g:g.prefer_time.find(str(i))>-1,groups)
            if len(gs[key])>0:
                cur_mins[key] = min(map(lambda g:g.member_count,gs[key]))
        for s in ["35","36","56"]:
            key = "%d%s" % (b,s)
            gs[key] = filter(lambda g:g.prefer_time.find(s[0])>-1 or g.prefer_time.find(s[1])>-1, groups)
            if len(gs[key])>0:
                cur_mins[key] = min(map(lambda g:g.member_count,gs[key]))
    remain = 0
    random.shuffle(users)
    count = 0
    for user in users:
        count += 1
        utime = "%d%d" % (user.basis,user.prefer_time)
        if not utime in cur_mins:
            remain += 1
            continue
        mins = filter(lambda g:g.member_count == cur_mins[utime],gs[utime])
        while len(mins)<1:
            cur_mins[utime] += 1
            mins = filter(lambda g:g.member_count == cur_mins[utime], gs[utime])
        g = random.choice(mins)
        g.member_count +=1
        user.group_id = g.id
    return remain

def groups_init():
    sem = User.current_semester()
    groups = Group.current_groups()
    users = User.query.filter_by(status = User.NEW_PAID).filter_by(semester = sem).filter_by(group_id = None).all()
    res = group_alg(users,groups)
    db.session.commit()
    return res

def groups_reinit(replay = False):
    sem = User.current_semester()
    groups = Group.current_groups()
    users = User.query.filter_by(status = User.NEW_PAID).filter_by(semester = sem).all()
    initial = None
    if not replay:
        initial = obj_func(users,groups)
    for u in users:
        u.group_id = None
    for g in groups:
        g.member_count = 0
    res = group_alg(users,groups,initial = initial)
    db.session.commit()
    return res

