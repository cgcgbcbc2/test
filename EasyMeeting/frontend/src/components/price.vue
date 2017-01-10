<template>
  <div class="carousel carousel-slider center" data-indicators="true">
    <div class="carousel-item white-text" href="#one!">
      <img src="../assets/banner.png">
    </div>
    <div class="carousel-item white-text" href="#two!">
      <img src="../assets/banner.png">
    </div>
  </div>
  <div class="about">
    <div class="title">费用说明</div>
    <hr>
    <div class="content">
      <div class="subtitle">多平台推送</div>
      多平台推送服务项目的价格还未制定，暂时免费
      <div class="subtitle">高级活动说明</div>
      高级活动说明服务项目的价格还未制定，暂时免费
      <div class="subtitle">活动签到</div>
      活动签到服务项目的价格还未制定，暂时免费
    </div>
  </div>
</template>

<style lang="less">

.about {
  margin-top: 30px;
  font-family: 'Microsoft Yahei', 'Hiragino Sans GB';
  .title {
    font-size: 2em;
    @media screen and (max-width: 960px) {
      font-size: 1.2em;
    }
    font-weight: bold;
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
  .content {
    color: #555;
    font-size: 1.2em;
    @media screen and (max-width: 960px) {
      padding-left: 20px;
      font-size: 1.0em;
    }
    .subtitle {
      font-size: 1.6em;
      font-weight: bold;
      color: #333;
      margin-top: 20px;
      margin-bottom: 20px;
      @media screen and (max-width: 960px) {
        font-size: 1.1em;
      }
    }
  }
}

</style>

<script>

import {
  getMe
} from '../vuex/actions'

export default {
  name: 'price',
  ready: function() {
    this.getMe()
    $('.carousel.carousel-slider').carousel({full_width: true});
  },
  methods: {

  }
}
</script>
