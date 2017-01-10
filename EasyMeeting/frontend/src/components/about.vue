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
    <div class="title">关于我们</div>
    <hr>
    <div class="content">
      <div class="subtitle">网站简介</div>
      EasyMeeting是一个基于微信公众平台的会议活动组织系统，覆盖会议和活动的发布、报名、审核、支付、通知、签到、日程等整个过程，手机和统计会议或活动的信息和数据，为会议/活动的组织方提供高效的智能化管理，为会议/活动参与者提供最便捷的服务。系统同时能够处理大批量的请求，长时间稳定运行于云平台，并能够及时通过消息提醒等途径通知相关参与人员。
      <div class="subtitle">小组简介</div>
      "我们的组名不可能这么难起"小组是由清华大学软件学院软件41班的唐人杰、李俊杰和软件42班的卫国扬、陈钰帆组成的软件工程(3)课程作业小组，小组组成旨在更快更好地完成软工三的课程大作业。
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
export default {
  name: 'about',
  ready: function() {
    $('.carousel.carousel-slider').carousel({full_width: true});
  },
  methods: {
    
  }
}
</script>
