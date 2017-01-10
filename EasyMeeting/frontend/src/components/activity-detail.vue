<template>
  <div class="row">
    <div class="act-icon col s10 offset-s2 m3 offset-m2">
      <img class="act-image" v-bind:src="act.image">
    </div>
    <div class="act-info col s12 m5">
      <div class="act-title">{{ act.title }}</div>
      <hr>
      <div class="act-time"><i class="fa fa-lg fa-calendar" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;活动时间: 
        <span id="act-time">{{ act.time }}</span>
      </div>
      <div class="act-place"><i class="fa fa-lg fa-paper-plane" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;活动地点: 
        <span id="act-place">{{ act.place }}</span>
      </div>
      <div class="act-brief"><i class="fa fa-lg fa-info-circle" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;&nbsp;活动详细描述: 
        <span id="act-brief">{{ act.info }}</span>
      </div>
      <hr>
      <div class="act-num">
        <span class="act-num-part">
          计划人数：
          <span id="act-total-num">{{ act.members }}</span>
        </span>
        <span class="act-num-part">
          已参加人数：
          <span id="act-remain-num">{{ act.passed + act.waiting }}</span>
        </span>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col m8 offset-m2 s12 offset-s0">
      <hr>
      <div class="act-info">{{ act.info }}</div>
      <div v-if="!act.isAuthor" class="act-operation">
        <a class="btn" v-on:click="participate()">我要报名</a>
      </div>
      <div v-if="act.isAuthor" class="act-operation">
        <a class="btn" v-link="{ path: '/activity/user/' + act.id }">管理报名人员</a>
        <a class="btn" v-link="{ path: '/activity/modify/' + act.id }">修改活动信息</a>
        <a class="btn" v-on:click="deleteAct()">删除活动</a>
      </div>
    </div>
  </div>
</template>

<style lang="less">

.row {
  margin-top: 20px;
  font-family: 'Microsoft Yahei', 'Hiragino Sans GB';
  font-size: 18px;
  .act-image {
    width: 250px;
    margin: 0 auto;
    @media screen and (max-width: 350px) {
      width: 200px;
    }
    @media screen and (max-width: 1000px) and (min-width: 700px) {
      width: 160px;
    }
  }
  .act-title {
    font-size: 26px;
    font-weight: bold;
  }
  .act-time {
    margin-top: 10px;
    font-size: 10px;
  }
  .act-place {
    margin-top: 10px;
  }
  .act-brief {
    margin-top: 10px;
  }
  .act-num {
    margin-top: 10px;
    .act-num-part {
      margin-right: 30px;
      background-color: #ccc;
      padding: 5px 15px 5px 15px;
      border-radius: 10px;
    }
  }
  .act-operation {
    margin-top: 24px;
  }
}

</style>

<script>
import {
  test_activity_detail
} from './test' 

import {
  getMe
} from '../vuex/actions'

import {
  ACT_SET_DETAIL,
} from '../vuex/mutation-types'

export default {
  name: 'activityDetail',
  vuex: {
    getters: {
      act: state => state.activity.data.currentAct,
      user: state => state.user.data
    },
    actions: {
      deleteAct: function () {
        let _this = this
        $.ajax({
          type: 'post',
          url: '/api/activity/delete',
          data: JSON.stringify({
            'act_id': _this.getId(),
          }),
          contentType: 'application/json;charset=utf-8',
          success: function (res) {
            let _data = JSON.parse(res)
            if(_data.errorcode == 200) {
              window.location.href = "#!/homepage"
            }
          }
        })
      },
      getActDetail: function({dispatch}) {
        let _this = this
        $.get("/api/activity/detail?id="+_this.getId()).done(function(res) {
          dispatch(ACT_SET_DETAIL, JSON.parse(res), _this.getId(), _this.user);
        }).fail(function(res) {
          console.log(res)
        });
      },
      postParticate: function  () {
        $.ajax({
          type: 'post',
          url: '/api/activity/operate',
          data: JSON.stringify({
            'activity_id':this.getId(),
            'user_id': this.user.openid,
            'operate_mode':1
          }),
          contentType: 'application/json;charset=utf-8',
          success: function (res) {
            let _data = JSON.parse(res)
            if(_data.errorcode == 200) {
              window.location.href = "#!/homepage"
            }
          }
        })
      },
      getMe,
    }
  },
  ready: function() {
    this.getMe()
    this.getActDetail()
  },
  methods: {
    getId: function() {
      return this.$route.params.id
    },
    participate: function () {
       this.postParticate()
    }
  }
}
</script>
