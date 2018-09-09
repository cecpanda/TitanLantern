<template>
  <transition name='icon'>
    <i class='iconfont' title='返回顶部' v-show="show" @click="backTop">&#xe6ae;</i>
  </transition>
</template>

<script>
import BScroll from 'better-scroll'

export default {
  name: 'BackTop',
  data () {
    return {
      show: true,
      scroll: undefined
    }
  },
  methods: {
    backTop () {
      this.scroll.scrollTo(0, 0)
    }
  },
  mounted () {
    this.scroll = new BScroll(document.body)
  }
}
</script>

<style lang='stylus' scoped>
.icon-enter
.icon-leave-to
  opacity 0
.icon-enter-active
.icon-leave-active
  transition opacity 3s
.iconfont
  font-size 2em
  color #409EFF
.iconfont:hover
  font-size 3em
  color #2CCC89
</style>
