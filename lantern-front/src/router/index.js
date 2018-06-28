import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/home/Home'
import Login from '@/user/Login'
import Logout from '@/user/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/logout',
      name: 'Logout',
      component: Logout
    }
  ]
})
