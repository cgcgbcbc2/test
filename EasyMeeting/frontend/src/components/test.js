export const test_user_info = {
  'nickname': 'Anonymous',
  'openid': 1,
  'mail': 'anonymous@easymeeting.com',
  'phone': 12345678900,
  'userinfo': 'This is a brief Info',
  'activityCreated': [{
    'id': 1,
    'title': '这个用户创建的第一个活动',
    'time': '2016-12-8',
    'place': 'ZJ1#412',
    'num': 4,
    'brief': '只是测试用的活动'
  }, {
    'id': 2,
    'title': '然后他又创建了一个',
    'time': '2016-12-8',
    'place': 'ZJ1#412',
    'num': 4,
    'brief': '还是测试用的，看看变成2个会不会出bug'
  }],
  'activityParticipate': [{
    'id': 3,
    'title': '这个用户参加了一个活动',
    'time': '2016-12-7',
    'place': 'ZJ1#412',
    'num': 100,
    'brief': '写代码'
  }]
}

export const test_activity_detail = {
  'id': 1,
  'isAuthor': true,
  'title': '这个用户创建的第一个活动',
  'time': '2016-12-8',
  'place': 'ZJ1#412',
  'num': 4,
  'passed': 3,
  'brief': '只是测试用的活动',
  'info': '为了测试用，所以写了一个看上去很长的活动介绍，其实这并没有什么卵用orz由于不够长，所以重复几次orz为了测试用，所以写了一个看上去很长的活动介绍，其实这并没有什么卵用orz由于不够长，所以重复几次orz为了测试用，所以写了一个看上去很长的活动介绍，其实这并没有什么卵用orz由于不够长，所以重复几次orz为了测试用，所以写了一个看上去很长的活动介绍，其实这并没有什么卵用orz由于不够长，所以重复几次orz为了测试用，所以写了一个看上去很长的活动介绍，其实这并没有什么卵用orz由于不够长，所以重复几次orz',
  'waitingUser': [{'id': 1, 'nickname': 'User1'}, {'id': 2, 'nickname': 'User2'}, {'id': 3, 'nickname': 'User3'}],
  'denyedUser': [{'id': 4, 'nickname': 'User4'}, {'id': 5, 'nickname': 'User5'}],
  'passedUser': [{'id': 6, 'nickname': 'User6'}],
}

export const test_act_recommand = {
  'code': 0,
  'data': [
  {
    'id': 1,
    'title': "Deep Dark Fantasy",
    'startTime': 1482837273007,
    'endTime': 1482837273007,
    'place': "新日暮里",
    'members': 10,
    'brief': "Billy Herrington Billy Herrington Billy Herrington"
  }, {
    'id': 2,
    'title': "Deep Dark Fantasy",
    'startTime': 1482837273007,
    'endTime': 1482837273007,
    'place': "新日暮里",
    'members': 10,
    'brief': "Billy Herrington Billy Herrington Billy Herrington"
  }]
}

export const test_user_create = {
  'code': 0,
  'data': [{
    'title': "",
  }]
}

export const test_act = {
  'code': 0,
  'data': [{
    'title': "Deep Dark Fantasy",
    'id': 1,
    'type': "哲学活动",
    'startTime': 1482837273007,
    'endTime': 1482837273007,
    'members': 10,
    'passed': 5,
    'host': '哲学联盟',
    'contact': '010-34388888',
    'review': true,
    'participated': 0,
    'denyed': 0,
    'place': "新日暮里",
    'members': 10,
    'image': '',
    'brief': "Billy Herrington Billy Herrington Billy Herrington",
    'info': "Billy Herrington Billy Herrington Billy Herrington Billy Herrington Billy Herrington Billy Herrington Billy Herrington Billy Herrington Billy Herrington"
  }, {
    'title': "Deep Dark Fantasy",
    'id': 1,
    'type': "哲学活动",
    'startTime': 1482837273007,
    'endTime': 1482837273007,
    'members': 10,
    'passed': 5,
    'host': '哲学联盟',
    'contact': '010-34388888',
    'review': true,
    'participated': 0,
    'denyed': 0,
    'place': "新日暮里",
    'members': 10,
    'image': '',
    'brief': "Billy Herrington Billy Herrington Billy Herrington",
    'info': "Billy Herrington Billy Herrington Billy Herrington Billy Herrington Billy Herrington Billy Herrington Billy Herrington Billy Herrington Billy Herrington"
  },]
}
