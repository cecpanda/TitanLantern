<template>
  <div>
    <h1>停机单 - 待我审核</h1>
    <p>如果修改了生产科的名字，记得更改这里的代码</p>
    <el-table
      :data="orders"
      style="width: 100%"
      border
      header-row-class-name='table-header'
    >
      <el-table-column label="编号" min-width='100'>
        <template slot-scope="scope">
          <router-link
            :to="'/tft/order/detail/' + scope.row.id"
            target='_blank'
            class='id-href'
          >
            {{ scope.row.id }}
          </router-link>
        </template>
      </el-table-column>
      <el-table-column prop="status.desc" label="状态" width='180'></el-table-column>
      <el-table-column prop="user.username" label="开单人"></el-table-column>
      <el-table-column prop="group.name" label="开单工程" min-width='100'></el-table-column>
      <el-table-column prop="created" label="开单时间" :formatter='formatDate' min-width='150'></el-table-column>
      <el-table-column prop="mod_user.username" label="修改人" width='100'></el-table-column>
      <el-table-column prop="modified" label="修改时间"  :formatter='formatDate' width='150'></el-table-column>
      <el-table-column prop="found_step" label="发现站点" min-width='100' :show-overflow-tooltip='true'></el-table-column>
      <el-table-column prop="found_time" label="发现时间" :formatter='formatDate' min-width='150'></el-table-column>
      <el-table-column prop="charge_group.name" label="责任工程" min-width='100'></el-table-column>
      <el-table-column prop="eq" label="停机设备" min-width='100' :show-overflow-tooltip='true'></el-table-column>
      <el-table-column prop="kind" label="停机机种" min-width='100' :show-overflow-tooltip='true'></el-table-column>
      <el-table-column prop="step" label="停机站点" min-width='100' :show-overflow-tooltip='true'></el-table-column>
      <el-table-column label="绝对不良" min-width='100'>
        <template slot-scope="scope">
          <span v-if='scope.row.defect_type'>是</span>
          <span v-else-if='scope.row.defect_type === false'>否</span>
          <span v-else></span>
        </template>
      </el-table-column>
      <el-table-column prop="remarks[0].content" label="最新批注" min-width='100'></el-table-column>
    </el-table>
    <el-pagination
      background
      @current-change="handleCurrentChange"
      :current-page.sync="page"
      :page-size='pageSize'
      layout="total, prev, pager, next, jumper"
      :total="count">
    </el-pagination>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getOrders } from '@/api/tft'
import { getUser } from '@/api/user'
import { formatDate } from '@/common/js/date.js'

export default {
  name: 'ToAudit',
  data () {
    return {
      page: 1,
      pageSize: 15,
      count: null,
      group: {},
      orders: []
    }
  },
  computed: {
    ...mapGetters({
      username: 'username'
    })
    // params () {
    //   if (this.group.name === 'MFG') {
    //     return {status: 1, page: this.page, 'page-size': this.pageSize}
    //   } else if (this.group.name) {
    //     return {status: 2, charge_group: this.group.name, page: this.page, 'page-size': this.pageSize}
    //   }
    // }
  },
  methods: {
    async getGroup () {
      await getUser(this.username)
        .then((res) => {
          // 只要第一个组
          let groups = res.data.groups
          if (groups.length) {
            this.group = groups[0]
          } else {
            this.group = {}
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    async getOrders () {
      await this.getGroup()

      let params

      if (this.group.name === 'MFG') {
        params = {status: 1, page: this.page, 'page-size': this.pageSize}
      } else if (this.group.name) {
        params = {status: 2, charge_group: this.group.name, page: this.page, 'page-size': this.pageSize}
      }

      if (params) {
        getOrders(params)
          .then((res) => {
            this.count = res.data.count
            this.orders = res.data.results
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    handleCurrentChange (val) {
      this.getOrders()
    },
    formatDate (row, column, time, index) {
      let date = new Date(time)
      return formatDate(date, 'yyyy-MM-dd hh:mm:ss')
    }
  },
  filters: {
    formatDate (time) {
      let date = new Date(time)
      return formatDate(date, 'yyyy-MM-dd hh:mm:ss')
    }
  },
  mounted () {
    this.getOrders()
  }
}
</script>

<style lang="stylus">
@import '~styles/varibles'
.table-header
  th
    font-size 1.1em
    background #CFD5DA
.id-href
  text-decoration none
  color #22558B
.el-table
  td
    div
      max-height 2.2em
      // overflow hidden
      // white-space nowrap
      // text-overflow ellipsis
.el-pagination
  margin 20px 0
</style>
