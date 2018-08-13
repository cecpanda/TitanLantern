<template>
  <el-container>
    <el-main>
      <router-view></router-view>
    </el-main>
    <el-aside width="">
      <el-menu
        class="el-menu-vertical-demo"
        @select="handleSelect"
        @open="handleOpen"
        @close="handleClose"
        :collapse="isCollapse"
        :router='true'
      >
        <el-menu-item index="/tft/order/start">
          <i class='el-icon-edit'></i>
          <span slot="title">
            我要开单
          </span>
        </el-menu-item>
        <el-menu-item index="/tft/order/mystart">
          <i class='el-icon-edit'></i>
          <span slot="title">
            我的开单
          </span>
        </el-menu-item>
        <el-menu-item index="/tft/order/audit">
          <i class='el-icon-star-on'></i>
          <span slot="title">
            待我审核
            <el-badge :value="0" :max="99" class="item">
            </el-badge>
          </span>
        </el-menu-item>
        <el-menu-item index="/tft/order">
          <i class='el-icon-document'></i>
          <span slot="title">summary</span>
        </el-menu-item>
        <el-menu-item index="/tft/order/query">
          <i class='el-icon-document'></i>
          <span slot="title">报表查询</span>
        </el-menu-item>
        <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
          <el-radio-button :label="false" v-if='isCollapse'>
            <i class='el-icon-d-arrow-left'></i>
          </el-radio-button>
          <el-radio-button :label="true" v-else>
            <i class='el-icon-d-arrow-right'></i>
          </el-radio-button>
        </el-radio-group>
      </el-menu>
    </el-aside>
  </el-container>
</template>

<script>
export default {
  name: 'Order',
  data () {
    return {
      isCollapse: false,
      defaultActive: '',
      activeMenu: ''
    }
  },
  methods: {
    handleSelect (index, indexPath) {
      console.log(index, indexPath)
    },
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style lang='stylus' scoped>
.active-menu
  font-size 0.9rem
.el-main
.el-aside
  border 1px solid #283D52
  min-height 550px
.el-menu-vertical-demo:not(.el-menu--collapse)
  width: 200px
</style>
