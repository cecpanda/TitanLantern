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
        <el-menu-item index="/tft/order/audit">
          <i class='el-icon-star-on'></i>
          <span slot="title">
            待我审核
            <el-badge :value="0" :max="99" class="item">
            </el-badge>
          </span>
        </el-menu-item>
        <el-menu-item index="/tft/order">
          <i class='el-icon-picture-outline'></i>
          <span slot="title">图表统计</span>
        </el-menu-item>
        <!-- <el-menu-item index="/tft/order/query">
          <i class='el-icon-document'></i>
          <span slot="title">报表查询</span>
        </el-menu-item> -->
        <el-submenu index="/tft/order/query" class='query'>
          <template slot="title">
            <i class="el-icon-document"></i>
            <router-link to='/tft/order/query'>
              <span>报表查询</span>
            </router-link>
          </template>
          <el-menu-item index="/tft/order/mystart">我的停机单</el-menu-item>
          <el-menu-item index="2-4-2">我的复机单</el-menu-item>
          <el-menu-item index="2-4-2">我的审核单</el-menu-item>
        </el-submenu>
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
      isCollapse: true,
      defaultActive: '',
      activeMenu: ''
    }
  },
  methods: {
    handleSelect (index, indexPath) {
    },
    handleOpen (key, keyPath) {
    },
    handleClose (key, keyPath) {
    }
  }
}
</script>

<style lang='stylus' scoped>
.active-menu
  font-size 0.9rem
.el-main
.el-aside
  border 1px dashed #283D52
  min-height 550px
.el-menu-vertical-demo:not(.el-menu--collapse)
  width: 200px
.query
  a
    text-decoration none
    color #333
</style>
