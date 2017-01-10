import {
  USER_SET,
  USER_SET_INFO,
  USER_CLEAR,
  USER_SET_ID
} from '../mutation-types'

const state = {
  'data': {
    'openid': '',
    'nickname': 'Test',
    'userinfo': 'This is a brief info',
    'unreadMessageNum': 0,
    'icon': '',
    'avator': '',
    'focusUser': {
      'openid': -1,
      'nickname': '',
      'userinfo': '',
      'phone': -1,
      'mail': '',
      'isSelf': false,
      'icon': '',
      'activityCreated': [],
      'activityParticipate': []
    }
  },
  'status': {

  }
}

const mutations = {
  [USER_SET] (state, data) {
    state.data.nickname = data.username
    state.data.userinfo = data.intro
    state.data.avator = data.avator
  },
  [USER_SET_ID] (state, res) {
    state.data.openid = res;
  },
  [USER_SET_INFO] (state, res, id) {
    /*state.data.focusUser.openid = res.openid;
    state.data.focusUser.nickname = res.nickname;
    state.data.focusUser.userinfo = res.userinfo;
    state.data.focusUser.phone = res.phone;
    state.data.focusUser.mail = res.mail;
    state.data.focusUser.activityCreated = res.activityCreated;
    state.data.focusUser.activityParticipate = res.activityParticipate;
    state.data.focusUser.isSelf = (state.data.openid == state.data.focusUser.openid);*/
    state.data.focusUser.openid = id;
    if(state.data.openid == id) {
      state.data.focusUser.isSelf = true;
    }
    else {
      state.data.focusUser.isSelf = false;
    }
    state.data.focusUser.nickname = res.name;
    state.data.focusUser.phone = res.mobile;
    state.data.focusUser.mail = res.email;
    state.data.focusUser.userinfo = res.introduction;
    state.data.focusUser.activityCreated = res.created;
    state.data.focusUser.activityParticipate = res.passed;
    state.data.focusUser.icon = res.avator;
  }
}

export default {
  state,
  mutations
}
