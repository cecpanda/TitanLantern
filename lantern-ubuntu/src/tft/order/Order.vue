<template>
  <el-container>
    <el-main>
      <router-view></router-view>
    </el-main>
    <el-aside width="">
      <el-menu
        class="el-menu-vertical-demo"
        @select="handleSelect"
        @open="handleOpen"
        @close="handleClose"
        :collapse="isCollapse"
        :router='true'
      >
        <el-menu-item index="/tft/order/start">
          <i class='el-icon-edit'></i>
          <span slot="title">
            我要开单
          </span>
        </el-menu-item>

        <el-submenu index="3">
          <template slot="title">
            <i class='el-icon-star-on'></i>
            <span slot="title">
              待我审核<el-badge :value="sum" :max="99"></el-badge>
            </span>
          </template>
          <el-menu-item index="/tft/order/to-audit">
            停机审核<el-badge :value="start" :max="99"></el-badge>
          </el-menu-item>
          <el-menu-item index="/tft/order/to-recover-audit">
            复机审核<el-badge :value="recover" :max="99"></el-badge>
          </el-menu-item>
        </el-submenu>

        <el-submenu index="/tft/order/query" class='query'>
          <template slot="title">
            <router-link to='/tft/order/query'>
              <i class="el-icon-document"></i>
              <span>报表查询</span>
            </router-link>
          </template>
          <el-menu-item index="/tft/order/mystart">我的停机单</el-menu-item>
          <el-menu-item index="/tft/order/myrecover">我的复机单</el-menu-item>
          <el-menu-item index="/tft/order/mystartaudit">停机审核单</el-menu-item>
          <el-menu-item index="/tft/order/myrecoveraudit">复机审核单</el-menu-item>
        </el-submenu>

        <el-menu-item index="/tft/order">
          <i class='el-icon-picture-outline'></i>
          <span slot="title">图表统计</span>
        </el-menu-item>

        <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
          <el-radio-button :label="false" v-if='isCollapse'>
            <i class='el-icon-d-arrow-left'></i>
          </el-radio-button>
          <el-radio-button :label="true" v-else>
            <i class='el-icon-d-arrow-right'></i>
          </el-radio-button>
        </el-radio-group>
      </el-menu>
    </el-aside>
  </el-container>
</template>

<script>
import { mapGetters } from 'vuex'
import { getOrders, getRecoverOrders } from '@/api/tft'
import { getUser } from '@/api/user'

export default {
  name: 'Order',
  data () {
    return {
      isCollapse: true,
      defaultActive: '',
      activeMenu: '',
      group: {},
      start: null,
      recover: null
    }
  },
  computed: {
    ...mapGetters({
      username: 'username'
      // start: 'start',
      // recover: 'recover'
    }),
    sum () {
      return this.start + this.recover
    }
  },
  methods: {
    handleSelect (index, indexPath) {
    },
    handleOpen (key, keyPath) {
    },
    handleClose (key, keyPath) {
    },
    async getGroup () {
      await getUser(this.username)
        .then((res) => {
          // 只要第一个组
          let groups = res.data.groups
          if (groups.length) {
            this.group = groups[0]
          } else {
            this.group = {}
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    async getStart () {
      await this.getGroup()
      let params
      if (this.group.name === 'MFG') {
        params = {status: 1}
      } else if (this.group.name) {
        params = {status: 2, charge_group: this.group.name}
      }
      if (params) {
        getOrders(params)
          .then((res) => {
            this.start = res.data.count
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    async getRecover () {
      await this.getGroup()
      let params
      if (this.group.name === 'QC') {
        params = {order__status: 5}
      } else if (this.group.name === 'MFG') {
        params = {order__status: 6, charge_group: this.group.name}
      }
      if (params) {
        getRecoverOrders(params)
          .then((res) => {
            this.recover = res.data.count
          })
          .catch((err) => {
            console.log(err)
          })
      }
    }
  },
  mounted () {
    this.getStart()
    this.getRecover()
  }
}
</script>

<style lang='stylus' scoped>
.active-menu
  font-size 0.9rem
.el-main
.el-aside
  border 1px dashed #283D52
  min-height 550px
.el-menu-vertical-demo:not(.el-menu--collapse)
  width: 200px
.query
  a
    text-decoration none
    color #333
</style>
