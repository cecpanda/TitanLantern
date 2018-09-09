<!-- 绘制可以走路的狗 -->
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
      dog: {
        speed: 0.1, // 小狗的速度
        step: 10, // 一步 10px
        currentX: 0, // 当前的位移
        mouseX: -1,
        frontStopX: -1, // 往前走停留的位置
        backStopX: window.innerWidth, // 往回走停留的位置
        direct: -1, // 方向
        stop: false // 是否停止
      },
      canvas: undefined,
      ctx: undefined,
      lastWalkingTime: undefined,
      index: -1,
      width: window.innerWidth // 画布的宽度
    }
  },
  computed: {
    dogWidth () {
      return this.dogs.length ? this.dogs[0].naturalWidth / 2 : 0
    }
  },
  methods: {
    init () {
      this.canvas = document.getElementById('dog')
      this.ctx = this.canvas.getContext('2d')
      this.canvas.width = this.width
      this.canvas.height = 600
      this.lastWalkingTime = Date.now() // 记录上一帧的时间
      this.index = -1 // 记录当前画的图片索引
      this.loadDogs() // 把 start 挪进来
      this.mousePosition()
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
    mousePosition () {
      window.addEventListener('mousemove', event => {
        this.dog.frontStopX = event.clientX - this.dogWidth
        this.dog.backStopX = event.clientX
      })
      window.addEventListener('touchstart', event => {
        this.dog.frontStopX = event.touches[0].clientX - this.dogWidth
        this.dog.backStopX = event.touches[0].clientX
      })
    },
    walk () {
      let now = Date.now()
      // 计算位移 = 时间 * 速度
      let distance = (now - this.lastWalkingTime) * this.dog.speed
      if (distance < this.dog.step) {
        window.requestAnimationFrame(this.walk)
      }
      this.index = ++this.index % this.dogsCount
      if (this.dog.frontStopX > this.dog.mouseX) {
        // 如果鼠标在狗的前面则往前走
        this.dog.direct = 1
      } else if (this.dog.backStopX < this.dog.mouseX) {
        // 如果鼠标在狗的后面则往回走
        this.dog.direct = -1
      } else {
        // 如果鼠标在狗在位置
        this.dog.stop = true
        // 初始化的时候小狗是反方向的，frontStopX为初始值-1
        // 说明鼠标还没动过
        this.dog.direct = this.dog.frontStopX === -1 ? -1 : this.dog.backStopX - this.dog.mouseX > this.pictureWidth / 2 ? 1 : -1
        this.index = -1
        // this.dog.mouseX = this.dog.stopX
      }
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height)
      this.ctx.save()
      if (!this.dog.stop) {
        this.dog.mouseX += this.dog.step * this.dog.direct
      }
      if (this.dog.direct === -1) {
        this.ctx.scale(this.dog.direct, 1)
      }
      let img = this.dogs[this.index + 1]
      let drawX = 0
      drawX = this.dog.mouseX * this.dog.direct - (this.dog.direct === -1 ? this.dogWidth : 0)
      this.ctx.drawImage(img, 0, 0, img.naturalWidth, img.naturalHeight, drawX, 20, 186, 162)
      this.ctx.restore()
      this.lastWalkingTime = now
      window.requestAnimationFrame(this.walk)
      // if (now - this.lastWalkingTime > 100) { // 绘制狗的图片，每过100ms就画一张
      //   let distance = (now - this.lastWalkingTime) * this.dog.speed
      //   if (distance < this.dog.step) {
      //     window.requestAnimationFrame(this.walk)
      //   }
      //   this.dog.currentX += distance
      //   // 先清掉上一次画的内容
      //   this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height)
      //   // 获取下一张图片的索引
      //   let index = ++this.index % this.dogsCount
      //   let img = this.dogs[index + 1]
      //   this.ctx.drawImage(img, 0, 0, img.naturalWidth, img.naturalHeight, this.dog.currentX, 400, 186, 162)
      //   this.lastWalkingTime = now
      // }
      // // 继续给下一帧注册一个函数
      // requestAnimationFrame(this.walk)
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
