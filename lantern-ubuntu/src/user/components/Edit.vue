<template>
  <div>
    <h1>修改资料</h1>
    <el-row>
      <el-form
        ref="form"
        label-width="150px"
        size='medium'
      >
        <el-col :span=8>
          <el-form-item label="用户名">
            <el-input v-model="profile.username" disabled></el-input>
          </el-form-item>
          <el-form-item label="真实姓名">
            <el-input v-model="profile.realname"></el-input>
          </el-form-item>
          <el-form-item label="邮箱">
            <el-input v-model="profile.email"></el-input>
          </el-form-item>
          <el-form-item label="电话">
            <el-input v-model="profile.mobile"></el-input>
          </el-form-item>
          <el-form-item label="手机">
            <el-input v-model="profile.phone"></el-input>
          </el-form-item>
          <el-form-item label="性别">
            <template>
              <el-radio v-model="profile.gender" label="M">男</el-radio>
              <el-radio v-model="profile.gender" label="F">女</el-radio>
            </template>
          </el-form-item>
          <el-form-item label="科室">
            <el-tag
              v-for='group of profile.groups'
              :key='group.id'
            >
              {{ group.name }}
            </el-tag>
          </el-form-item>
        </el-col>
        <el-col :span=8>
          <el-form-item label="头像">
            <el-upload
              class="avatar-uploader"
              action="https://jsonplaceholder.typicode.com/posts/"
              :show-file-list="false"
              :on-success="handleAvatarSuccess"
              :before-upload="beforeAvatarUpload"
            >
              <img
                v-if="profile.avatar"
                :src="profile.avatar"
                class="avatar"
              >
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
          </el-form-item>
          <el-form-item label="注册日期">
<!--             <el-date-picker
              v-model="profile.date_joined"
              type="datetime"
              disabled
            >
            </el-date-picker> -->
            <el-tag>
              {{ profile.date_joined | formatDate }}
            </el-tag>
          </el-form-item>
          <el-form-item>
          </el-form-item>
          <el-form-item>
            <el-button
              type="primary"
              round
              @click="submitForm('form')"
            >
              修改
            </el-button>
          </el-form-item>
        </el-col>
      </el-form>
    </el-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getUser, changeProfile } from '@/api/user'
import { formatDate } from '@/common/js/date.js'

export default {
  name: 'Edit',
  data () {
    return {
      profile: {},
      allGroups: []
    }
  },
  computed: {
    ...mapGetters({
      username: 'username'
    })
  },
  methods: {
    getUserProfile (username) {
      getUser(username)
        .then((response) => {
          this.profile = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // getAllGroups () {
    //   getAllGroups()
    //     .then((response) => {
    //       this.allGroups = response.data
    //     })
    //     .catch((error) => {
    //       console.log(error)
    //     })
    // },
    handleAvatarSuccess (res, file) {
      this.profile.avatar = URL.createObjectURL(file.raw)
    },
    beforeAvatarUpload (file) {
      const isJPG = file.type === 'image/jpeg' || file.type === 'image/png'
      const isLt2M = file.size / 1024 / 1024 < 2
      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG/PNG 格式!')
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!')
      }
      return isJPG && isLt2M
    },
    submitForm (formName) {
      changeProfile(this.profile)
        .then((res) => {
          this.profile = res.data
          this.$message.sucess('修改成功')
        })
        .catch((error) => {
          console.log(error)
          this.$message.error('修改失败')
        })
    }
  },
  created () {
    this.getUserProfile(this.username)
  },
  filters: {
    formatDate (time) {
      let date = new Date(time)
      return formatDate(date, 'yyyy-MM-dd hh:mm:ss')
    }
  }
}
</script>

<style lang='stylus' scoped>
.avatar-uploader
.el-upload
  border: 1px dashed #d9d9d9
  border-radius: 6px
  cursor: pointer
  position: relative
  overflow: hidden
.avatar-uploader
.el-upload:hover
  border-color: #409EFF
.avatar-uploader-icon
  font-size: 28px
  color: #8c939d
  width: 178px
  height: 178px
  line-height: 178px
  text-align: center
.avatar
  width: 178px
  height: 178px
  display: block
</style>
