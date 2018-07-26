<template>
  <el-row>
    <el-col :span='8'>
      <el-form :model="form" label-width="50px">
        <el-form-item label="旧密码" prop="password">
          <el-input type="password" v-model="form.password"></el-input>
        </el-form-item>
        <el-form-item label="新密码" prop="password">
          <el-input type="password" v-model="form.password"></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="password">
          <el-input type="password" v-model="form.password"></el-input>
        </el-form-item>
      </el-form>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: 'ChangePassword',
  data () {
    return {
      form: {
        old_password: '',
        new_password: ''
      }
    }
  }
}
</script>

<style lang="stylus" scoped>

</style>
