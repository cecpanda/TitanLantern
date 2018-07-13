<template>
<el-container>
  <el-header>
    <HomeHeader></HomeHeader>
  </el-header>
  <el-container>
    <el-main>
      Main <br/>
      <br/><br/><br/>
    </el-main>
    <el-aside width="200px">Aside</el-aside>
  </el-container>
  <el-footer>Footer</el-footer>
</el-container>
</template>

<script>
import { mapGetters } from 'vuex'
import HomeHeader from './components/Header'

export default {
  name: 'Home',
  computed: {
    ...mapGetters({
      isLogin: 'isLogin',
      username: 'username'
    })
  },
  components: {
    HomeHeader
  }
}
</script>

<style lang='stylus' scoped>
.el-header, .el-footer
  color: #333
  text-align: center
  line-height: 60px
  position relativce

.el-main
  background-color: #E9EEF3
  color: #333
  text-align: center
  line-height: 160px
.el-aside
  background-color: #D3DCE6
  color: #333
  text-align: center
  line-height: 200px
</style>
