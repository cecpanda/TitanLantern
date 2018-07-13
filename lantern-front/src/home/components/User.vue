<template>
  <el-button plain @click="open12">
    用户
  </el-button>
</template>

<script>
export default {
  name: 'User',
  methods: {
    open12 () {
      this.$notify({
        title: '用户',
        dangerouslyUseHTMLString: true,
        message: `<ul>
                    <router-link to='/'><li>1</li></router-link>
                    <li>2</li>
                  </ul>`
      })
    }
  }
}
</script>

<style lang="stylus" scoped>
</style>
