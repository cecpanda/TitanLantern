// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store/index'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import cookie from '../static/cookie'

Vue.config.productionTip = false

Vue.use(ElementUI)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
  methods: {
    checkLogin () {
      if (!cookie.getCookie('token')) {
        this.$router.push({name: 'Login'})
      } else {
        this.$router.push({name: 'Home'})
      }
    }
  },
  created () {
    this.checkLogin()
  },
  watch: {
    '$route': 'checkLogin'
  }
})
