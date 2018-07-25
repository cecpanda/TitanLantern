<template>
  <div class='avatar'>
    <img :src="user.avatar">
    <el-tag>用户名：{{ user.username }}</el-tag>
    <el-tag>真名： {{ user.realname }}</el-tag>
    <br/>
    <el-button
      type="primary"
      round
      @click='handleunFollow'
      v-if='isFollowing'
      size="mini"
    >
      取消关注
    </el-button>
    <template v-else-if='user.username===username'></template>
    <el-button
      type="primary"
      round
      @click='handleFollow'
      v-else
      size="mini"
    >
      关注
    </el-button>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { follow, unfollow, followStatus } from '@/api/user'

export default {
  name: 'Avatar',
  props: ['user'],
  data () {
    return {
      isFollowing: false
    }
  },
  computed: {
    ...mapGetters({
      username: 'username'
    })
  },
  methods: {
    followStatus () {
      followStatus(this.username, this.user.username)
        .then((res) => {
          if (res.data.status) {
            this.isFollowing = true
          }
        })
    },
    handleFollow () {
      follow(this.user.username)
        .then((res) => {
          this.isFollowing = !this.isFollowing
        })
        .catch((error) => {
          console.log(error)
        })
    },
    handleunFollow () {
      unfollow(this.user.username)
        .then((res) => {
          this.isFollowing = !this.isFollowing
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  mounted () {
    this.followStatus()
  }
}
</script>

<style lang='stylus' scoped>
.avatar
  margin-top 30px
  img
    display block
    width 100%
</style>
