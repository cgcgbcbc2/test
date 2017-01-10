<template>
  <div class="create-container container">
    <div class="row">
      <h2>修改个人信息</h2>
    </div>
    <div class="progress row hidden">
      <div class="indeterminate"></div>
    </div>
    <div class="row">
      <div class="col s12">
        <div class="row">
          <div class="input-field col s12">
            <input id="name" value="" type="text" class="validate" v-model="name">
            <label>昵称</label>
          </div>
          
          <div class="col-s12">
              <input type="url" name="picUrl" class="form-control" id="input-pic_url" style="width:80%;display:inline;" placeholder="请填入图片链接" value="{{ activity.picUrl }}" required>
              <button type="button" class="btn btn-info" style="width:17%;float:right;" id="input-uploadPic" v-on:click="uploadImage()">上传</button>
          </div>

          <div class="input-field col s12">
            <input id="phone" value="" type="text" class="validate" v-model="phone">
            <label>手机</label>
          </div>
          <div class="input-field col s12">
            <input id="email" value="" type="text" class="validate" v-model="email">
            <label>邮箱</label>
          </div>
          <div class="input-field col s12">
            <textarea id="description" class="materialize-textarea" v-model="description"></textarea>
            <label>个人简介</label>
          </div>
          <a class="waves-effect waves-light btn" v-on:click="submit()">Submit</a>
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
  test_user_info,
  test_user_create
} from './test' 

import {
  getMe
} from '../vuex/actions'

import {
  USER_SET_INFO,
  USER_SET_ID
} from '../vuex/mutation-types'

export default {
  name: 'usrModify',
  components: {

  },
  data: function(){
    return {
      'name': '',
      'phone': '',
      'email': '',
      'description': '',
      'modalmessage': '',
    }
  },
  vuex: {
    getters: {
      userid: state => state.user.data.openid,
    },
    actions: {
      modifyUsrInfo: function({dispatch}, data) {
        let _this = this;
        $.ajax({
          type: "post",
          url: '/api/userinfo/modify',
          data: JSON.stringify({
            'name': _this.name,
            'email': _this.email,
            'mobile': _this.phone,
            'introduction': _this.description
          }),
          contentType: 'application/json;charset=utf-8',
          success: function(res){
            window.location.href = "#!/user/" + _this.userid;
          },
          error: function(res) {
          }
        })
      },
      getInfo: function({dispatch}) {
        let _this = this;
        $.get("/api/userinfo/detail?user_id=" + _this.userid).done(function(res) {
          _this.name = JSON.parse(res).name;
          _this.email = JSON.parse(res).email;
          _this.phone = JSON.parse(res).mobile;
          _this.description = JSON.parse(res).introduction;
          console.log(res);
        }).fail(function(res) {
          console.log(res);
        });
      },
      getMe,
    }
  },
  ready: function () {
    this.getMe();
    this.getInfo();
    $('.alert-modal').css('display', 'none');
    $('#fileUploadBtn').on('change', function () {
      if (this.files.length > 0) {
        var form = new FormData();
        var f = this.files[0];
        //console.log(this.files);
        form.append('image', this.files[0]);
        $.ajax({
          type: 'post',
          url: '/api/userinfo/upload',
          data: form,
          processData: false,
          contentType: false,
          success: function (res) {
            $('#input-pic_url').val(f.name);
          }
        })
      }
    });
  },
  methods: {
    submit: function () {
      if(!this.name) {
        this.modalmessage = '昵称不能为空！'
        $('.alert-modal').css('display', 'inline');
        return
      }
      else if(!this.phone) {
        this.modalmessage = '手机不能为空！'
        $('.alert-modal').css('display', 'inline');
        return
      }
      else if(!this.email) {
        this.modalmessage = '邮箱不能为空！'
        $('.alert-modal').css('display', 'inline');
        return
      }
      this.modifyUsrInfo({
        'name': this.name,
        'phone': this.phone,
        'email': this.email,
        'description': this.description
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
