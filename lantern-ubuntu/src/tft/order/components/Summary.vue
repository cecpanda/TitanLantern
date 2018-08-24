<template>
  <div>
    <pre><span v-for='(a, index) in ycy' :key='index'><span v-html='a'></span><br></span></pre>
  </div>
</template>

<script>
import axios from '@/api/http'

export default {
  name: 'Panda',
  data () {
    return {
      ycy: []
    }
  },
  computed: {
  },
  methods: {
    getYcy () {
      axios.get('/static/ycy.json')
        .then((res) => {
          this.ycy = res.data
        })
    }
  },
  mounted () {
    this.getYcy()
  },
  beforeDestroy () {
    // if (this.timer) {
    //   clearInterval(this.timer) // 在vue实例销毁钱，清除我们的定时器
    // }
  }
}
</script>

<style lang='stylus' scoped>
div
  pre
    // color rgba(255, 0, 0, 0.5)
    font-size 6px
    line-height 12px

</style>
