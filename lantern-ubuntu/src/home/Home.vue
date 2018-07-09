<template>
  <div class='home'>
    <el-container>
      <el-header>Header</el-header>
      <el-main>Main</el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'Home'
}

</script>

<style lang='stylus' scoped>
.el-header
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
.el-main
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 160px;
</style>
