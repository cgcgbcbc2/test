<template>
  <div class="row">
    <div class="user-icon col s10 offset-s2 m3 offset-m2">
      <img class="user-image" v-bind:src="focusUser.icon">
    </div>
    <div class="user-info col s12 m5">
      <div class="user-title">User {{focusUser.nickname}}</div>
      <hr>
      <div class="user-mobile"><i class="fa fa-lg fa-phone" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;手机: 
        <span id="user-mobile">{{focusUser.phone}}</span>
      </div>
      <div class="user-mail"><i class="fa fa-lg fa-envelope" aria-hidden="true"></i>&nbsp;&nbsp;邮箱: 
        <span id="user-mail">{{focusUser.mail}}</span>
      </div>
      <hr>
      <div class="user-intro"><i class="fa fa-lg fa-info-circle" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;个人简介: 
        <span id="user-intro">{{focusUser.userinfo}}</span>
      </div>
      <div class="leave-msg" v-if="!focusUser.isSelf">
        <div class="input-field">
          <textarea id="msg" class="materialize-textarea"></textarea>
          <label for="msg">留言内容</label>
        </div>
        <a class="btn">留言</a>
      </div>
      <div class="modify" v-if="focusUser.isSelf">
        <a class="btn" v-link="{ path: '/modify/' }">更改个人信息</a>
      </div>
    </div>
  </div>
  <div class="act-list" v-if="!focusUser.isSelf">
    <div class="title">ta创建的活动</div>
    <hr>
    <ul>
      <li v-for="i in focusUser.activityCreated">
        <div class="card">
          <div class="card-image">
            <a v-link="{ path: '/activity/detail/' + i.ID }"><img v-bind:src="i.image"></a>
          </div>
          <div class="card-content">
            <a v-link="{ path: '/activity/detail/' + i.ID }"><div class="title">{{ i.name }}</div></a>
            <div class="time">活动时间: {{ getCaoNiMaTimeString(parseInt(i.start_time)) }}</div>
            <div class="place-and-num">活动地点: <span id="place" style="margin-right:50px;">{{ i.loc }}</span>
              计划人数：<span id="num">{{ i.member_maxcount }}</span></div>
            <div class="info">活动简介: <span id="info">{{ i.brief_desc }}</span></div>
          </div>
       </div>
      </li>
    </ul>
  </div>
  <div class="act-list" v-if="!focusUser.isSelf">
    <div class="title">ta参加的活动</div>
    <hr>
    <ul>
      <li v-for="i in focusUser.activityParticipate">
        <div class="card">
          <div class="card-image">
            <a v-link="{ path: '/activity/detail/' + i.ID }"><img v-bind:src="i.image"></a>
          </div>
          <div class="card-content">
            <a v-link="{ path: '/activity/detail/' + i.ID }"><div class="title">{{ i.name }}</div></a>
            <div class="time">活动时间: {{ getCaoNiMaTimeString(parseInt(i.start_time)) }}</div>
            <div class="place-and-num">活动地点: <span id="place" style="margin-right:50px;">{{ i.loc }}</span>
              计划人数：<span id="num">{{ i.member_maxcount }}</span></div>
            <div class="info">活动简介: <span id="info">{{ i.brief_desc }}</span></div>
          </div>
       </div>
      </li>
    </ul>
  </div>
  <div class="act-list" v-if="focusUser.isSelf">
    <div class="title">您创建的活动</div>
    <hr>
    <ul>
      <li v-for="i in focusUser.activityCreated">
        <div class="card">
          <div class="card-image">
            <a v-link="{ path: '/activity/detail/' + i.ID }"><img v-bind:src="i.image"></a>
          </div>
          <div class="card-content">
            <a v-link="{ path: '/activity/detail/' + i.ID }"><div class="title">{{ i.name }}</div></a>
            <div class="time">活动时间: {{ getCaoNiMaTimeString(parseInt(i.start_time)) }}</div>
            <div class="place-and-num">活动地点: <span id="place" style="margin-right:50px;">{{ i.loc }}</span>
              计划人数：<span id="num">{{ i.member_maxcount }}</span></div>
            <div class="info">活动简介: <span id="info">{{ i.brief_desc }}</span></div>
          </div>
       </div>
      </li>
    </ul>
  </div>
  <div class="act-list" v-if="focusUser.isSelf">
    <div class="title">您参加的活动</div>
    <hr>
    <ul>
      <li v-for="i in focusUser.activityParticipate">
        <div class="card">
          <div class="card-image">
            <a v-link="{ path: '/activity/detail/' + i.ID }"><img v-bind:src="i.image"></a>
          </div>
          <div class="card-content">
            <a v-link="{ path: '/activity/detail/' + i.ID }"><div class="title">{{ i.name }}</div></a>
            <div class="time">活动时间: {{ getCaoNiMaTimeString(parseInt(i.start_time)) }}</div>
            <div class="place-and-num">活动地点: <span id="place" style="margin-right:50px;">{{ i.loc }}</span>
              计划人数：<span id="num">{{ i.member_maxcount }}</span></div>
            <div class="info">活动简介: <span id="info">{{ i.brief_desc }}</span></div>
          </div>
       </div>
      </li>
    </ul>
  </div>
