import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/home/Home'
import User from '@/user/User'
import Action from '@/user/components/Action'
import Edit from '@/user/components/Edit'
import Follow from '@/user/components/Follow'
import ChangePassword from '@/user/components/ChangePassword'
import Order from '@/tft/Order'
import Summary from '@/tft/components/Summary'
import StartOrder from '@/tft/components/Start'
import AuditOrder from '@/tft/components/Audit'

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
    }, {
      path: '/tft/order',
      component: Order,
      children: [
        {
          path: '',
          component: Summary
        }, {
          path: 'start',
          component: StartOrder
        }, {
          path: 'audit',
          component: AuditOrder
        }
      ]
    }
  ]
})
