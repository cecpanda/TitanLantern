<template>
  <el-container>
    <el-main>
      Maindfsd
    </el-main>
    <el-aside width="200px">
      aside
    </el-aside>
  </el-container>
</template>

<script>
import HomeHeader from './Header'

export default {
  name: 'Home',
  components: {
    HomeHeader
  }
}
</script>

<style lang='stylus' scoped>
.el-main
  height 620px
  background-color: #E9EEF3
  color: #333
  text-align: center
  // line-height: 160px
  border 1px solid red
.el-aside
  background-color: #D3DCE6
  color: #333
  text-align: center
  border 1px solid red
</style>
