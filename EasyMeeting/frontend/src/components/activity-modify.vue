<template>
  <div class="create-container container">
    <div class="row">
      <h2>修改活动信息</h2>
    </div>
    <div class="progress row" v-show="isSubmiting">
      <div class="indeterminate"></div>
    </div>
    <div class="row">
      <div class="col s12">
        <div class="row">
          <h5>活动信息</h5>
          <div class="input-field col s12">
            <input value="" type="text" class="validate" v-model="title">
            <label>活动名称</label>
          </div>
          <div class="input-field col s12">
            <input value="" type="text" class="validate" v-model="type">
            <label>活动类型</label>
          </div>
          <div class="input-field col s12">
            <input value="" type="text" class="validate" v-model="place">
            <label>活动地点</label>
          </div>
          
          <div class="col-s12">
              <input type="url" name="picUrl" class="form-control" id="input-pic_url" style="width:80%;display:inline;" placeholder="请填入图片链接" value="{{ activity.picUrl }}" required>
              <button type="button" class="btn btn-info" style="width:17%;float:right;" id="input-uploadPic" v-on:click="uploadImage()">上传</button>
          </div>

          <div class="input-field col s12">
            <input value="" type="text" class="validate" v-model="members">
            <label>活动人数上限</label>
          </div>
          <div class="input-field col s12">
            <input value="" type="text" class="validate" v-model="brief">
            <label>活动简介-用于主页简介</label>
          </div>
          <div class="input-field col s12">
            <textarea id="textarea1" class="materialize-textarea" v-model="info"></textarea>
            <label>活动详细描述</label>
          </div>
          <div class="switch-field col s12">
            <div class="switch">
              <span class="tag">是否审核报名用户</span>
              <label>
                否 <input type="checkbox" v-model="review">
                <span class="lever"></span> 是
              </label>
            </div>
          </div>
          <div class="input-field col s6">
            <input value="" type="text" class="validate date-picker" id="start-datepicker" v-model="startdate" data-fx-mobile="true" data-large-mode="true" data-large-default="true" data-max-year="2030" data-min-year="2016">
            <label>开始日期(例:2016/01/02)</label>
          </div>
          <div class="input-field col s6">
            <input value="" type="text" class="validate time-picker" id="start-timepicker" v-model="starttime">
            <label>开始时间(例:09:08)</label>
          </div>
          <div class="input-field col s6">
            <input value="" type="text" class="validate date-picker" id="end-datepicker" v-model="enddate" data-fx-mobile="true" data-large-mode="true" data-large-default="true" data-max-year="2030" data-min-year="2016">
            <label>结束日期(例:2016/01/02)</label>
          </div>
          <div class="input-field col s6">
            <input value="" type="text" class="validate time-picker" id="end-timepicker" v-model="endtime">
            <label>结束时间(例:09:08)</label>
          </div>
          <h5>主办单位信息</h5>
          <div class="input-field col s12">
            <input value="" type="text" class="validate" v-model="host">
            <label>主办单位名称</label>
          </div>
          <div class="input-field col s12">
            <input value="" type="text" class="validate" v-model="contact">
            <label>主办方联系方式</label>
          </div>
          <a class="waves-effect btn" v-on:click="submit()">Submit</a>
        </div>
      </div>
    </div>
    <div class="alert-modal">
      <div class="modal-content">
        <h4>提示信息</h4>
        <p>{{ modalmessage }}</p>
      </div>
      <div class="modal-footer">
        <a v-on:click="hideModal()" class="waves-effect waves-green btn">OK</a>
      </div>
    </div>
  </div>
  <div><input style="display:none" type="file" id="fileUploadBtn" accept="image/*"/></div>
</template>

<style lang="less">
  .picker {
    width:300px!important;
  }
  .switch-field {
    margin-bottom: 30px;
    .tag {
      margin-right: 20px;
    }
  }
  .alert-modal {
    width: 100%;
    height: 100%;
    position: fixed;
    top: 0px;
    left: 0px;
    padding-top: 20%;
    opacity: 0.7;
    background-color: black;
    text-align: center;
    color: white;
    font-family: 'Microsoft Yahei';
    .modal-content {
      opacity: 1;
    }
    .modal-footer {
      margin-top: 50px;
      color: white;
    }
  }
</style>

<script>

import {
  
} from '../vuex/mutation-types'


import {
  changeMainTitle,
  getTimeStamp,
  getTimeString,
  getMe,
  createActList
} from '../vuex/actions'

