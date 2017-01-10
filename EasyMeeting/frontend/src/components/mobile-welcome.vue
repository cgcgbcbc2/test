<template>
  <div class="row">
    <div class="col s12 m5">
      <div class="card-panel teal">
        <span class="white-text">
          欢迎来到EasyMeeting!</br>从微信公众号进入体验更佳哦～
        </span>
        <div class="welcome"><img id="qrcode" src="../assets/qrcode.jpeg"></div>
      </div>
    </div>
  </div>
</template>

<script>

import {
  ACT_SET_LIST,
  ACT_SET_TITLE,
  ACT_SET_PAGE,
  USER_SET_ID,
} from '../vuex/mutation-types'

import {
  createActList
} from '../vuex/actions'

export default {
  name: 'mobileWelcome',
  ready: function() {
    $("nav").hide();
    $("footer").hide();
  }
}
</script>

<style lang="less">
.welcome {
  width: 90%;
  height:90%;
  margin: 0 auto;
  padding-top: 50px;
  #qrcode {
    width: 100%;
    height: 100%;
  }
}
</style>