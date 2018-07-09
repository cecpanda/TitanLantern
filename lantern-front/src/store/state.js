// import cookie from '../../static/cookie'

// export default {
//   name: cookie.getCookie('name') || '',
//   token: cookie.getCookie('token') || ''
// }
import { jwtAuthVerify } from '../api/user'

const checkLogin = () => {
  let token = localStorage.getItem('token') || ''
  if (!token.length) {
    return false
  }
  return jwtAuthVerify(token)
}

export default {
  // name: localStorage.name || '',
  isLogged: checkLogin(),
  test: 'woca'
}
