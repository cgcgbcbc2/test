import V from './common'
import App from './App'

import Router from 'vue-router'
import routerMap from './router'
import store from './vuex/store'



import '../node_modules/materialize-css/dist/css/materialize.min.css'
import '../node_modules/materialize-css/dist/js/materialize.min.js'
import '../node_modules/font-awesome/css/font-awesome.min.css'


import materialize from 'materialize-css'

V.Vue.use(Router)
//const router = new Router({hashbang: false, history: true,})
const router = new Router()

routerMap(router)


const vm = V.Vue.extend({store})

router.start(vm, '#app')
