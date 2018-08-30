<template>
  <el-row>
    <el-col :span='8'>
      <el-form :model="form" status-icon :rules="rules" ref="form" label-width="120px">
        <el-form-item label="旧密码" prop="oldPassword">
          <el-input type="password" v-model="form.oldPassword"></el-input>
        </el-form-item>
        <el-form-item label="新密码" prop="newPassword">
          <el-input type="password" v-model="form.newPassword"></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="checkPassword">
          <el-input type="password" v-model="form.checkPassword"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button @click="resetForm('form')">重置</el-button>
          <el-button type="primary" @click="submitForm('form')">提交</el-button>
        </el-form-item>
      </el-form>
    </el-col>
  </el-row>
</template>

<script>
import { changePassword } from '@/api/user'

export default {
  name: 'ChangePassword',
  data () {
    let validateoldPassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入旧密码'))
      } else {
        callback()
      }
    }
    let validatenewPassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入新密码'))
      } else {
        if (this.form.checkPassword !== '') {
          this.$refs.form.validateField('checkPassword')
        }
        callback()
      }
    }
    let validatecheckPassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.form.newPassword) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      form: {
        oldPassword: '',
        newPassword: '',
        checkPassword: ''
      },
      rules: {
        oldPassword: [
          { validator: validateoldPassword, trigger: 'blur' }
        ],
        newPassword: [
          { validator: validatenewPassword, trigger: 'blur' }
        ],
        checkPassword: [
          { validator: validatecheckPassword, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          changePassword(this.form.oldPassword, this.form.newPassword)
            .then((res) => {
              this.$message({
                showClose: true,
                message: '修改成功',
                type: 'success'
              })
              this.form.oldPassword = ''
              this.form.newPassword = ''
              this.form.checkPassword = ''
            })
            .catch((error) => {
              console.log(error)
              this.$message({
                showClose: true,
                message: '旧密码错误',
                type: 'error'
              })
            })
        } else {
          this.$message({
            showClose: true,
            message: '请输入密码',
            type: 'warning'
          })
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style lang="stylus" scoped>

</style>
