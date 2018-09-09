<template>
  <div>
    <pre><span v-for='(a, index) in pic1' :key='index'><span v-html='a'></span><br></span></pre>
    <pre><span v-for='(a, index) in pic2' :key='index'><span v-html='a'></span><br></span></pre>
  </div>
</template>

<script>
import axios from '@/api/http'

export default {
  name: 'Panda',
  data () {
    return {
      panda1: [],
      index1: 1,
      panda2: [],
      index2: 1
    }
  },
  computed: {
    pic1 () {
      return this.panda1[this.index1]
    },
    pic2 () {
      return this.panda2[this.index2]
    }
  },
  methods: {
    getPanda1 () {
      console.log('@')
      axios.get('/static/panda1.json')
        .then((res) => {
          this.panda1 = res.data
        })
    },
    getPanda2 () {
      axios.get('/static/panda2.json')
        .then((res) => {
          this.panda2 = res.data
        })
    }
  },
  mounted () {
    this.getPanda1()
    // this.getPanda2()
    var _this = this // 声明一个变量指向vue实例this,保证作用域一致
    this.timer = setInterval(() => {
      if (this.index1 < this.panda1.length - 1) {
        _this.index1++
      } else {
        _this.index1 = 1
      }
      if (this.index2 < this.panda2.length - 1) {
        _this.index2++
      } else {
        _this.index2 = 1
      }
    }, 100)
  },
  beforeDestroy () {
    if (this.timer) {
      clearInterval(this.timer) // 在vue实例销毁钱，清除我们的定时器
    }
  }
}
</script>

<style lang='stylus' scoped>
div
  pre
    // color rgba(255, 0, 0, 0.5)
    font-size 8px
    line-height 8px
</style>
