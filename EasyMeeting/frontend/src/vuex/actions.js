import {
  MAIN_TITLE_CHANGE,
  USER_SET_ID,
  USER_SET
} from './mutation-types'

const default_img = ""

function parseTime(number) {
  let str = number+''
  if(str.length == 1) {
    str = '0'+ str
  }
  return str
}

export function getUserInfo(openid) {
    $.get('')
}

export function changeMainTitle({dispatch}, title) {
  dispatch(MAIN_TITLE_CHANGE, title)
}

export function getTimeStamp(date, time) {
  let dateList = date.split('/')
  let timeList = time.split(':')
  let dateObj = new Date(parseInt(dateList[0]), parseInt(dateList[1])-1, parseInt(dateList[2]), parseInt(timeList[0]), parseInt(timeList[1]), 0)
  return dateObj.getTime()
}

export function getTimeString(timeStamp) {
  let dateObj = new Date(parseInt(timeStamp))
  return {
    date: dateObj.getFullYear() + '/' + parseTime(dateObj.getMonth()+1) + '/' + parseTime(dateObj.getDate()),
    time: parseTime(dateObj.getHours()) + ':' + parseTime(dateObj.getMinutes())
  }
}

export function getMe({dispatch}) {
  $.get("/api/userinfo/getme").done(function(res) {
    let id = JSON.parse(res).id
    if(id == 0) {
      window.location.href = "/index/#!/"
    }
    else {
      dispatch(USER_SET_ID, id);
      dispatch(USER_SET, JSON.parse(res))
    }
  }).fail(function(res) {
    console.log(res);
  });
}

export function createActList(resData) {
  let actList = []
  let start = "", end = ""
  for (let i = 0; i < resData.length; i ++) {
    let act = {}
    start = getTimeString(parseInt(resData[i].start_time))
    end = getTimeString(parseInt(resData[i].end_time))

    act.id = resData[i].ID
    act.title = resData[i].name
    act.host = resData[i].host
    act.startTime = parseInt(resData[i].start_time)
    act.endTime = parseInt(resData[i].end_time)
    act.time = start.date + ' ' + start.time + ' 至 ' + end.date  + ' ' + end.time
    act.place = resData[i].loc
    act.members = resData[i].member_maxcount
    act.passed = resData[i].member_passed_count
    act.brief = resData[i].brief_desc
    act.info = resData[i].desc
    act.type = resData[i].type
    if(resData[i].image == '' || resData[i].image == null) {
      act.image = default_img
    }
    else {
      act.image = resData[i].image
    }
    act.creator = {
      'id': resData[i].uID,
      'name': resData[i].uName,
      'avatar': resData[i].uAvator,
    }
    act.contact = resData[i].contact

    actList.push(act)
  }
  return actList
}