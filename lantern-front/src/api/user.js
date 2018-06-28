import axios from 'axios'
import conf from './config'

let host = conf.host

// 登录
export const jwtAuth = params => {
  return axios.post(`${host}/jwt-auth/`, params)
}

// 验证 token 还有效不
export const jwtAuthVerify = params => {
  return axios.post(`${host}/jwt-token-verify/`, params, {
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then((response) => {
      return true
    })
    .catch((error) => {
      console.log(error)
      return false
    })
}
