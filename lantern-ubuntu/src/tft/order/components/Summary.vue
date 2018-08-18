<template>
  <div>Summary
    {{ data }}
    <button @click='change'>hehe</button>
  </div>
</template>

<script>
import { getOrders } from '@/api/tft'

export default {
  name: 'Summary',
  data () {
    return {
      name: 'jack',
      age: 10,
      data: {}
    }
  },
  computed: {
    msg: {
      get () {
        return this.name + this.age
      },
      set (val) {
      }
    }
  },
  methods: {
    change () {
      let params = {
        page: 1,
        'page-size': 3,
        group: ['cvd', 'pvd']
      }
      getOrders(params)
        .then((res) => {
          this.data = res.data.results
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style lang='stylus' scoped>

</style>
