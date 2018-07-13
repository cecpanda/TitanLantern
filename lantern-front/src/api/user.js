import axios from 'axios'
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
    .then((response) => {
      return true
    })
    .catch((error) => {
      console.log(error)
      return false
    })
}
