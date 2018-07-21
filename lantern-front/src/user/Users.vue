<template>
  <div>
    <el-row>用户总数: {{ count }}</el-row>
    <el-row :gutter="20">
      <el-col
        :span="3"
        v-for='user in Users'
        :key='user.username'
      >
        <Avatar :user='user'></Avatar>
      </el-col>
    </el-row>
    <el-pagination
      background
      @current-change="handleCurrentChange"
      :current-page.sync="page"
      :page-size='pageSize'
      layout="prev, pager, next, jumper"
      :total="count">
    </el-pagination>
  </div>
</template>

<script>
import { getAllUsers } from '@/api/user'
import Avatar from './components/Avatar'

export default {
  name: 'Users',
  data () {
    return {
      page: 1,
      pageSize: 10,
      count: null,
      Users: []
    }
  },
  methods: {
    getUsers () {
      getAllUsers(this.page, this.pageSize)
        .then((res) => {
          this.count = res.data.count
          this.Users = res.data.results
        })
        .catch((error) => {
          console.log(error)
        })
    },
    handleCurrentChange (val) {
      this.getUsers()
    }
  },
  created () {
    this.getUsers()
  },
  components: {
    Avatar
  }
}
</script>

<style lang='stylus' scoped>
.el-pagination
  margin 50px auto
</style>
