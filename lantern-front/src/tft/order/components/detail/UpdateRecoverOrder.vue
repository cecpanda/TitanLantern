<template>
  <div>
    <el-button
      type='warning'
      icon='el-icon-edit'
      @click='visible = true'
    >
      修改
    </el-button>
    <el-dialog title="申请复机" :visible.sync="visible" width='68%'>
      <el-form :model='recoverOrder' :rules='recoverOrderRules' ref='form'>
        <el-form-item label="责任单位对策说明" prop='solution' label-width='15%'>
          <el-input
            type='textarea'
            :rows='3'
            v-model="recoverOrder.solution"
            placeholder='不能超过 200 字符'
          ></el-input>
        </el-form-item>
        <el-form-item label="先行lot结果说明" prop='explain' label-width='15%'>
          <el-input
            type='textarea'
            :rows='3'
            v-model="recoverOrder.explain"
            placeholder='不能超过 200 字符'
          ></el-input>
        </el-form-item>
        <el-form-item label="是否部分复机" prop='partial' label-width='15%'>
          <el-radio v-model="recoverOrder.partial" :label="true">是</el-radio>
          <el-radio v-model="recoverOrder.partial" :label="false">否</el-radio>
        </el-form-item>
        <el-form-item label="部分复机设备" prop='eq' label-width='15%'>
          <el-input v-model="recoverOrder.eq" placeholder='不能超过 50 字符'></el-input>
          <span class='tip'>部分复机时必填, 否则被忽略</span>
        </el-form-item>
        <el-form-item label="部分复机机种" prop='kind' label-width='15%'>
          <el-input v-model="recoverOrder.kind" placeholder='不能超过 30 字符'></el-input>
          <span class='tip'>部分复机时必填, 否则被忽略</span>
        </el-form-item>
        <el-form-item label="部分复机站点" prop='step' label-width='15%'>
          <el-input v-model="recoverOrder.step" placeholder='不能超过 50 字符'></el-input>
          <span class='tip'>部分复机时必填, 否则被忽略</span>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="visible = false">取 消</el-button>
        <el-button type="primary" @click="updateRecoverOrder">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { updateRecoverOrder } from '@/api/tft'

export default {
  name: 'UpdateRecoverOrder',
  props: {
    recoverorder: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      visible: false,
      recoverOrder: this.recoverorder,
      recoverOrderRules: {
        solution: [
          { required: true, message: '请输入责任单位对策说明', trigger: 'blur' },
          { min: 1, max: 200, message: '长度不超过 200 个字符', trigger: 'blur' }
        ],
        explain: [
          { required: true, message: '请输入先行lot结果说明', trigger: 'blur' },
          { min: 1, max: 200, message: '长度不超过 200 个字符', trigger: 'blur' }
        ],
        partial: [
          { required: true, message: '是否部分复机', trigger: 'blur' }
        ],
        eq: [
          { min: 0, max: 50, message: '长度不超过 50 个字符', trigger: 'blur' }
        ],
        kind: [
          { min: 0, max: 30, message: '长度不超过 30 个字符', trigger: 'blur' }
        ],
        step: [
          { min: 0, max: 50, message: '长度不超过 50 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    updateRecoverOrder () {
      this.$refs['form'].validate((valid) => {
        if (valid) {
          let params = {
            solution: this.recoverOrder.solution,
            explain: this.recoverOrder.explain,
            partial: this.recoverOrder.partial
          }
          if (params.partial) {
            params.eq = this.recoverOrder.eq
            params.kind = this.recoverOrder.kind
            params.step = this.recoverOrder.step
          }
          updateRecoverOrder(this.recoverOrder.id, params)
            .then((res) => {
              this.$notify({
                title: '成功',
                message: '修改成功',
                type: 'success'
              })
              // this.recoverOrder = {solution: '', explain: '', partial: false, eq: '', kind: '', step: ''}
              this.visible = false
              this.$emit('change')
            })
            .catch((err) => {
              this.$notify({
                title: '失败',
                message: err,
                type: 'error'
              })
              // this.recoverOrder = {solution: '', explain: '', partial: false, eq: '', kind: '', step: ''}
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
