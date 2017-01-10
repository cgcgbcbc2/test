import {
  MAIN_TITLE_CHANGE
} from '../mutation-types'

const state = {
  'data': {
    'title': 'EasyMeeting',
  },
  'status': {

  }
}

const mutations = {
  [MAIN_TITLE_CHANGE] (state, title) {
    state.data.title = title
  }
}

export default {
  state,
  mutations
}