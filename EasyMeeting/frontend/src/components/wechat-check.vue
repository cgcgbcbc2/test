<template>
  <h1>
    <div id="result">xx</div>
  </h1>
</template>

<script>

import {
  ACT_SET_LIST,
  ACT_SET_TITLE,
  ACT_SET_PAGE,
  USER_SET_ID,
} from '../vuex/mutation-types'

import {
  createActList,
  getMe
} from '../vuex/actions'

export default {
  name: 'wechatCheck',
  vuex: {
    getters: {
      
    },
    actions: {  
      setLogin: function({dispatch}, id) {
        let _this = this
        $.get('/api/validate/brutelogin?user_id=' + id).done(function(res) {
          _this.turnTo(_this.getType())
          _this.getMe()
        }).fail(function(res) {
          console.log(res)
        })
      },
      turnTo: function({dispatch}, type) {
        console.log(type)
        let url = ""
        $("nav").show();
        $("footer").show();
        if(type == "homepage" || type == "HOMEPAGE") {
          url = "/index/#!/homepage"
          window.location.href = url
        }
        else if(type == "createact" || type == "CREATEACT") {
          url = "/index/#!/activity/create"
          window.location.href = url
        }
        else if(type == "listact" || type == "LISTACT") {
          $.get('/api/activity/list/pages').done(function(res) {
            console.log(res)
            dispatch(ACT_SET_LIST, createActList(JSON.parse(res).result_list))
            dispatch(ACT_SET_TITLE, "活动大厅")
            dispatch(ACT_SET_PAGE, JSON.parse(res).page_info)
            window.location.href = "/index/#!/activity/list"
          }).fail(function(res) {
            console.log(res)
          })
        }
      },
      getMe
    }
  },
  ready: function() {
    this.setLogin(this.getId())
  },
  methods: {
    getId: function () {
      return this.$route.params.id
    },
    getType: function() {
      return this.$route.params.type
    }
  }
}

</script>