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
