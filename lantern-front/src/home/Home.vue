<template>
  <el-menu
    :default-active="activeIndex2"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b">
    <el-menu-item index="1">首页</el-menu-item>
    <el-submenu index="2">
      <template slot="title">TFT</template>
      <el-menu-item index="2-1">Hold-Lot</el-menu-item>
    </el-submenu>
    <el-submenu index="3">
      <template slot="title">LCD</template>
      <el-menu-item index="3-1">选项1</el-menu-item>
      <el-menu-item index="3-2">选项2</el-menu-item>
      <el-menu-item index="3-3">选项3</el-menu-item>
      <el-submenu index="3-4">
        <template slot="title">选项4</template>
        <el-menu-item index="3-4-1">选项1</el-menu-item>
        <el-menu-item index="3-4-2">选项2</el-menu-item>
        <el-menu-item index="3-4-3">选项3</el-menu-item>
      </el-submenu>
    </el-submenu>
    <el-menu-item index="4" disabled>SL</el-menu-item>
    <el-menu-item index="5">登录</el-menu-item>
  </el-menu>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style lang='stylus' scoped>
</style>
