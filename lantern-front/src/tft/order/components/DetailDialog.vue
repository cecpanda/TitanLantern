<template>
  <el-dialog title="外层 Dialog">
    <el-dialog
      width="30%"
      title="内层 Dialog"
      append-to-body>
    </el-dialog>
    <div slot="footer" class="dialog-footer">
      <el-button @click="outerVisible = false">取 消</el-button>
    </div>
  </el-dialog>
</template>

<script>
export default {
  name: 'DetailDialog',
  props: {
  },
  data () {
    return {
    }
  }
}
</script>

<script lang='stylus' scoped>

</script>
