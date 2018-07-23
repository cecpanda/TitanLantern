<template>
  <div>
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="关注" name="following" @click='handleFollowing'>我的关注</el-tab-pane>
      <el-tab-pane label="被关注" name="follower" @click='handleFollower'>关注我的</el-tab-pane>
    </el-tabs>
    <el-row :gutter="20">
      <el-col
        :span="3"
        v-for='user in users'
        :key='user'
      >
        {{ user }}
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Avatar from './Avatar'
import { following, followers } from '@/api/user'

export default {
  name: 'Name',
  data () {
    return {
      activeName: 'following',
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
    },
    handleFollowing () {
      following(this.username)
        .then((res) => {
          this.users = res.data.following
        })
        .catch((error) => {
          console.log(error)
        })
    },
    handleFollower () {
      followers(this.username)
        .then((res) => {
          this.users = res.data.followers
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  watch: {
    activeName (val) {
      if (val === 'following') {
        this.handleFollowing()
      }
      if (val === 'follower') {
        this.handleFollower()
      }
    }
  },
  components: {
    Avatar
  },
  mounted () {
    this.handleFollowing()
  }
}
</script>

<style lang='stylus' scoped>

</style>
