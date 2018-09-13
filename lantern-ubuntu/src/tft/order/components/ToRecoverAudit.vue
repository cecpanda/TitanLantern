<template>
  <div>
    <h1>复机单 - 待我审核</h1>
    <p>如果修改了生产科、QC的名字，记得更改这里的代码</p>
    <el-table
      :data="orders"
      style="width: 100%"
      border
      header-row-class-name='table-header'
    >
      <el-table-column label="编号" min-width='100'>
        <template slot-scope="scope">
          <router-link
            :to="'/tft/order/detail/' + scope.row.order.id"
            target='_blank'
            class='id-href'
          >
            {{ scope.row.order.id }}
          </router-link>
        </template>
      </el-table-column>
      <el-table-column prop="order.status" label="状态" min-width='180'></el-table-column>
      <el-table-column prop="id" label="序号" min-width='60'></el-table-column>
      <el-table-column prop='user.username' label="申请人" min-width='80'></el-table-column>
      <el-table-column prop='mod_user.username' label="修改人" min-width='80'></el-table-column>
      <el-table-column label="部分复机" min-width='100'>
        <template slot-scope="scope">
          <span v-if='scope.row.partial'>是</span>
          <span v-else>否</span>
        </template>
      </el-table-column>
      <el-table-column prop='audit.qc_signer.username' label="工程品质签复" min-width='150'></el-table-column>
      <el-table-column prop='audit.qc_time' label="品质签复时间" :formatter='formatDate' min-width='150'></el-table-column>
      <el-table-column prop='audit.p_signer.username' label="生产领班签复" min-width='150'></el-table-column>
      <el-table-column prop='audit.p_time' label="生产签复时间" :formatter='formatDate' min-width='150'></el-table-column>
      <el-table-column label="是否拒签" min-width='100'>
        <template slot-scope="scope">
          <span v-if='scope.row.rejected'>是</span>
          <span v-else>否</span>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      background
      @current-change="handleCurrentChange"
      :current-page.sync="page"
      :page-size='pageSize'
      layout="prev, pager, next, jumper"
      :total="count">
    </el-pagination>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getRecoverOrders } from '@/api/tft'
import { getUser } from '@/api/user'
import { formatDate } from '@/common/js/date.js'

export default {
  name: 'ToRecoverAudit',
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

      if (this.group.name === 'QC') {
        params = {order__status: 5, page: this.page, 'page-size': this.pageSize}
      } else if (this.group.name === 'MFG') {
        params = {order__status: 6, page: this.page, 'page-size': this.pageSize}
      }

      if (params) {
        getRecoverOrders(params)
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
