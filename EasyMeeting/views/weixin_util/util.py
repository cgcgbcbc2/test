#! encoding=utf-8
class NotMatch(Exception):
    pass

def abort():
    raise NotMatch()

