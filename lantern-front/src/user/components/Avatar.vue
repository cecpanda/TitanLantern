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
import { getFollowing, follow, unfollow } from '@/api/user'

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
    getFollowing () {
      getFollowing(this.username)
        .then((res) => {
          let following = res.data.following
          // if (this.user.username in following) {
          // 上面的这个有点问题
          if (following.includes(this.user.username)) {
            this.isFollowing = true
          }
        })
        .catch((error) => {
          console.log(error)
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
    this.getFollowing()
  }
}
</script>

<style lang='stylus' scoped>
.avatar
  img
    display block
    width 100%
</style>
