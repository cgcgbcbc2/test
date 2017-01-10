import {
  ACT_SET_DETAIL,
  ACT_SET_LIST,
  ACT_SET_TITLE,
  ACT_SET_PAGE
} from '../mutation-types'

import {
  getTimeString,
  default_img
} from '../actions'

const state = {
  'data': {
    'currentAct': {
      'id': -1,
      'title': '',
      'type': '',
      'time': '',
      'place': '',
      'members': -1,
      'waiting': -1,
      'passed': -1,
      'isAuthor': false,
      'brief': '',
      'info': '',
      'host': '',
      'contact': '',
      'image': '',
      'review': 'true',
      'startTime': '',
      'endTime': '',
      'creator': {},
      'image': '',
      'waitingUser': [],
      'denyedUser': [],
      'passedUser': []
    },
    'actList': [
      {
        id: 1,
        title: "test title",
        startTime: "2016-10-22",
        endTime: "2016-11-13",
        place: "1#412",
        brief: "This is a brief introduction",
      },
      {
        id: 2,
        title: "test title",
        startTime: "2016-10-22",
        endTime: "2016-11-13",
        place: "1#412",
        brief: "This is a brief introduction",
      }
    ]
  },
  'status': {
    'listTitle': "所有活动",
    'totalPage': 6,
    'currentPage': 3,
  }
}

const mutations = {
  [ACT_SET_DETAIL] (state, res, id, user) {
    state.data.currentAct.id = id
    state.data.currentAct.title = res.name
    state.data.currentAct.host = res.host
    console.log(user)
    if(user.openid == res.uID) {
      state.data.currentAct.isAuthor = true
    }
    else {
      state.data.currentAct.isAuthor = false
    }
    state.data.currentAct.startTime = parseInt(res.start_time)
    state.data.currentAct.endTime = parseInt(res.end_time)
    let start = getTimeString(res.start_time)
    let end = getTimeString(res.end_time)
    console.log(start)
    console.log(end)
    state.data.currentAct.time = start.date + ' ' + start.time + ' 至 ' + end.date  + ' ' + end.time
    state.data.currentAct.place = res.loc
    state.data.currentAct.type = res.type
    state.data.currentAct.members = res.member_maxcount
    state.data.currentAct.passed = res.member_passed_count
    state.data.currentAct.waiting = res.member_participatied_count
    state.data.currentAct.brief = res.brief_desc
    state.data.currentAct.info = res.desc
    state.data.currentAct.image = res.pic_url
    state.data.currentAct.creator = {
      'id': res.uID,
      'name': res.uName,
      'avatar': res.uAvator,
    }
    if(res.image == '' || res.image == null) {
      state.data.currentAct.image = default_img
    }
    else {
      state.data.currentAct.image = res.image
    }
    state.data.currentAct.waitingUser = res.member_participatied
    state.data.currentAct.denyedUser = res.member_denied
    state.data.currentAct.passedUser = res.member_passed
  },
  [ACT_SET_LIST] (state, data) {
    console.log(data)
    state.data.actList = data
  },
  [ACT_SET_TITLE] (state, title) {
    state.status.listTitle = title
  },
  [ACT_SET_PAGE] (state, page){
    state.status.currentPage = page[0].page + 1
    state.status.totalPage = parseInt(page[0].count/10) + 1
  }
}

export default {
  state,
  mutations
}
