<template>
  <el-menu
      :default-active="activeIndex"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <el-menu-item index="1">首页</el-menu-item>
      <el-submenu index="2">
        <template slot="title">TFT</template>
        <el-menu-item index="2-1">停机单</el-menu-item>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">LCD</template>
        <el-menu-item index="3-1">1</el-menu-item>
        <el-menu-item index="3-2">2</el-menu-item>
        <el-submenu index="3-3">
          <template slot="title">3</template>
          <el-menu-item index="3-3-1">选项1</el-menu-item>
          <el-menu-item index="3-3-2">选项2</el-menu-item>
          <el-menu-item index="3-3-3">选项3</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-menu-item index="4">SL</el-menu-item>
      <el-menu-item index="5" disabled>禁止</el-menu-item>
      <el-menu-item index="6" class='user'>
        <User/>
      </el-menu-item>
      <el-menu-item index="7" class='login'>
        <Login/>
      </el-menu-item>
    </el-menu>
</template>

<script>
import { mapGetters } from 'vuex'
import Login from './Login'
import User from './User'

export default {
  name: 'HomeHeader',
  components: {
    Login,
    User
  },
  data () {
    return {
      activeIndex: '1'
    }
  },
  computed: {
    ...mapGetters({
      isLogin: 'isLogin',
      username: 'username'
    })
  },
  methods: {
    handleSelect (key, keyPath) {
    }
  }
}
</script>

<style lang='stylus' scoped>
.login
  position absolute
  right 20px
</style>
