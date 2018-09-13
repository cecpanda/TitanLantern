<template>
  <div>
    <h1>我的复机审核</h1>
    <el-table
      :data="orders"
      style="width: 100%"
      border
      header-row-class-name='table-header'
      @row-dblclick='rowdbClick'
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
import { formatDate } from '@/common/js/date.js'
import { getRecoverOrders } from '@/api/tft'

export default {
  name: 'MyRecoverAudit',
  data () {
    return {
      page: 1,
      pageSize: 15,
      count: null,
      orders: []
    }
  },
  computed: {
    ...mapGetters({
      username: 'username'
    })
  },
  methods: {
    getOrders () {
      getRecoverOrders({page: this.page, 'page-size': this.pageSize, audit_signer: this.username})
        .then((res) => {
          this.count = res.data.count
          this.orders = res.data.results
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // tableRowClassName ({row, rowIndex}) {
    //   if (row.status.code === '0') {
    //     return 'status0'
    //   } else if (row.status.code === '1') {
    //     return 'status1'
    //   } else if (row.status.code === '2') {
    //     return 'status2'
    //   } else if (row.status.code === '3') {
    //     return 'status3'
    //   } else if (row.status.code === '4') {
    //     return 'status4'
    //   } else if (row.status.code === '5') {
    //     return 'status5'
    //   } else if (row.status.code === '6') {
    //     return 'status6'
    //   } else if (row.status.code === '7') {
    //     return 'status7'
    //   } else if (row.status.code === '8') {
    //     return 'status8'
    //   } else if (row.status.code === '9') {
    //     return 'status9'
    //   }
    //   return 'status0'
    // },
    handleCurrentChange (val) {
      this.getOrders()
    },
    formatDate (row, column, time, index) {
      let date = new Date(time)
      return formatDate(date, 'yyyy-MM-dd hh:mm:ss')
    },
    rowdbClick (row, event) {
      // this.$router.push({path: `/tft/order/detail/${row.id}`})
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
  .status0
    background $status0
  .status1
    background $status1
  .status2
    background $status2
  .status3
    background $status3
  .status4
    background $status4
  .status5
    background $status5
  .status6
    background $status6
  .status7
    background $status7
  .status8
    background $status8
  .status9
    background $status9
.status0:hover
.status1:hover
.status2:hover
.status3:hover
.status4:hover
.status5:hover
.status6:hover
.status7:hover
.status8:hover
.status9:hover
  font-weight bold
.el-pagination
  margin 20px 0
</style>
