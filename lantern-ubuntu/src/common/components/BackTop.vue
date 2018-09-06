<template>
  <transition name='icon'>
    <i class='iconfont' title='返回顶部' v-show="show" @click="backTop">&#xe6ae;</i>
  </transition>
</template>
<script>
export default {
  name: 'BackTop',
  data () {
    return {
      scrollTop: '',
      show: false
    }
  },
  methods: {
    handleScroll () {
      this.scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
      if (this.scrollTop > 500) {
        this.show = true
      } else {
        this.show = false
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
          _that.show = false
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
.icon-enter
.icon-leave-to
  opacity 0
.icon-enter-active
.icon-leave-active
  transition opacity 2s
.iconfont
  position fixed
  bottom 20px
  right 20px
  font-size 3em
  color #409EFF
.iconfont:hover
  font-size 3.5em
  color #065FBB
</style>
