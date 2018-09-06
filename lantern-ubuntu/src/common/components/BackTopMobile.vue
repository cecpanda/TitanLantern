<template>
  <transition name='icon'>
    <i class='iconfont' title='返回顶部' v-show='show' @click='backTop'>&#xe6ae;</i>
  </transition>
</template>

<script>
// PC 不能用，移动端不知道
export default {
  name: 'BackTop',
  props: {
    // 这是选择滚动对象的props值，如果滚动的对象是当前组件的父元素，就设置scrollObj为true.如果没有设置就默认为window对象
    myself: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      show: false,
      target: ''
    }
  },
  methods: {
    handleScroll () {
      console.log(this.target.scrollTop)
      if (this.target.scrollTop > 500) {
        this.show = true
      } else {
        this.show = false
      }
    },
    backTop () {
      let timer = setInterval(() => {
        let top = this.target.scrollTop
        let speed = Math.ceil(top / 5)
        this.target.scrollTop = top - speed
        if (top === 0) {
          clearInterval(timer)
        }
      }, 20)
    }
  },
  mounted () {
    // 通过这个 target 来判断当前的滚动监听对象是谁
    if (this.myself) {
      this.target = this.$el.parentNode
    } else {
      this.target = document.body
    }
    this.target.addEventListener('scroll', this.handleScroll)
  },
  destroyed () {
    this.target.removeEventListener('scroll', this.handleScroll)
  }
}
</script>

<style lang='stylus' scoped>
.iconfont
  font-size 2em
  color #409EFF
.iconfont:hover
  font-size 3em
  color #2CCC89
</style>
