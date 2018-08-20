<template>
  <el-menu
      :default-active="activeIndex"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      :router='true'
    >
      <el-menu-item index="/">首页</el-menu-item>
      <el-submenu index="2">
        <template slot="title">TFT</template>
        <el-menu-item index="/tft/order">停机单</el-menu-item>
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
      <el-submenu index="6" class='login' v-if='isLogin && username'>
        <template slot="title">
          <img :src="user.avatar" /> &nbsp;
          {{ username }}
        </template>
        <el-menu-item index="/user">个人中心</el-menu-item>
        <el-menu-item index="6-2">设置中心</el-menu-item>
        <el-menu-item index="6-3" @click='logout'>退出</el-menu-item>
      </el-submenu>
      <el-menu-item index="7" class='login' v-else>
        <Login></Login>
      </el-menu-item>
    </el-menu>
</template>

<script>
import { getUser } from '@/api/user'
import { mapGetters } from 'vuex'
import Login from './Login'

export default {
  name: 'HomeHeader',
  components: {
    Login
  },
  data () {
    return {
      activeIndex: '1',
      user: {}
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
      console.log(key, keyPath)
    },
    getUser () {
      getUser(this.username)
        .then((res) => {
          this.user = res.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    logout () {
      localStorage.removeItem('token')
      localStorage.removeItem('username')
      // 记得加上啊，更新全局状态
      this.$store.commit('setInfo')
      this.$router.push({name: 'Home'})
    }
  },
  watch: {
    // 否则，在登录后，不进行信息查询。
    // 在 updated 中执行，容易四循环
    isLogin (val, oldVal) {
      this.getUser()
    }
  },
  mounted () {
    this.getUser()
  }
}
</script>

<style lang='stylus' scoped>
.login
  position absolute
  right 20px
  img
    width 35px
    height 35px
</style>
