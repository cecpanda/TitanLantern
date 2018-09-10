<!-- 绘制原地踏步的狗 -->
<template>
  <canvas id='dog' ref='canvas'></canvas>
</template>

<script>
export default {
  name: 'WalkingDog',
  data () {
    return {
      dogs: [],
      dogsPath: '../../static/dogs',
      dogsCount: 8,
      canvas: undefined,
      ctx: undefined,
      lastWalkingTime: undefined,
      index: -1
    }
  },
  methods: {
    init () {
      this.canvas = document.getElementById('dog')
      this.ctx = this.canvas.getContext('2d')
      this.canvas.width = window.innerWidth - 75
      this.canvas.height = 600
      this.lastWalkingTime = Date.now() // 记录上一帧的时间
      this.index = -1 // 记录当前画的图片索引
      this.loadDogs() // 把 start 挪进来
      this.walk()
    },
    loadDogs () {
      for (let i = 0; i <= this.dogsCount; i++) {
        let image = this.dogsPath + `/${i}.png`
        let im = new Image()
        im.src = image
        this.dogs.push(im)
      }
    },
    walk () {
      let now = Date.now()
      if (now - this.lastWalkingTime > 100) { // 绘制狗的图片，每过100ms就画一张
        // 先清掉上一次画的内容
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height)
        // 获取下一张图片的索引
        let index = ++this.index % this.dogsCount
        let img = this.dogs[index + 1]
        this.ctx.drawImage(img, 0, 0, img.naturalWidth, img.naturalHeight, 20, 400, 186, 162)
        this.lastWalkingTime = now
      }
      // 继续给下一帧注册一个函数
      requestAnimationFrame(this.walk)
    },
    // 目前不用这个了
    async start () {
      // 等待资源加载完
      await this.loadDogs()
      // requestAnimationFrame(this.walk)
      this.walk()
    }
  },
  mounted () {
    this.init()
  }
}
</script>

<style lang='stylus' scoped>
#dog
  border 1px solid #409EFF
</style>
