<template>
<div>
  <nav>
    <div class="nav-wrapper blue">
      <a v-link="{ path: '/homepage' }" class="brand-logo white-text">EasyMeeting</a>
      <a v-on:click="showSideBar()" data-activates="mobile-demo" class="button-collapse"><i class="fa fa-bars fa-lg" aria-hidden="true"></i></a>
      <ul class="right hide-on-med-and-down">
        <li><a v-link="{ path: '/activity/create' }" class="white-text">创建活动</a></li>
        <li><a v-link="{ path: '/user/' + userid }" class="white-text">个人中心</a></li>
        <li><a v-on:click="getAllList" class="white-text">活动大厅</a></li>
        <li><a v-link="{ path: '/message' }" class="white-text">我的私信<span class="alert-num" v-show="unreadMessage != 0">{{unreadMessage}}</span></a></li>
        <li><a v-link="{ path: '/price' }" class="white-text">费用说明</a></li>
        <li><a v-link="{ path: '/about' }" class="white-text">关于我们</a></li>
        <li><a v-on:click="logout()" class="white-text">登出</a></li>
      </ul>
      <ul class="side-nav" id="mobile-demo">
        <div class="user-area">
          <a v-link="{ path: '/user/' + userid }" class="side-nav-icon"><img class="user-icon" v-bind:src="avator"></a>
          <a v-link="{ path: '/user/' + userid }" class="side-nav-username">{{ username }}</a>
          <a v-link="{ path: '/user/' + userid }" class="side-nav-info">{{ userinfo }}</a>
        </div>
        <li><a v-link="{ path: '/activity/create' }">创建活动</a></li>
        <li><a v-link="{ path: '/user/' + userid }" >个人中心</a></li>
        <li><a v-on:click="getAllList">活动大厅</a></li>
        <li><a v-link="{ path: '/message' }" >我的私信<span class="alert-num" v-show="unreadMessage != 0">{{unreadMessage}}</span></a></li>
        <li><a v-link="{ path: '/price' }">费用说明</a></li>
        <li><a v-link="{ path: '/about' }">关于我们</a></li>
        <li><a v-on:click="logout()">登出</a></li>
      </ul>
    </div>
  </nav>
  <div id="main-container">
    <router-view></router-view>
  </div>
  <footer class="page-footer white black-text">
    © 2016 Copyright 我们的组名不可能这么难起
  </footer>
</div>
</template>

<script>

import {
  ACT_SET_LIST,
  ACT_SET_TITLE,
  ACT_SET_PAGE,
  USER_SET_ID,
  USER_SET_INFO
} from './vuex/mutation-types'

import {
  createActList,
  getMe
} from './vuex/actions'

import {
  test_act
} from './components/test'

export default {
  name: 'App',
  components: {

  },
  data: function() {
    return {
      sideXpos: -100,
      timer: 0
    }
  },
  vuex: {
    getters: {
      maintitle: state => state.main.data.title,

      username: state => state.user.data.nickname,
      userid: state => state.user.data.openid,
      userinfo: state => state.user.data.userinfo,
      avator: state => state.user.data.avator,
      unreadMessage: state => state.user.data.unreadMessageNum,
    },
    actions: {
      getUserBriefInfo: function() {
      },
      getAllList: function({dispatch}) {
        $.get('/api/activity/list/pages').done(function(res) {
          console.log(res)
          dispatch(ACT_SET_LIST, createActList(JSON.parse(res).result_list))
          dispatch(ACT_SET_TITLE, "活动大厅")
          dispatch(ACT_SET_PAGE, JSON.parse(res).page_info)
          window.location.href = "/index/#!/activity/list"
        }).fail(function(res) {
          console.log(res)
        })
      },
      getMe
    }
  },
  ready: function() {
    let _this = this;
    $(".button-collapse").sideNav({
      closeOnClick: true,
    });
    $(document).click(function(e){
      if ($('.side-nav').css('transform') >= "matrix(1, 0, 0, 1, 0, 0)" && e.pageX > $('.side-nav').width()) {
        _this.hideSideBar();
      };
    });
    $('.drag-target').css('display', 'none');
    this.getMe()
    this.getUserBriefInfo()
  },
  methods: {
    showSideBar: function () {
      let _this = this;
      if (_this.sideXpos >= 0) {
        return;
      };
      this.timer = setInterval(function () {
        if (_this.sideXpos >= 0) {
          $('.side-nav').css({'transform': 'translateX(0%)'});
          _this.sideXpos = 0;
          clearInterval(_this.timer);
        } else {
          $('.side-nav').css({'transform': 'translateX(' + _this.sideXpos + '%)'});
          _this.sideXpos = _this.sideXpos + 4;
        };
      }, 6);
    },
    hideSideBar: function () {
      let _this = this;
      if (_this.sideXpos <= -100) {
        return;
      };
      this.timer = setInterval(function () {
        if (_this.sideXpos <= -100) {
          $('.side-nav').css({'transform': 'translateX(-100%)'});
          _this.sideXpos = -100;
          $('body').css('overflow', 'visible');
          clearInterval(_this.timer);
        } else {
          $('.side-nav').css({'transform': 'translateX(' + _this.sideXpos + '%)'});
          _this.sideXpos = _this.sideXpos - 4;
        };
      }, 6);
    },
    logout: function () {
      $.post('/api/validate/logout').done(function(res) {
        console.log(res);
        window.location.href = "/index/#!";
      }).fail(function(res) {
        console.log(res);
      })
    },

  }
}
</script>

<style lang="less">

body {
  margin: 0;
  padding: 0;
  .nav-wrapper {
    .brand-logo {
      margin-left: 5%;
    }
    .material-icons img {
      width: 30px;
      height: 30px;
      margin-top: 15px;
    }
    .right {
      font-family: 'Microsoft Yahei', 'Hiragino Sans GB';
    }
    .alert-num {
      margin-left: 10px;
      padding-left: 5px;
      padding-right: 5px;
      color: white;
      font-size: 16px;
      background-color: red;
      border-radius: 10px;
    }
    .side-nav {
      user-select: none;
      text-align: center;
      font-family: 'Microsoft Yahei', 'Hiragino Sans GB';
      .user-area {
        padding-top: 50px;
        background: #2196F3;
        color: #fff;
        padding-left: 20px;
      }
      .side-nav-icon {
        text-align: left;
        height: 60px;
        .user-icon {
          width: 60px;
          height: 60px;
          border-radius: 50%;
        }
      }
      .side-nav-username {
        text-align: left;
        font-size: 24px;
        height: 40px;
        color: #fff;
      }
      .side-nav-info {
        text-align: left;
        height: 50px;
        line-height: 25px;
        overflow-y: hidden;
        margin-bottom: 20px;
        color: #fff;
      }
      li {
        height: 70px;
        a {
          font-size: 18px;
        }
        
      }
    }
  }
  .container {
    max-width: 1000px;
    margin: 0 auto;
  }
  .hidden {
    display: none;
  }
  footer {
    width: 320px;
    margin: 0 auto;
    margin-bottom: 50px;
    font-family: 'Microsoft Yahei', 'Hiragino Sans GB';
  }
}

</style>