</template>

<style lang="less">

.row {
  margin-top: 20px;
  font-family: 'Microsoft Yahei', 'Hiragino Sans GB';
  font-size: 18px;
  .user-image {
    width: 250px;
    margin: 0 auto;
    @media screen and (max-width: 350px) {
      width: 200px;
    }
    @media screen and (max-width: 1000px) and (min-width: 700px) {
      width: 160px;
    }
  }
  .user-title {
    font-size: 32px;
    font-weight: bold;
  }
  .user-mobile {
    margin-top: 10px;
  }
  .user-mail {
    margin-top: 10px;
  }
  .user-intro {
    margin-top: 10px;
  }
  .leave-msg {
    margin-top: 24px;
  }
  .modify {
    margin-top: 24px;
  }
}

.act-list {
  .title {
    font-size: 2em;
    @media screen and (max-width: 960px) {
      font-size: 1.2em;
    }
    font-weight: bold;
    font-family: 'Microsoft Yahei', 'Hiragino Sans GB';
  }
  padding-left: 10%;
  width: 90%;
  @media screen and (max-width: 960px) {
    .title {
      padding-left: 20px;
    }
    padding-left: 0;
    width: 100%;
  }
  .card {
    font-family: 'Microsoft Yahei', 'Hiragino Sans GB';
    overflow: hidden;
    height: 200px;
    @media screen and (max-width: 960px) {
      height: 130px;
    }
    .card-image {
      width: 150px;
      @media screen and (max-width: 960px) {
        width: 80px;
        margin-left: 20px;
      }
      float: left;
    }
    .card-content {
      padding-left: 200px;
      font-size: 1.1em;
      .title {
        color: black;
        padding-left: 0px;
      }
      .info {
        margin-top: 5px;
        height: 50px;
        line-height: 25px;
        overflow: hidden;
        text-overflow: ellipsis;
        @media screen and (max-width: 960px) {
          height: 32px;
          line-height: 16px;
        }
      }
    }
  }
}

</style>

<script>
import {
  test_user_info,
  test_user_create
} from './test' 

import {
  USER_SET_INFO,
  USER_SET_ID
} from '../vuex/mutation-types'

import {
  getTimeString,
  getMe
} from '../vuex/actions'

export default {
  name: 'userIntro',
  data: function() {
    return {
      createList: [{
        
      }],
      participateList: []
    }
  },
  vuex: {
    getters: {
      focusUser: state => state.user.data.focusUser,
      userid: state => state.user.data.openid,
    },
    actions: {
      getInfo: function({dispatch}) {
        let _this = this;
        $.get("/api/userinfo/detail?user_id=" + _this.getId()).done(function(res) {
          dispatch(USER_SET_INFO, JSON.parse(res), _this.getId());
          console.log(res);
          console.log(_this.userid);
        }).fail(function(res) {
          console.log(res);
        });
      },
      getMe
    }
  },
  ready:function() {
    this.getMe();
    this.getInfo();
  },
  methods: {
    getId: function() {
      return this.$route.params.id
    },
    getCaoNiMaTimeString: function (timeStamp) {
      let dateObj = new Date(parseInt(timeStamp))
      return (dateObj.getFullYear() + '/' + dateObj.getMonth()+1) + '/' + dateObj.getDate();
    }
  }
}
</script>
