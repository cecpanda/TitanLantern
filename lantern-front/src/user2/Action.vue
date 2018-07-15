<template>
  <el-container>
    <el-aside width="">
      <SideNav/>
    </el-aside>
    <el-main>
      <h1>我的动态</h1>
      {{ this.profile }}
    </el-main>
  </el-container>
</template>

<script>
import { mapGetters } from 'vuex'
import { getUser } from '@/api/user'
import SideNav from './components/SideNav'

export default {
  name: 'UserAction',
  // props: {
  //   username: {
  //     type: String,
  //     required: true
  //   }
  // }
  data () {
    return {
      profile: {}
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
    }
  },
  created () {
    this.getUserProfile(this.username)
  },
  components: {
    SideNav
  }
}
</script>

<style lang='stylus' scoped>
</style>
