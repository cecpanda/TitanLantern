import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/home/Home'
// import Action from '@/user/Action'
import User from '@/user/User'
import Users from '@/user/Users'
import Action from '@/user/components/Action'
import Edit from '@/user/components/Edit'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    }, {
      path: '/users',
      name: 'Users',
      component: Users
    }, {
      path: '/user',
      component: User,
      children: [
        {
          path: '',
          component: Action
        }, {
          path: 'edit',
          component: Edit
        }
      ]
    }
  ]
})
