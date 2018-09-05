<template>
  <div @click='backTop'>BackTop
  </div>
</template>

<script>
import BScroll from 'better-scroll'

export default {
  name: 'BackTop',
  methods: {
    backTop () {
      this.scroll.scrollTo(0, 0)
      // document.body.scrollTop = 0
      // document.documentElement.scrollTop = 0
    }
  },
  mounted () {
    this.scroll = new BScroll(document.body)
  }
}
</script>

<style lang='stylus' scoped>

</style>
