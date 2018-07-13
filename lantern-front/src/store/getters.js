import { jwtVerify } from '@/api/user'

export default {
  isLogin: state => {
    return jwtVerify(state.token)
  },
  username: state => {
    return state.username
  }
}
