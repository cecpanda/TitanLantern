<template>
  <div>
    <el-tabs v-model="activeName" @tab-click="handleClick" type="border-card">
      <el-tab-pane label="关注" name="following">
        我的关注
      </el-tab-pane>
      <el-tab-pane label="粉丝" name="follower">
        我的粉丝
      </el-tab-pane>
      <el-tab-pane label="所有用户" name="allUsers">
        所有用户
      </el-tab-pane>
    </el-tabs>
<!--     <el-row :gutter="20">
      <el-col
        :span="3"
        v-for='user in users'
        :key='user.username'
      >
        {{ user.username }}
      </el-col>
    </el-row> -->
    <el-row :gutter="20">
      <el-col
        :span="3"
        v-for='user in users'
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
        layout="total, prev, pager, next, jumper"
        :total="count">
      </el-pagination>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Avatar from './Avatar'
import { following, followers, getAllUsers } from '@/api/user'

export default {
  name: 'Name',
  data () {
    return {
      activeName: 'following',
      page: 1,
      pageSize: 10,
      count: null,
      users: []
    }
  },
  computed: {
    ...mapGetters({
      username: 'username'
    })
  },
  methods: {
    handleClick (tab, event) {
      if (tab.name === 'following') {
        this.handleFollowing()
      }
      if (tab.name === 'follower') {
        this.handleFollower()
      }
      if (tab.name === 'allUsers') {
        this.handleAllUsers()
      }
    },
    handleFollowing () {
      following(this.username, this.page, this.pageSize)
        .then((res) => {
          this.count = res.data.count
          this.users = res.data.results
        })
        .catch((error) => {
          console.log(error)
        })
    },
    handleFollower () {
      followers(this.username, this.page, this.pageSize)
        .then((res) => {
          this.count = res.data.count
          this.users = res.data.results
        })
        .catch((error) => {
          console.log(error)
        })
    },
    handleAllUsers () {
      getAllUsers(this.page, this.pageSize)
        .then((res) => {
          this.count = res.data.count
          this.users = res.data.results
        })
        .catch((error) => {
          console.log(error)
        })
    },
    handleCurrentChange (val) {
      if (this.activeName === 'following') {
        this.handleFollowing()
      } else if (this.activeName === 'follower') {
        this.handleFollower()
      } else if (this.activeName === 'allUsers') {
        this.handleAllUsers()
      }
    }
  },
  // watch: {
  //   activeName (val) {
  //     if (val === 'following') {
  //       this.handleFollowing()
  //     }
  //     if (val === 'follower') {
  //       this.handleFollower()
  //     }
  //     if (val === 'allUsers') {
  //       this.handleAllUsers()
  //     }
  //   }
  // },
  components: {
    Avatar
  },
  mounted () {
    this.handleFollowing()
  }
}
</script>

<style lang='stylus' scoped>
.el-pagination
  margin-top 50px
</style>
