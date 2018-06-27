import cookie from '../../static/cookie'

export default {
  name: cookie.getCookie('name') || '',
  token: cookie.getCookie('token') || ''
}
