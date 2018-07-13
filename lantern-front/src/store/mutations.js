export default {
  setInfo (state) {
    state.token = localStorage.getItem('token')
    state.username = localStorage.getItem('username')
  }
}
