<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
// import { jwtAuthVerify } from './api/user'

export default {
  name: 'App'
  // data () {
  //   return {
  //     isLogged: false
  //   }
  // },
  // methods: {
  //   checkLogin () {
  //     // let token = JSON.parse(localStorage.getItem('token'))
  //     let token = this.$store.state.token
  //     this.isLogged = jwtAuthVerify({token: token})
  //   }
  // },
  // watch: {
  //   $route () {
  //     this.checkLogin()
  //   },
  //   isLogged (val) {
  //     this.$store.dispatch('setLoginStatus', val)
  //   }
  // },
  // created () {
  //   this.checkLogin()
  // }
}
</script>

<style>
/*#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}*/
</style>
