<template>
  <div>
    <canvas ref='rain' id='rain' width='500' height=100></canvas>
  </div>
</template>

<script>
import Drops from '@/common/rain/Drops'
import DropWords from '@/common/rain/DropWords'
import Gui from '@/common/rain/Gui'
import Environment from '@/common/rain/Environment'
import Text from '@/common/rain/Text'
import RainText from '@/common/rain/RainText'

export default {
  name: 'Rain',
  data () {
    return {
      words: 'abcdefg'
    }
  },
  methods: {
    mainCode (data, message) {
      let gui = new Gui()
      let environment = new Environment()
      let rainText = []
      let inputText = new Text()
      let makeRainText = false
      let rainMessage

      if (message === null) {
        rainMessage = false
      } else {
        rainMessage = true
      }

      environment.initializeCanvas()

      let drops = []
      for (let i = 0; i < environment.getIntensity(); i++) {
        drops[i] = new Drops(i, environment.getChars(), environment.getGravity())
        drops[i].initializeDrop()
      }

      let currentDrop
      let dropWord = new Array(5)
      for (let i = 0; i < dropWord.length; i++) {
        dropWord[i] = new Array(4)
        dropWord[i][0] = new DropWords()
        currentDrop = Math.floor(Math.random() * (data.length - 1 + 1)) + 1
        dropWord[i][0].initializeText(data[currentDrop]['palavra'], environment.getGravity(), environment.getWind())
        dropWord[i][1] = Math.floor(Math.random() * (800 - 60 + 1)) + 60 // max_counter
        dropWord[i][2] = 0 // counter
        dropWord[i][3] = false
      }

      document.addEventListener('mousemove', function (e) {
        environment.updateCurrentWind(e.clientX)
      })

      let theRain = setInterval(rainTimer, 16.6)

      let rainCanvas = document.getElementById('rain')
      let rainContext = rainCanvas.getContext('2d')

      let text = []
      let timing = []
      let currentText = 0
      let totalTexts = 0

      function rainTimer () {
        if (gui.checkInput()) {
          gui.confirmReceive()
          var analyzetext = gui.getText()
          text = inputText.processText(analyzetext)
          for (let a = 0; a < text.length; a++) {
            if (text[a].length > 0) {
              totalTexts++
              rainText[totalTexts - 1] = new RainText()
              rainText[totalTexts - 1].initializeText(text[a], environment.getGravity(), environment.getWind())
            }
          }
        }
        if (rainMessage === true) {
          var analyzeText = message
          text = inputText.processText(analyzeText)
          for (let a = 0; a < text.length; a++) {
            if (text[a].length > 0) {
              totalTexts++
              rainText[totalTexts - 1] = new RainText()
              rainText[totalTexts - 1].initializeText(text[a], environment.getGravity(), environment.getWind())
            }
          }
          rainMessage = false
        }
        if (rainText[currentText] !== undefined) {
          makeRainText = true
          if (rainText[currentText].endRainText() === true) {
            makeRainText = false
            currentText++
          }
        }
        environment.updateCurrentIntensity()
        rainContext.clearRect(0, 0, rainCanvas.width, rainCanvas.height)
        rainContext.textAlign = 'center'
        rainContext.textBaseline = 'middle'
        let currentIntensity = environment.getCurrentIntensity()
        let currentWind = environment.getWind()

        for (var z = 0; z < dropWord.length; z++) {
          if (dropWord[z][2] < dropWord[z][1]) {
            dropWord[z][2]++
          } else {
            dropWord[z][0].updateText()
            let inText = dropWord[z][0].getText()
            let echo = dropWord[z][0].echoLine()
            for (let i = 0; i < inText.length; i++) {
              if (echo[i] !== null) {
                let offsetX = 0
                let offsetY = inText[i][3] / 2 + 10

                rainContext.beginPath()
                rainContext.moveTo(inText[i][0] + offsetX, inText[i][1] - offsetY)
                rainContext.lineTo(echo[i][0] + offsetX, echo[i][1] - offsetY)
                rainContext.strokeStyle = '#7fa1d3'
                rainContext.stroke()
              }

              rainContext.fillStyle = 'black'
              rainContext.font = inText[i][3] + 'pt Source Sans Pro'
              rainContext.fillText(inText[i][2], inText[i][0], inText[i][1])
            }
          }
          if (dropWord[z][0].endRainText()) {
            dropWord[z] = new Array(4)
            dropWord[z][0] = new DropWords()
            currentDrop = Math.floor(Math.random() * (data.length - 1 + 1)) + 1
            dropWord[z][0].initializeText(data[currentDrop]['palavra'], environment.getGravity(), environment.getWind())
            dropWord[z][1] = Math.floor(Math.random() * (800 - 60 + 1)) + 60
            dropWord[z][2] = 0
            dropWord[z][3] = false
          }
        }
        for (let i = 0; i < environment.getCurrentIntensity(); i++) {
          drops[i].updateDrop(currentIntensity, currentWind)

          let offsetX = 0
          let offsetY = drops[i].getSize() / 2

          let echo = drops[i].echoLine()
          rainContext.beginPath()
          rainContext.moveTo(drops[i].getX() + offsetX, drops[i].getY() - offsetY)
          rainContext.lineTo(echo[0] + offsetX, echo[1] - offsetY)
          rainContext.strokeStyle = '#7fa1d3'
          rainContext.stroke()

          var tempColor = (200 + (8 * 11)) - (drops[i].getSize() * 11)
          rainContext.fillStyle = 'rgba("+temp_color+", "+temp_color+", "+temp_color+", 1)'

          rainContext.font = drops[i].getSize() + 'px Source Sans Pro'
          rainContext.fillText(drops[i].getChar(), drops[i].getX(), drops[i].getY())
        }
      }
      if (make_rain_text === true) {
        rainText[currentText].updateText()
          var in_text = rain_text[current_text].getText()
          var echo = rain_text[current_text].echoLine()
          for(var i = 0; i < in_text.length; i++){
            if(echo[i] != null){
              var offset_x = 0
              var offset_y = in_text[i][3]/2+10

              rain_context.beginPath()
              rain_context.moveTo(in_text[i][0]+offset_x,in_text[i][1]-offset_y)
              rain_context.lineTo(echo[i][0]+offset_x,echo[i][1]-offset_y)
              rain_context.strokeStyle="#7fa1d3"
              rain_context.stroke()
            }

            rain_context.fillStyle = "black"
            rain_context.font = "bold "+in_text[i][3]+"pt Source Sans Pro";
            rain_context.fillText(in_text[i][2], in_text[i][0], in_text[i][1]);
          }
      }
    }
  }
}
</script>

<style lang='stylus' scoped>

</style>
