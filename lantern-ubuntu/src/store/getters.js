// import { jwtVerify } from '@/api/user'
import base64 from 'js-base64'

export default {
  isLogin: state => {
    // jwtVerify(state.token)
    //   .then((response) => {

    //   }).catch((err) => {
    //     console.log(err)
    //   })
    if (state.token) {
      return true
    }
    return false
  },
  username: state => {
    let userInfo = JSON.parse(base64.Base64.decode(state.token.split('.')[1]))
    return state.username || userInfo.username
  }
}
