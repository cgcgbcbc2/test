<template>
  <div class="user-container">
    <div class="row">
      <div class="col s12">
        <ul class="tabs">
          <li class="switchTab1 tab col s4"><a class="active" v-on:click="switchTab(1);">待审核用户</a></li>
          <li class="switchTab2 tab col s4"><a v-on:click="switchTab(2);">已通过用户</a></li>
          <li class="switchTab3 tab col s4"><a v-on:click="switchTab(3);">已拒绝用户</a></li>
        </ul>
      </div>
      <div id="test1" class="single col s12">
        <ul class="collection" v-for="user in act.waitingUser">
          <li class="collection-item avatar">
            <img v-bind:src="user.UAvator" alt="" class="icon">
            <span class="username">{{ user.UName }}</span>
            <span class="right-btn">
              <a class="waves-effect waves-light btn" v-on:click="pass(user.UID)">通过</a>
              <a class="waves-effect waves-light btn" v-on:click="refuse(user.UID)">拒绝</a>
            </span>
          </li>
        </ul>
      </div>
      <div id="test2" class="single col s12">
        <ul class="collection" v-for="user in act.passedUser">
          <li class="collection-item avatar">
            <img v-bind:src="user.UAvator" alt="" class="icon">
            <span class="username">{{ user.UName }}</span>
          </li>
        </ul>
      </div>
      <div id="test3" class="single col s12">
        <ul class="collection" v-for="user in act.denyedUser">
          <li class="collection-item avatar">
            <img v-bind:src="user.UAvator" alt="" class="icon">
            <span class="username">{{ user.UName }}</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style lang="less">

.user-container {
  .row {
    width: 50%;
    @media screen and (max-width: 960px) {
      width: 100%;
    }
    margin-top: 50px;
    margin-bottom: 50px;
    .tabs {
      overflow: hidden;
    }
    .tabs:hover {
      cursor: pointer;
    }
    .collection {
      .collection-item {
        .icon {
          width: 50px;
          margin-top: 10px;
          margin-left: 10px;
          vertical-align:middle;
        }
        .username {
          font-size: 20px;
          font-weight: bold;
          padding-left: 50px;
        }
        .right-btn {
          float: right;
          margin-top: 10px;
        }
      }
    }
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
  ACT_SET_DETAIL
} from '../vuex/mutation-types'

export default {
  name: 'activityDetail',
  data: function() {
    return {
      currentTab: 1,
    }
  },
  vuex: {
    getters: {
      act: state => state.activity.data.currentAct,
    },
    actions: {
      getActDetail: function({dispatch}) {
        let _this = this;
        $.get('/api/activity/detail?id=' + _this.getId()).done(function(res) {
          //res = test_activity_detail;
          dispatch(ACT_SET_DETAIL, JSON.parse(res), _this.getId(), JSON.parse(res).uID);
          console.log(res);
        }).fail(function(res) {
          console.log(res);
        });
      }
    },
    getMe
  },
  ready: function() {
    this.getMe()
    this.getActDetail();
    $('#test1').css('display', 'inline');
    $('#test2').css('display', 'none');
    $('#test3').css('display', 'none');
  },
  methods: {
    getId: function () {
      return this.$route.params.id
    },
    switchTab: function (id) {
      for (var i = 1; i <= 3; i++) {
        $('#test' + i).css('display', 'none');
      };
      $('#test' + id).css('display', 'inline');
      if (this.currentTab < id) {
        $(".indicator").animate({right: 2 * $('.switchTab1').width() - $('.switchTab' + id).position().left});
        $(".indicator").animate({left: $('.switchTab' + id).position().left});
      } else {
        $(".indicator").animate({left: $('.switchTab' + id).position().left});
        $(".indicator").animate({right: 2 * $('.switchTab1').width() - $('.switchTab' + id).position().left});
      };
      this.currentTab = id;
    },
    pass: function (wtf_id) {
      $.ajax({
        type: 'post',
        url: '/api/activity/operate',
        data: JSON.stringify({
          'activity_id': this.getId(),
          'user_id': wtf_id,
          'operate_mode': 2
        }),
        contentType: 'application/json;charset=utf-8',
        success: function (res) {
        }
      })
    },
    refuse: function (wtf_id) {
      $.ajax({
        type: 'post',
        url: '/api/activity/operate',
        data: JSON.stringify({
          'activity_id': this.getId(),
          'user_id': wtf_id,
          'operate_mode': 3
        }),
        contentType: 'application/json;charset=utf-8',
        success: function (res) {
          window.location.href = "#!/activity/user/" + this.getId();
        }
      })
    }
  }
}
</script>
