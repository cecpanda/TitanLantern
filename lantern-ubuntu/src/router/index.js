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
import Order from '@/tft/order/Order'
import Summary from '@/tft/order/components/Summary'
import StartOrder from '@/tft/order/components/Start'
import UpdateOrder from '@/tft/order/components/Update'
import MyStart from '@/tft/order/components/MyStart'
import AuditOrder from '@/tft/order/components/Audit'
import Detail from '@/tft/order/components/Detail'
import Query from '@/tft/order/components/Query'
import Wiget from '@/widgets/index'
import Clock from '@/widgets/Clock'
import Panda from '@/widgets/Panda'
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
          path: 'update/:id',
          component: UpdateOrder,
          props: true,
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
        }, {
          path: 'detail/:id',
          component: Detail,
          props: true
        }, {
          path: 'query',
          component: Query
        }
      ]
    }, {
      path: '/widget',
      component: Wiget,
      children: [
        {
          path: 'clock',
          component: Clock
        }, {
          path: 'panda',
          component: Panda
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
