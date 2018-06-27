import axios from 'axios'

let host = 'http://127.0.0.1:8000'

// 登录
export const login = params => {
  return axios.post(`${host}/jwt-auth/`, params)
}

// 验证 token 还有效不

export const loginVerify = params => {
  axios.post(`${host}/jwt-auth-verify/`, params, {
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then((response) => {
      console.log(response.data)
      return true
    })
    .catch((error) => {
      console.log(error)
      return false
    })
}
