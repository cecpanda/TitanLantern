<template>
  <div class="login">
    <el-button type="text" @click="loginVisible=true">登录</el-button>
    <el-dialog title="登录" :visible.sync="loginVisible" :width='width'>
      <el-form
        :model="form"
        :rules="rules"
        ref="loginForm"
        :label-width="labelWidth"
        status-icon
      >
        <el-form-item label="用户名" prop="username">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="form.password"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="loginVisible=false">取 消</el-button>
        <el-button @click="resetForm('loginForm')">重置</el-button>
        <el-button type="primary" :plain="true" @click="submitForm('loginForm')">登录</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { jwtAuth } from '@/api/user'

export default {
  name: 'Login',
  data () {
    let validateUsername = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入用户名'))
      } else {
        callback()
      }
    }
    let validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        callback()
      }
    }
    return {
      loginVisible: false,
      width: '33%',
      labelWidth: '15%',
      form: {
        username: '',
        password: ''
      },
      rules: {
        username: [
          { required: true, validator: validateUsername, trigger: 'blur' }
        ],
        password: [
          { required: true, validator: validatePass, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          jwtAuth(this.form.username, this.form.password)
            .then((response) => {
              console.log(response.data)
              this.loginVisible = false
              localStorage.setItem('token', response.data.token)
              localStorage.setItem('username', response.data.username)
              this.$store.dispatch('setInfo')
              this.$router.push({name: 'Home'})
            })
            .catch((error) => {
              console.log(error)
              this.$message({
                showClose: true,
                message: '账号或密码错误',
                type: 'error'
              })
            })
        } else {
          this.$message({
            showClose: true,
            message: '请输入账号密码',
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

<style lang='stylus' scoped>
.login
  position absolute
  right 20px
</style>
