export default {
  setLoginStatus (ctx, isLogged) {
    ctx.commit('setLoginStatus', isLogged)
  },
  setTest (state, val) {
    state.test = val
  }
}
