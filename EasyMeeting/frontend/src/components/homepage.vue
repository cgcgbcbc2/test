<template>
  <div class="carousel carousel-slider center" data-indicators="true">
    <div class="carousel-item white-text" href="#one!">
      <img src="../assets/banner.png">
    </div>
    <div class="carousel-item white-text" href="#two!">
      <img src="../assets/banner.png">
    </div>
  </div>
  <div class="search-field">
    <input class="input" id="search" type="text" class="validate" v-model="searchContent">
    <button class="btn" type="submit" name="action" v-on:click="search()" v-link="{ path: '/activity/list' }">搜索</button>
  </div>
  <div class="act-list">
    <div class="title">强烈推荐</div>
    <hr>
      <ul v-for="act in recommandList">
        <a v-link="{ path: '/activity/detail/' + act.id }">
        <li>
          <div class="card">
            <div class="card-image">
              <img v-bind:src="act.image">
            </div>
            <div class="card-content">
              <div class="title">{{act.title}}</div>
              <div class="time">活动时间: {{ act.time }}</div>
              <div class="place-and-num">活动地点: <span id="place" style="margin-right:50px;">{{act.place}}</span>计划人数：<span id="num">{{act.members}}</span></div>
              <div class="info">活动简介: <span id="info">{{act.brief}}</span></div>
            </div>
        </div>
        </li>
        </a>
      </ul>
  </div>
  <div class="act-list">
    <div class="title">最新活动</div>
    <hr>
      <ul v-for="act in newestList">
        <a v-link="{ path: '/activity/detail/' + act.id }">
        <li>
          <div class="card">
            <div class="card-image">
              <img v-bind:src="act.image">
            </div>
            <div class="card-content">
              <div class="title">{{act.title}}</div>
              <div class="time">活动时间: {{ act.time }}</div>
              <div class="place-and-num">活动地点: <span id="place" style="margin-right:50px;">{{act.place}}</span>计划人数：<span id="num">{{act.members}}</span></div>
              <div class="info">活动简介: <span id="info">{{act.brief}}</span></div>
            </div>
        </div>
        </li>
        </a>
      </ul>
  </div>
</template>

<style lang="less">

.carousel img {
  width: 100%;
  height: 400px;
  @media screen and (max-width: 960px) {
    height: 200px;
  }
}

.search-field {
  width: 350px;
  margin: 0 auto;
  margin-top: 20px;
  margin-bottom: 20px;
  .input {
    width: 200px;
  }
  .btn {
    margin-left: 20px;
    width: 100px;
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
  test_user_init,
  test_act_recommand,
  test_newest_act
} from './test' 

import {
  createActList,
  getMe,
  getTimeString
} from '../vuex/actions'

import {
  USER_SET_INFO,
  USER_SET_ID,
  USER_CLEAR,
  ACT_SET_LIST,
  ACT_SET_TITLE
} from '../vuex/mutation-types'

export default {
  name: 'homepage',
  data: function() {
    return {
      searchContent: '',
      recommandList: [],
      newestList: [],
    }
  },
  vuex: {
    getters: {
      userid: state => state.user.data.openid
    },
    actions: {
      getActList: function() {
        let _this = this;
        $.get("/api/activity/list/refer").done(function (res) {
          console.log(res)
          _this.recommandList = createActList(JSON.parse(res).result_list)
          console.log(_this.recommandList);
        })
        $.get("/api/activity/list/new").done(function (res) {
          _this.newestList = createActList(JSON.parse(res).result_list)
          console.log(_this.newestList);
        })
      },
      initHomepage: function({dispatch}) {
        let _this = this
        $.get("/api/userinfo/detail?user_id=" + _this.userid).done(function(res) {
          //res = test_user_init
          dispatch(USER_CLEAR)
          dispatch(USER_SET_INFO, JSON.parse(res))
        }).fail(function(res) {
          console.log(res)
        })
        /*
        $.get("/api").done(function(res) {
          //res = test_act_recommand
          //if(res.code == 0) {
            //_this.recommandList = createActList(res.data)
          //}
        }).fail(function(res) {
          console.log(res)
        })
        $.get("").done(function(res) {
          //res = test_newest_act
          //if(res.code == 0) {
            //_this.newestList = createActList(res.data)
          //}
        }).fail(function(res) {
          console.log(res)
        })*/
      },
      searchContent: function({dispatch}, content) {
        let param = {
          'search': content
        }
        $.ajax({
          type: "post",
          url: '',
          data: JSON.stringify(param),
          contentType: 'application/json;charset=utf-8',
          success: function(res){
            dispatch(ACT_SET_LIST, res.data)
            dispatch(ACT_SET_TITLE, "搜索结果")
            window.location.href=$("#jump")[0].hash
          },
          error: function(res) {
            console.log(res)
          }
        })
      },
      getMe
    }
  },
  ready: function() {
    this.getMe()
    this.initHomepage()
    this.getActList()
    //console.log(createActList(test_act_recommand.data))
    $('.carousel.carousel-slider').carousel({full_width: true});
  },
  methods: {
    search: function() {
      this.searchAct(this.searchContent)
    },
  }
}
</script>
