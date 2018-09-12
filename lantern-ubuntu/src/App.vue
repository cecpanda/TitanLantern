<template>
  <el-container>
    <el-header>
      <HomeHeader></HomeHeader>
    </el-header>
    <router-view/>
    <el-footer>
      Copyright © 2010-2020, Cecpandalcd, All Rights Reserved.
    </el-footer>
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
  text-align center
  line-height 60px
  position relativce
  margin-bottom 20px
.el-footer
  height 50px
  line-height 50px
  text-align center
  margin-top 25px
  // border 1px solid green
  background-color #CFE0F1
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
