<template>
  <div>
    <span @click='visible = true'>
      <i class="el-icon-star-off"></i>
      <i class="el-icon-star-off"></i>
      <i class="el-icon-star-off"></i>
    </span>
    <el-dialog title="复机审核 - QC" :visible.sync="visible">
      <el-form :model='audit' :rules='rules' ref='form'>
        <el-form-item label="是否拒签" prop='rejected' label-width='20%'>
          <el-radio v-model="audit.rejected" :label="true">是</el-radio>
          <el-radio v-model="audit.rejected" :label="false">否</el-radio>
        </el-form-item>
        <el-form-item label="拒签理由" prop='reason' label-width='20%'>
          <el-input
            type='textarea'
            :rows='4'
            v-model="audit.reason"
            placeholder='不能超过 100 字符'
          ></el-input>
          拒签时必填
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
import { recoverQcAudit } from '@/api/tft'

export default {
  name: 'RecoverQcAudit',
  props: {
    recoverorder: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      visible: false,
      audit: {
        rejected: false,
        reason: ''
      },
      rules: {
        rejected: [
          { required: true, message: '是否拒签', trigger: 'blur' }
        ],
        reason: [
          { min: 1, max: 100, message: '长度在 1 到 100 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    add () {
      this.$refs['form'].validate((valid) => {
        if (valid) {
          let params = {
            id: this.recoverorder.id,
            rejected: this.audit.rejected
          }
          if (params.rejected) {
            params.reason = this.audit.reason
          }
          recoverQcAudit(params)
            .then((res) => {
              this.$notify({
                title: '成功',
                message: '复机 - QC 审核成功',
                type: 'success'
              })
              this.audit = {rejected: false, reason: ''}
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
              this.audit = {rejected: false, reason: ''}
              this.visible = false
            })
        }
      })
    }
  }
}
</script>

<style lang='stylus' scoped>

</style>
