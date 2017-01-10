<template>
  <div class="search-field">
    <input class="input" id="search" type="text" class="validate" v-model="searchContent">
    <button class="btn" type="submit" name="action" v-on:click="search">搜索</button>
  </div>
  <div class="act-list">
    <div class="title">{{listTitle}}</div>
    <hr>
    <template v-for="act in actList">
      <ul>
        <a v-link="{ path: '/activity/detail/' + act.id }">
        <li>
          <div class="card">
            <div class="card-image">
              <img v-bind:src="act.image">
            </div>
            <div class="card-content">
              <div class="title">{{act.title}}</div>
              <div class="time">活动时间: {{act.time}}</div>
              <div class="place-and-num">活动地点: <span id="place" style="margin-right:50px;">{{act.place}}</span>计划人数：<span id="num">{{act.members}}</span></div>
              <div class="time">活动主办方: {{act.host}}</div>
              <div class="info">活动简介: <span id="info">{{act.brief}}</span></div>
            </div>
        </div>
        </li>
        </a>
      </ul>
    </template>
    <ul class="pagination">
      <li v-if="currentPage == 1" class="disabled"><a><i class="fa fa-chevron-left" aria-hidden="true"></i></a></li>
      <li v-if="currentPage != 1" class="waves-effect"><a v-on:click="jumpTo(0)"><i class="fa fa-chevron-left" aria-hidden="true"></i></a></li>
      <template v-for="i in totalPage">
        <li v-if="(i + 1) == currentPage" class="active"><a>{{ i + 1 }}</a></li>
        <li v-if="(i + 1) != currentPage" class="waves-effect"><a v-on:click="jumpTo(i)">{{ i + 1 }}</a></li>
      </template>
      <li v-if="currentPage == totalPage" class="disabled"><a><i class="fa fa-chevron-right"></i></a></li>
      <li v-if="currentPage != totalPage" class="waves-effect"><a v-on:click="jumpTo(totalPage - 1)"><i class="fa fa-chevron-right"></i></a></li>
    </ul>
  </div>
</template>

<style lang="less">

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
    color: black !important;
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

.pagination {
  margin-top: 50px;
  text-align: center;
}

</style>

<script>
import {
  test_activity_list
} from './test'

import {
  getMe,
  createActList
} from '../vuex/actions'

import {
  ACT_SET_LIST,
  ACT_SET_TITLE,
  ACT_SET_PAGE
} from '../vuex/mutation-types'

export default {
  name: 'actList',
  data: function() {
    return {
      gotoPageId: 0,
      searchContent: '',
    }
  },
  vuex: {
    getters: {
      actList: state => state.activity.data.actList,
      listTitle: state => state.activity.status.listTitle,
      totalPage: state => state.activity.status.totalPage,
      currentPage: state => state.activity.status.currentPage,
    },
    actions: {
      gotoPage: function ({dispatch}) {
        $.ajax({
          type: "get",
          url: '/api/activity/list/pages?page=' + this.gotoPageId,
          success: function(res){
            dispatch(ACT_SET_LIST, createActList(JSON.parse(res).result_list))
            dispatch(ACT_SET_PAGE, JSON.parse(res).page_info)
          },
          error: function(res) {
            console.log(res)
          }
        })
      },
      searchAct: function() {
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
      getMe,
    }
  },
  ready: function() {
    this.getMe()
  },
  methods: {
    jumpTo: function (pageId) {
      this.gotoPageId = pageId;
      this.gotoPage();
    },
    search: function() {
      this.searchAct(this.searchContent)
    }
  }
}
</script>
