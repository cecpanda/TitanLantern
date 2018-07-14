<!-- <template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
/*#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}*/
</style> -->

<template>
  <div class="app">
    <el-container>
      <el-header>
        <HomeHeader></HomeHeader>
      </el-header>
      <!--
      <el-container>
        <el-main>
          Main <br/>
          <br/><br/><br/>
        </el-main>
        <el-aside width="200px">Aside</el-aside>
      </el-container>
      -->
      <router-view/>
      <el-footer>Footer</el-footer>
    </el-container>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import HomeHeader from './home/Header'

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
.el-footer
  margin-top 50px
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
