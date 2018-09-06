<template>
  <div>
    <span @click='visible = true'>
      <i class="el-icon-star-off"></i>
      <i class="el-icon-star-off"></i>
      <i class="el-icon-star-off"></i>
    </span>
    <el-dialog :title="'责任工程审核 - ' + groupName" :visible.sync="visible">
      <el-form :model='chargeAudit' :rules='chargeRules' ref='chargeForm'>
        <el-form-item label="是否拒签" prop='rejected' label-width='20%'>
          <el-radio v-model="chargeAudit.rejected" :label="true">是</el-radio>
          <el-radio v-model="chargeAudit.rejected" :label="false">否</el-radio>
        </el-form-item>
        <el-form-item label="拒签理由" prop='reason' label-width='20%'>
          <el-input
            type='textarea'
            :rows='4'
            v-model="chargeAudit.reason"
            placeholder='不能超过 100 字符'
          ></el-input>
          拒签时必填
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="visible = false">取 消</el-button>
        <el-button type="primary" @click="addChargeAudit">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { chargeAudit } from '@/api/tft'

export default {
  name: 'ChargeAudit',
  props: {
    order: {
      required: true
    },
    groupName: {}
  },
  data () {
    return {
      visible: false,
      chargeAudit: {
        rejected: false,
        reason: ''
      },
      chargeRules: {
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
    addChargeAudit () {
      this.$refs['chargeForm'].validate((valid) => {
        if (valid) {
          let params = {
            order: this.order,
            rejected: this.chargeAudit.rejected
          }
          if (params.rejected) {
            params.reason = this.chargeAudit.reason
          }
          chargeAudit(params)
            .then((res) => {
              this.$notify({
                title: '成功',
                message: '责任工程审核成功',
                type: 'success'
              })
              this.chargeAudit = {rejected: false, reason: ''}
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
              this.chargeAudit = {rejected: false, reason: ''}
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