export default {
  name: 'actCreate',
  components: {

  },
  data: function(){
    return {
      'act_id': 0,
      'title': '',
      'place': '',
      'info': '',
      'type': '',
      'brief': '',
      'startdate': null,
      'starttime': ' ',
      'enddate': null,
      'endtime': ' ',
      'members': 0,
      'limit': '',
      'host': '',
      'image': '/image/activity/default.png',
      'contact': '',
      'modalmessage': '',
      'review': true,
      'isSubmiting': false
    }
  },
  vuex: {
    getters: {
      maintitle: state => state.main.data.title,

      
    },
    actions: {
      changeMainTitle,
      modifyActivity: function({dispatch}, data) {
        let _this = this
        $.ajax({
          type: "post",
          url: '/api/activity/modify',
          data: JSON.stringify(data),
          contentType: 'application/json;charset=utf-8',
          success: function(res){
            let _data = JSON.parse(res)
            if(_data.errorcode == 200) {
              window.location.href = "#!/homepage"
            }
            else {
              _this.modalmessage = '活动名称修改失败'
              $('.alert-modal').css('display', 'inline');
              console.log(res)
            }
            _this.isSubmiting = false
          },
          error: function(res) {
            console.log(res)
            _this.isSubmiting = false
          }
        })
      },
      getActInfo: function({dispatch}) {
        let _this = this;
        $.get("/api/activity/detail?id=" + _this.getId()).done(function(res) {
          let arr = [];
          arr.push(JSON.parse(res));
          let currAct = createActList(arr)[0];
          _this.title = currAct.title;
          _this.place = currAct.place;
          _this.info = currAct.info;
          _this.type = currAct.type;
          _this.brief = currAct.brief;
          _this.startdate = getTimeString(currAct.startTime).date;
          _this.starttime = getTimeString(currAct.startTime).time;
          _this.enddate = getTimeString(currAct.endTime).date;
          _this.endtime = getTimeString(currAct.endTime).time;
          _this.members = currAct.members;
          _this.host = currAct.host;
          _this.image = currAct.image;
          _this.contact = currAct.contact;
        }).fail(function(res) {
          console.log(res);
        });
      },
      getMe
    }
  },
  ready: function() {
    this.getMe()
    this.getActInfo()
    this.changeMainTitle('修改活动信息')
    let _this = this
    $('.alert-modal').css('display', 'none');
    $('#fileUploadBtn').on('change', function () {
      if (this.files.length > 0) {
        var form = new FormData();
        var f = this.files[0];
        //console.log(this.files);
        form.append('image', this.files[0]);
        $.ajax({
          type: 'post',
          url: '/api/activity/upload',
          data: form,
          processData: false,
          contentType: false,
          success: function (res) {
            console.log(res);
            $('#input-pic_url').val(f.name);
            _this.image = JSON.parse(res).pic_url;
          }
        })
      }
    });
  },
  methods:{
    getId: function() {
      return this.$route.params.id
    },
    upLoadImg: function() {

    },
    submit: function() {
      if(!this.title) {
        this.modalmessage = '活动名称不能为空！'
        $('.alert-modal').css('display', 'inline');
        return
      }
      else if(!this.place) {
        this.modalmessage = '活动地点不能为空！'
        $('.alert-modal').css('display', 'inline');
        return
      }
      else if(!this.brief) {
        this.modalmessage = '活动简介不能为空！'
        $('.alert-modal').css('display', 'inline');
        return
      }
      else if(!this.info) {
        this.modalmessage = '活动描述不能为空！'
        $('.alert-modal').css('display', 'inline');
        return
      }
      else if(!this.startdate) {
        this.modalmessage = '请选择活动开始日期！'
        $('.alert-modal').css('display', 'inline');
        return
      }
      else if(!this.enddate) {
        this.modalmessage = '请选择活动结束日期！'
        $('.alert-modal').css('display', 'inline');
        return
      }
      else if(!this.starttime || this.starttime == ' ') {
        this.modalmessage = '请选择活动开始时间！'
        $('.alert-modal').css('display', 'inline');
        return
      }
      else if(!this.starttime || this.starttime == ' ') {
        this.modalmessage = '请选择活动结束时间！'
        $('.alert-modal').css('display', 'inline');
        return
      }
      let start = getTimeStamp(this.startdate, this.starttime)
      let end = getTimeStamp(this.enddate, this.endtime)
      let now = Date.now()
      if(start < now) {
        this.modalmessage = '活动开始时间不能早于当前时间！'
        $('.alert-modal').css('display', 'inline');
        return
      }
      if(end < start) {
        this.modalmessage = '活动结束时间应晚于活动开始时间！'
        $('.alert-modal').css('display', 'inline');
        return
      }
      this.isSubmiting = true
      this.modifyActivity({
        'act_id': this.getId,
        'title': this.title,
        'type': this.type,
        'startTime': start,
        'endTime': end,
        'members': this.members,
        'place': this.place,
        'review': this.review,
        'host': this.host,
        'contact': this.contact,
        'image': this.image,
        'brief': this.brief,
        'info': this.info,
      })
    },
    hideModal: function () {
      $('.alert-modal').css('display', 'none');
    },
    uploadImage: function () {
      $('#fileUploadBtn').click();
    }
  }
}

</script>
