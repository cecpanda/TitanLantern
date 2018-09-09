<template>
  <div id='product-audit'>
    <span @click='visible = true'>
      <i class="el-icon-star-off"></i>
      <i class="el-icon-star-off"></i>
      <i class="el-icon-star-off"></i>
    </span>
    <el-dialog title="生产签核" :visible.sync="visible">
      <el-form :model='productAudit' :rules='productRules' ref='productForm'>
        <el-form-item label="Recipe关闭人员" prop='recipe_close' label-width='20%'>
          <el-input v-model="productAudit.recipe_close"></el-input>
        </el-form-item>
        <el-form-item label="Recipe确认人员" prop='recipe_confirm' label-width='20%'>
          <el-input v-model="productAudit.recipe_confirm"></el-input>
        </el-form-item>
        <el-form-item label="添加批注" prop='remark' label-width='20%'>
          <el-input
            type='textarea'
            :rows='4'
            v-model="productAudit.remark"
            placeholder='不能超过 500 字符'
          ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="visible = false">取 消</el-button>
        <el-button type="primary" @click="addProductAudit">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { productAudit } from '@/api/tft'

export default {
  name: 'ProductAudit',
  props: {
    order: {
      required: true
    }
  },
  data () {
    return {
      visible: false,
      productAudit: {
        recipe_close: '',
        recipe_confirm: '',
        remark: ''
      },
      productRules: {
        recipe_close: [
          { required: true, message: '请输入 Recipe 关闭人员', trigger: 'blur' },
          { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur' }
        ],
        recipe_confirm: [
          { required: true, message: '请输入 Recipe 确认人员', trigger: 'blur' },
          { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur' }
        ],
        remark: [
          { min: 1, max: 500, message: '长度在 1 到 500 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    addProductAudit () {
      this.$refs['productForm'].validate((valid) => {
        if (valid) {
          let params = {
            order: this.order,
            recipe_close: this.productAudit.recipe_close,
            recipe_confirm: this.productAudit.recipe_confirm
          }
          if (this.productAudit.remark) {
            params.remark = this.productAudit.remark
          }
          productAudit(params)
            .then((res) => {
              this.$notify({
                title: '成功',
                message: '生产签核成功',
                type: 'success'
              })
              this.productAudit = {recipe_close: '', recipe_confirm: '', remark: ''}
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
              this.productAudit = {recipe_close: '', recipe_confirm: '', remark: ''}
              this.visible = false
            })
        }
      })
    }
  }
}
</script>

<style lang='stylus' scoped>
// #product-audit
//   display inline
</style>
