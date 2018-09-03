import axios from 'axios'
import store from '../store/index'
import router from '../router/index'
// import router from '../router/index'

axios.defaults.timeout = 5000

// http request 拦截器
axios.interceptors.request.use(
  config => {
    if (store.state.token) {
      config.headers.Authorization = `JWT ${store.state.token}`
    }
    return config
  },
  err => {
    return Promise.reject(err)
  }
)

// http response 拦截器
// http response 拦截器
axios.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error.response) {
      switch (error.response.status) {
        case 401:
          localStorage.removeItem('token')
          localStorage.removeItem('username')
          router.replace({
            path: 'login',
            query: {redirect: router.currentRoute.fullPath}
          })
      }
    }
    return Promise.reject(error.response.data)
  }
)

export default axios
