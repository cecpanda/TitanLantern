// import axios from 'axios'
import axios from './http'
import conf from './config'

let host = conf.host

// 登录
export const jwtAuth = (username, password) => {
  return axios.post(`${host}/jwt/auth/`, {
    username: username,
    password: password
  }, {
    headers: {'Content-Type': 'application/json'}
  })
}

// 验证 token 还有效不
export const jwtVerify = token => {
  return axios.post(`${host}/jwt/verify/`, {token: token}, {
    headers: {
      'Content-Type': 'application/json'
    }
  })
}

// 获取所有用户
// export const getAllUsers = (page, pageSize) => {
//   return axios.get(`${host}/account/user/?page=${page}&page-size=${pageSize}`)
// }

export const getAllUsers = (page, pageSize) => {
  return axios.get(`${host}/account/user/`, {
    params: {
      page: page,
      'page-size': pageSize
    }
  })
}

// 获取关注列表
export const getFollowing = (username) => {
  return axios.get(`${host}/account/user/${username}/following/`)
}

// 关注
export const follow = (username) => {
  return axios.post(`${host}/account/follow/`, {
    user_to: username
  })
}

// 取消关注
export const unfollow = (username) => {
  return axios.post(`${host}/account/follow/unfollow/`, {
    user_to: username
  })
}

// 关注列表
export const following = (username, page, pageSize) => {
  return axios.get(`${host}/account/user/${username}/following/`, {
    params: {
      page: page,
      'page-size': pageSize
    }
  })
}

// 被关注列表
export const followers = (username, page, pageSize) => {
  return axios.get(`${host}/account/user/${username}/followers/`, {
    params: {
      page: page,
      'page-size': pageSize
    }
  })
}

// 判断关注状态
export const followStatus = (userFrom, userTo) => {
  return axios.get(`${host}/account/user/follow-status/`, {
    params: {
      user_from: userFrom,
      user_to: userTo
    }
  })
}

// 获取指定用户资料
export const getUser = username => {
  return axios.get(`${host}/account/user/${username}`, {
    headers: {
      'Content-Type': 'application/json'
    }
  })
}

// 查询所有组
export const getAllGroups = () => {
  return axios.get(`${host}/account/group/`)
}

// 修改资料
export const changeProfile = (params) => {
  return axios.put(`${host}/account/user/change-profile/`, params)
}

// 修改密码
export const changePassword = (oldPassword, newPassword) => {
  return axios.post(`${host}/account/user/change-password/`, {
    old_password: oldPassword,
    new_password: newPassword
  })
}

// timeline
export const getAction = (page, pageSize) => {
  return axios.get(`${host}/action/?page=${page}&page-size=${pageSize}`)
}
