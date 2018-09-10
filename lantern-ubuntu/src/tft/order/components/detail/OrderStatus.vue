<template>
  <el-button type='info'>{{ status }}</el-button>
</template>

<script>
export default {
  name: 'OrderStatus',
  props: ['order', 'status']
}
</script>

<style lang='stylus' scoped>

</style>
