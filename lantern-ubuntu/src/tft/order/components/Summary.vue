<template>
  <div>
    <pre><span v-for='(a, index) in ycy' :key='index'><span v-html='a'></span><br></span></pre>
    <pre class='panda'><span v-for='(a, index) in pic' :key='index'><span v-html='a'></span><br></span></pre>
  </div>
</template>

<script>
import axios from '@/api/http'

export default {
  name: 'Panda',
  data () {
    return {
      ycy: [],
      panda: [],
      index: 1
    }
  },
  computed: {
    pic () {
      return this.panda[this.index]
    }
  },
  methods: {
    getYcy () {
      axios.get('/static/ycy.json')
        .then((res) => {
          this.ycy = res.data
        })
    },
    getPanda () {
      axios.get('/static/panda.json')
        .then((res) => {
          this.panda = res.data
        })
    }
  },
  mounted () {
    this.getYcy()
    this.getPanda()
    var _this = this // 声明一个变量指向vue实例this,保证作用域一致
    this.timer = setInterval(() => {
      if (this.index < this.panda.length - 1) {
        _this.index++
      } else {
        _this.index = 1
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
    font-size 6px
    line-height 4px
.panda
  font-size 5px
  line-height ipx
</style>
