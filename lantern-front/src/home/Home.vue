<template>
  <el-container>
    <el-main>
      Main <br/><br/><br/><br/>
    </el-main>
    <el-aside width="200px">Aside</el-aside>
  </el-container>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style lang='stylus' scoped>
.el-main
  background-color: #E9EEF3
  color: #333
  text-align: center
  line-height: 160px
  border 1px solid red
.el-aside
  background-color: #D3DCE6
  color: #333
  text-align: center
  line-height: 200px
  border 1px solid red
</style>
