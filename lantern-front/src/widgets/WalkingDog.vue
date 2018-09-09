<template>
  <canvas id="dog" ref='dog'></canvas>
</template>

<script>
export default {
  name: 'WalkingDog',
  data () {
    return {
      canvas: undefined,
      ctx: undefined,
      width: window.innerWidth - 500, // 画布的宽度
      height: 600,
      dogs: [], // (372, 324)
      dogsPath: '../../static/dogs',
      dogsCount: 8,
      // dog 的一些设置. 注意监听器是怎么写的
      dog: {
        speed: 0.1, // 速度
        step: 10, // 一步 10px
        direct: 1, // 方向
        stop: false, // 停止
        index: 0,
        x: 200
        // y: 0, // 不做设置了，直接写死在 drawImage 中
      },
      timer: null // 定时器
    }
  },
  computed: {
    dogSet () { // dog 图片的一些设置
      return {
        // 要使用的图像的宽度、高度，（伸展或缩小图像）
        w: this.dogs.length ? this.dogs[0].naturalWidth / 2 : 0,
        h: this.dogs.length ? this.dogs[0].naturalHeight / 2 : 0
      }
    }
  },
  methods: {
    loadDogs () {
      for (let i = 0; i <= this.dogsCount; i++) {
        let image = this.dogsPath + `/${i}.png`
        let im = new Image()
        im.src = image
        this.dogs.push(im)
      }
    },
    draw () {
      // 先清掉上一次画的内容
      // 不管之前有没有变换坐标系，全清掉了
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height)
      this.ctx.clearRect(0, 0, -this.canvas.width, this.canvas.height)
      if (this.dog.stop) {
        this.dog.index = 0
      }
      let dog = this.dogs[this.dog.index]
      console.log(this.dog.index)
      if (dog.complete) { // 如果图片已经存在于浏览器缓存，直接画图
        this.ctx.drawImage(dog, 0, 0, dog.naturalWidth, dog.naturalHeight, this.dog.x, 0, this.dogSet.w, this.dogSet.h)
      } else {
        dog.onload = () => {
          this.ctx.drawImage(dog, 0, 0, dog.naturalWidth, dog.naturalHeight, this.dog.x, 0, this.dogSet.w, this.dogSet.h)
        }
      }
    },
    walkUpAndDown () { // 来回走
      if (this.dog.direct > 0 && this.dog.x > this.width - this.dogSet.w) {
        this.dog.direct = -1
        this.ctx.scale(-1, 1)
        this.dog.x = -this.dog.x - this.dogSet.w
      } else if (this.dog.direct < 0 && this.dog.x > 0 - this.dogSet.w) {
        this.dog.direct = 1
        this.ctx.scale(-1, 1)
        this.dog.x = -this.dog.x - this.dogSet.w
      }
      this.dog.x += this.dog.step
      // index 持续增加，不受影响
      if (this.dog.index < this.dogsCount) {
        this.dog.index += 1
      } else {
        this.dog.index = 1
      }
      setTimeout(() => {
        requestAnimationFrame(this.walkUpAndDown)
      }, 100)

      // 下面的方法可以实现
      // this.timer = setInterval(() => {
      //   if (this.dog.direct > 0 && this.dog.x > this.width - this.dogSet.w) {
      //     this.dog.direct = -1
      //     this.ctx.scale(-1, 1)
      //     this.dog.x = -this.dog.x - this.dogSet.w
      //   } else if (this.dog.direct < 0 && this.dog.x > 0 - this.dogSet.w) {
      //     this.dog.direct = 1
      //     this.ctx.scale(-1, 1)
      //     this.dog.x = -this.dog.x - this.dogSet.w
      //   }
      //   this.dog.x += this.dog.step
      //   // index 持续增加，不受影响
      //   if (this.dog.index < this.dogsCount) {
      //     this.dog.index += 1
      //   } else {
      //     this.dog.index = 1
      //   }
      // }, 100)
    },
    walk () {
      this.dog.x = Math.abs(this.dog.x) * this.dog.direct
      requestAnimationFrame(this.draw)
    },
    mouseListener () {
      window.addEventListener('mousemove', (event) => {
        // clientX screenX ofsetX
        // 也可以给 this.canvas 添加监听事件，但在container 没效果了
        // 两侧的空白当 20px 处理
        if (offsetX < Math.abs(this.dog.x) + 20) {
          this.stop = false
          this.dog.direct = -1
        } else if (offsetX > Math.abs(this.dog.x)) {
          this.dog.direct = 1
        } else {
          this.dog.stop = true
        }
      })
      window.addEventListener('touchstart', (event) => {
        // let offsetX = event.touches[0].clientX
      })
    },
    async init () {
      this.canvas = document.getElementById('dog')
      // this.canvas = this.$refs.dog
      this.ctx = this.canvas.getContext('2d')
      this.canvas.width = this.width
      this.canvas.height = this.height
      // this.lastWalkingTime = Date.now() // 记录上一帧的时间
      await this.loadDogs()
      this.draw()
      // this.walkUpAndDown()
    }
    // 可以放在 init 中，把 mounted 中 loadDogs 去掉
    // async start () {
    //   await this.loadDogs()
    //   this.wait()
    // },
  },
  watch: {
    dog: {
      handler () {
        this.draw()
        console.log('watch dog')
      },
      deep: true // 深度监听，可监听到对象、数组的变化
    },
    'dog.direct' () {
      this.dog.x -= this.dogSet.w
      this.ctx.scale(-1, 1)
    }
  },
  mounted () {
    this.init()
    this.mouseListener()
  },
  beforeDestroy () {
    if (this.timer) {
      clearInterval(this.timer) // 在vue实例销毁钱，清除我们的定时器
    }
  }
}
</script>

<style lang='stylus' scoped>
#dog
  border 1px solid #409EFF
</style>
