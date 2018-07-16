<template>
  <div>
    <h1>我的动态</h1>
    {{ this.profile }}
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getUser } from '@/api/user'

export default {
  name: 'Action',
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
  }
}
</script>

<style lang='stylus' scoped>

</style>
