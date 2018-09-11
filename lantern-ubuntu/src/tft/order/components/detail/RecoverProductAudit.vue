<template>
  <div class='audit'>
    <!-- <span @click='visible = true' class='visible'>
      <i class="el-icon-star-off"></i>点
      <i class="el-icon-star-off"></i>这
      <i class="el-icon-star-off"></i>里
    </span> -->
    <el-button type="success" size='mini' @click='visible = true'>点击这里</el-button>
    <el-dialog title="复机审核 - 生产" :visible.sync="visible">
      <div>准奏</div>
      <div slot="footer" class="dialog-footer">
        <el-button @click="visible = false">取 消</el-button>
        <el-button type="primary" @click="add">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { recoverProductAudit } from '@/api/tft'

export default {
  name: 'RecoverProductAudit',
  props: {
    recoverorder: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      visible: false
    }
  },
  methods: {
    add () {
      let params = {id: this.recoverorder.id}
      recoverProductAudit(params)
        .then((res) => {
          this.$notify({
            title: '成功',
            message: '复机 - 生产审核成功',
            type: 'success'
          })
          this.visible = false
          this.$emit('change')
        })
        .catch((err) => {
          console.log(err)
          this.$notify({
            title: '错误',
            message: err,
            type: 'error'
          })
          this.visible = false
        })
    }
  }
}
</script>

<style lang='stylus'>
// .el-dialog
//   box-shadow 10px 10px 5px #888888
//   background rgba(255, 255, 255, 0.1)
</style>
