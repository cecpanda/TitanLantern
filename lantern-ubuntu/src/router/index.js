import Vue from 'vue'
import store from '@/store/index'
import Router from 'vue-router'
import Home from '@/home/Home'
import Login from '@/home/Login'
import User from '@/user/User'
import Action from '@/user/components/Action'
import Edit from '@/user/components/Edit'
import Follow from '@/user/components/Follow'
import ChangePassword from '@/user/components/ChangePassword'
import Order from '@/tft/Order'
import Summary from '@/tft/components/Summary'
import StartOrder from '@/tft/components/Start'
import MyStart from '@/tft/components/MyStart'
import AuditOrder from '@/tft/components/Audit'
// import { jwtVerify } from '@/api/user'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    }, {
      path: '/login',
      name: 'Login',
      component: Login
    }, {
      path: '/user',
      component: User,
      meta: {
        requireAuth: true
      },
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
          component: StartOrder,
          meta: {
            requireAuth: true
          }
        }, {
          path: 'mystart',
          component: MyStart,
          meta: {
            requireAuth: true
          }
        }, {
          path: 'audit',
          component: AuditOrder
        }
      ]
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(r => r.meta.requireAuth)) {
    if (store.state.token) {
      next()
    } else {
      next({
        path: '/login',
        query: {redirect: to.fullPathh}
      })
    }
  } else {
    next()
  }
})

export default router
