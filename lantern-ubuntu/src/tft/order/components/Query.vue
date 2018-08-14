<template>
  <div>
    <el-row>
      <el-col :span='6'>
        <el-col :span='6'>
        </el-col>
        <el-col :span='6'>
        </el-col>
        <el-col :span='6'>
        </el-col>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'Query'
}
</script>

<style lang='stylus' scoped>
.el-col
  border 1px solid red
  min-height 30px
</style>
