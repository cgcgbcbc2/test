import App from './App'
import homepage from './components/homepage'
import about from './components/about'
import price from './components/price'
import actList from './components/activity-list'
import actDetail from './components/activity-detail'
import actUser from './components/activity-user'
import usrIntro from './components/user-intro'
import usrModify from './components/user-modify'
import message from './components/message'
import actCreate from './components/activity-create'
import actModify from './components/activity-modify'
import validate from './components/validate'
import wechatCheck from './components/wechat-check'
import mobileWelcome from './components/mobile-welcome'
import login from './login'

export default function(router) {
  router.map({
    '/': {
      component: App,
      subRoutes:{
        '/': {
          component: login
        },
        '/homepage':{
          component: homepage
        },
        '/about': {
          component: about
        },
        '/price': {
          component: price
        },
        '/activity/list': {
          component: actList
        },
        '/activity/detail/:id': {
          component: actDetail
        },
        '/activity/user/:id': {
          component: actUser
        },
        '/user/:id': {
          component: usrIntro
        },
        '/modify': {
          component: usrModify
        },
        '/message': {
          component: message
        },
        '/activity/create': {
          component: actCreate
        },
        '/activity/modify/:id': {
          component: actModify
        },
        '/wechat/check/:id/:type': {
          component: wechatCheck
        },
        '/mobile/welcome': {
          component: mobileWelcome
        }
      }
    },
    '/validate': {
      component: validate
    },
    '/login': {
      component: login
    }
  })
}
