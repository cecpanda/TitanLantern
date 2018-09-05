
<template>
  <div id='back-top'>
    <i class='iconfont' v-show="backTopShow" @click="backTop">&#xe6ae;</i>
  </div>
</template>
<script>
export default {
  name: 'BackTop',
  data () {
    return {
      scrollTop: '',
      backTopShow: false
    }
  },
  methods: {
    handleScroll () {
      this.scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
      if (this.scrollTop > 500) {
        this.backTopShow = true
      }
    },
    backTop () {
      let timer = null
      let _that = this
      cancelAnimationFrame(timer)
      timer = requestAnimationFrame(function fn () {
        if (_that.scrollTop > 0) {
          _that.scrollTop -= 50
          document.body.scrollTop = document.documentElement.scrollTop = _that.scrollTop
          timer = requestAnimationFrame(fn)
        } else {
          cancelAnimationFrame(timer)
          _that.goTopShow = false
        }
      })
    }
  },
  mounted () {
    window.addEventListener('scroll', this.handleScroll)
  },
  destroyed () {
    window.removeEventListener('scroll', this.handleScroll)
  }
}
</script>

<style lang='stylus' scoped>
#back-top
  position fixed
  right 20px
  bottom 20px
.iconfont:hover
  font-size 2em
</style>
