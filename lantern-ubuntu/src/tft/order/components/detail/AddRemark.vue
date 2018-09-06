<template>
  <div id='add-remark'>
    <i class="el-icon-plus" @click='visible = true'></i>
    <el-dialog title="添加批注" :visible.sync="visible">
      <el-form :model='remark' :rules='rules' ref='form'>
        <el-form-item label="" prop='content'>
          <el-input
            type='textarea'
            :rows='5'
            v-model="remark.content"
            placeholder='批注内容'
          ></el-input>
          不能超过 500 字符
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="visible = false">取 消</el-button>
        <el-button type="primary" @click="add">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { addRemark } from '@/api/tft'

export default {
  name: 'AddRemark',
  props: {
    order: {
      required: true
    }
  },
  data () {
    return {
      visible: false,
      remark: {
        content: ''
      },
      rules: {
        content: [
          { required: true, message: '请输入批注内容', trigger: 'blur' },
          { min: 1, max: 500, message: '长度在 1 到 500 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    add () {
      this.$refs['form'].validate((valid) => {
        if (valid) {
          addRemark(this.order, this.remark.content)
            .then((res) => {
              this.$notify({
                title: '成功',
                message: '添加成功',
                type: 'success'
              })
              this.remark.content = ''
              this.visible = false
              // 触发事件，使父组件重新获取 order
              // this.getOrder()
              this.$emit('change')
            })
            .catch((err) => {
              this.$notify({
                title: '错误',
                message: err,
                type: 'error'
              })
              this.remark.content = ''
              this.visible = false
            })
        }
      })
    }
  }
}
</script>

<style lang='stylus'>
#add-remark
  display inline
.el-dialog
  text-align left
</style>
