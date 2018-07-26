import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/home/Home'
// import Action from '@/user/Action'
import User from '@/user/User'
import Action from '@/user/components/Action'
import Edit from '@/user/components/Edit'
import Follow from '@/user/components/Follow'
import ChangePassword from '@/user/components/ChangePassword'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
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
        }, {
          path: 'follow',
          component: Follow
        }, {
          path: 'change-password',
          component: ChangePassword
        }
      ]
    }
  ]
})
