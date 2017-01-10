<template>
  <div class="act-list">
    <div class="title"><span class="user-title">Anonymous</span>的消息</div>
    <hr>
    <ul>
      <li>
        <div class="card">
          <div class="card-image">
            <img src="../assets/huaji.jpg">
          </div>
          <div class="card-content">
            <div class="from"><span id="from">滑稽</span>：</div>
            <div class="new">new</div>
            <div class="content">你们搞的这个活动，Exciting啊！</div>
          </div>
       </div>
      </li>
      <li>
        <div class="card">
          <div class="card-image">
            <img src="../assets/huaji.jpg">
          </div>
          <div class="card-content">
            <div class="from"><span id="from">滑稽</span>：</div>
            <div class="content">你们搞的这个活动，Exciting啊！*2</div>
          </div>
       </div>
      </li>
    </ul>
  </div>
</template>

<style lang="less">

.act-list {
  margin-top: 20px;
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
    .card-image {
      width: 150px;
      @media screen and (max-width: 960px) {
        width: 80px;
        margin-left: 20px;
      }
      float: left;
    }
    .card-content {
      margin-top: 0px;
      padding-top: 0px;
      padding-left: 200px;
      height: 180px;
      font-size: 1.2em;
      @media screen and (max-width: 960px) {
        padding-left: 120px;
        height: 90px;
        font-size: 1em;
      }
      .from {
        padding-left: 0px;
        font-size: 1.5em;
        font-weight: bold;
        margin-bottom: 10px;
      }
      .from, .new {
        display: inline;
      }
      .new {
        float: right;
        padding-left: 7px;
        padding-right: 7px;
        color: white;
        font-size: 16px;
        background-color: red;
        border-radius: 10px;
      }
    }
  }
}

</style>

<script>
export default {
  name: 'homepage',
  methods: {

  }
}
</script>
