<template>
  <el-menu
    :default-active="activeIndex2"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
  >
    <el-menu-item index="1">首页</el-menu-item>
    <el-submenu index="2">
      <template slot="title">TFT</template>
      <el-menu-item index="2-1">Hold Lot</el-menu-item>
      <el-menu-item index="2-2">选项2</el-menu-item>
      <el-submenu index="2-3">
        <template slot="title">选项3</template>
        <el-menu-item index="2-3-1">选项1</el-menu-item>
        <el-menu-item index="2-3-2">选项2</el-menu-item>
        <el-menu-item index="2-3-3">选项3</el-menu-item>
      </el-submenu>
    </el-submenu>
    <el-submenu index="3">
      <template slot="title">LCD</template>
      <el-menu-item index="3-1">选项1</el-menu-item>
      <el-menu-item index="3-2">选项2</el-menu-item>
    </el-submenu>
    <el-menu-item index="4" disabled>SL</el-menu-item>
    <el-menu-item index="5">
      <template v-if='isLogged'>
        <router-link to='' >用户信息</router-link>
        <router-link to='/logout'>退出</router-link>
      </template>
      <router-link to='/login' v-else>登录</router-link>
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1',
      isLogged: this.$store.state.isLogged
    }
  },
  computed: {
  },
  methods: {
    handleSelect (key, keyPath) {
      this.$store.dispatch('setTest', 'hehe')
    },
    logOut () {
      localStorage.removeItem('token')
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
</style>
