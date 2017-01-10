import V from '../common'
import Vuex from 'Vuex'

V.Vue.use(Vuex)

import user from './modules/user'
import activity from './modules/activity'
import message from './modules/message'
import main from './modules/main'


export default new Vuex.Store({
  modules: {
    user,
    activity,
    message,
    main,
  }
})