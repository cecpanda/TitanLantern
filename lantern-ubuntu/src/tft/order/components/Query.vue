<template>
  <div class='table'>
    <h1>报表查询</h1>
    <el-table
      :data="orders"
      style="width: 100%"
      border
      header-row-class-name='table-header'
      @row-dblclick='rowdbClick'
      :row-class-name="tableRowClassName"
      @cell-mouse-enter='cellMouseEnter'
      @cell-mouse-leave='cellMouseLeave'
      @sort-change='sortChange'
      @filter-change='filterChange'
    >
      <el-table-column prop="id" label="编号" min-width='100'></el-table-column>
      <el-table-column prop="status.desc" label="状态" min-width='180'></el-table-column>
      <el-table-column prop="user.username" label="开单人"></el-table-column>
      <el-table-column
        prop="group.name"
        label="开单工程"
        min-width='100'
        :filters='groupFilters'
        :filter-method='filterGroup'
        column-key='group'
      ></el-table-column>
      <el-table-column prop="created" label="开单时间" :formatter='formatDate' min-width='150' sortable='custom'></el-table-column>
      <!-- <el-table-column prop="mod_user" label="修改人"></el-table-column>
      <el-table-column prop="modified" label="修改时间"  :formatter='formatDate'></el-table-column> -->
      <el-table-column prop="found_step" label="发现站点" min-width='100'></el-table-column>
      <el-table-column prop="found_time" label="发现时间" :formatter='formatDate' min-width='150'></el-table-column>
      <el-table-column
        prop="charge_group.name"
        label="责任工程"
        min-width='100'
        :filters='chargeGroupFilters'
        :filter-method='filterChargeGroup'
      ></el-table-column>
      <el-table-column prop="eq" label="停机设备" min-width='100'></el-table-column>
      <el-table-column prop="kind" label="停机机种" min-width='100'></el-table-column>
      <el-table-column prop="step" label="停机站点" min-width='100'></el-table-column>
      <el-table-column prop="defect_type" label="绝对不良" min-width='100'></el-table-column>
      <el-table-column prop="remarks[0].content" label="最新批注" min-width='100'></el-table-column>
    </el-table>
    <el-pagination
      background
      @current-change="handleCurrentChange"
      :current-page.sync="page"
      :page-size='pageSize'
      layout="prev, pager, next, jumper"
      :total="count"
    >
    </el-pagination>
  </div>
</template>

<script>
import { formatDate } from '@/common/js/date.js'
import { getOrders } from '@/api/tft'

export default {
  name: 'Query',
  data () {
    return {
      page: 1,
      pageSize: 10,
      count: null,
      orders: []
    }
  },
  computed: {
    groupFilters () {
      let filters = []
      let values = new Set()
      this.orders.forEach((order) => {
        values.add(order.group.name)
      })
      values.forEach((value) => {
        filters.push({text: value, value: value})
      })
      return filters
    },
    chargeGroupFilters () {
      let filters = []
      let values = new Set()
      this.orders.forEach((order) => {
        values.add(order.charge_group.name)
      })
      values.forEach((value) => {
        filters.push({text: value, value: value})
      })
      return filters
    }
  },
  methods: {
    getOrders () {
      getOrders(this.page, this.pageSize)
        .then((res) => {
          this.count = res.data.count
          this.orders = res.data.results
        })
        .catch((error) => {
          console.log(error)
        })
    },
    handleCurrentChange (val) {
      this.getOrders()
    },
    formatDate (row, column, time, index) {
      let date = new Date(time)
      return formatDate(date, 'yyyy-MM-dd hh:mm:ss')
    },
    rowdbClick (row, event) {
      this.$router.push({path: `/tft/order/detail/${row.id}`})
    },
    tableRowClassName ({row, rowIndex}) {
      if (row.status.code === '0') {
        return 'status0'
      } else if (row.status.code === '1') {
        return 'status1'
      } else if (row.status.code === '2') {
        return 'status2'
      } else if (row.status.code === '3') {
        return 'status3'
      } else if (row.status.code === '4') {
        return 'status4'
      } else if (row.status.code === '5') {
        return 'status5'
      } else if (row.status.code === '6') {
        return 'status6'
      } else if (row.status.code === '7') {
        return 'status7'
      } else if (row.status.code === '8') {
        return 'status8'
      } else if (row.status.code === '9') {
        return 'status9'
      }
      return 'status0'
    },
    rowStyle ({row, rowIndex}) {
    },
    cellMouseEnter (row, column, cell, event) {
    },
    cellMouseLeave (row, column, cell, event) {
    },
    sortChange ({column, prop, order}) {
      console.log(order)
      if (order === 'descending') {
        prop = '-' + prop
      }
      getOrders(this.page, this.pageSize, prop)
        .then((res) => {
          this.orders = res.data.results
          this.count = res.data.count
        })
        .catch((error) => {
          console.log(error)
        })
    },
    filterGroup (value, row, column) {
      console.log('filter')
      return row.group.name === value
    },
    filterChargeGroup (value, row, column) {
      return row.charge_group.name === value
    },
    filterChange (filters) {
      console.log('filters')
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

<style lang='stylus'>
@import '~styles/varibles'
.table-header
  th
    font-size 1.1em
    background #CFD5DA
.el-table
  td
    div
      max-height 2.2em
      overflow hidden
      white-space nowrap
      text-overflow ellipsis
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
</style>
