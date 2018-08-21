<template>
  <div>
    <el-button type="text" @click="dialogVisible=true">{{ id }}</el-button>
    <!-- <span @click="dialogVisible=true">{{ id }}</span> -->
    <el-dialog
      :title="id"
      :visible.sync="dialogVisible"
      width="95%"
    >
      <span>{{ id }}</span><br>
      <span>{{ id }}</span><br>
      <span>{{ id }}</span><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
      <span>{{ id }}</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible=false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible=false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'DetailDialog',
  props: ['id', 'visible'],
  data () {
    return {
      // dialogVisible: this.visible
      dialogVisible: false
    }
  },
  methods: {
    handleClose () {
    }
  }
}
</script>

<style lang='stylus' scoped>

</style>
