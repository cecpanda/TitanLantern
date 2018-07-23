<template>
  <el-container>
    <el-header>
      <HomeHeader></HomeHeader>
    </el-header>
    <router-view/>
    <el-footer>Footer</el-footer>
  </el-container>
</template>

<script>
import HomeHeader from './home/Header'

export default {
  name: 'Home',
  components: {
    HomeHeader
  }
}
</script>

<style lang='stylus' scoped>
.el-header
  color: #333
  text-align: center
  line-height: 60px
  position relativce
  margin-bottom 20px
.el-footer
  text-align: center
  margin-top 20px
  border 1px solid green
// .el-main
//   background-color: #E9EEF3
//   color: #333
//   text-align: center
//   line-height: 160px
//   border 1px solid red
// .el-aside
//   background-color: #D3DCE6
//   color: #333
//   text-align: center
//   line-height: 200px
//   border 1px solid red
</style>
