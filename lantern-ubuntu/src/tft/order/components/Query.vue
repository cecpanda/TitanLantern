<template>
  <div class='table'>
    <h1>报表查询</h1>
    <el-row class='search'>
      <el-col :span='12' :offset='12'>
        <el-input v-model='search' placeholder="请输入内容" @keyup.enter.native='searching'>
          <el-select v-model="select" slot="prepend" placeholder="请选择">
            <el-option
              v-for='(option, index) in selectOptions'
              :label="option.label"
              :value="option.value"
              :key='index'
            ></el-option>
          </el-select>
          <el-button
            slot="append"
            icon="el-icon-search"
            @click='searching'
          ></el-button>
          <el-button
            slot="append"
            icon="el-icon-message"
            @click="openSearchMsg"
          ></el-button>
        </el-input>
      </el-col>
    </el-row>
    <el-row v-if='searchFlag && searchText' class='searchConent'>
      <el-col :span='12' :offset='12'>
        搜索内容: {{ this.searchText }} <br>
        发现数量: {{ this.count }}
      </el-col>
    </el-row>
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
        column-key='charge_group'
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
      layout="total, prev, pager, next, jumper"
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
      pageSize: 3,
      count: null,
      orders: [],
      selectOptions: [
        {label: '所有', value: 'all'},
        {label: '工号', value: 'username'},
        {label: '真名', value: 'realname'},
        {label: '开单工程', value: 'group'},
        {label: '责任工程', value: 'charge_group'}
      ],
      search: '',
      select: 'all',
      searchFlag: false,
      searchText: '', // 上次搜索的内容，直接使用 search 会出现动态效果
      ordering: '',
      filters: {}
    }
  },
  computed: {
    groupFilters () {
      // 在分页下得到不想要的结果
      // 只能过滤本页，切换页后，过滤状态保留
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
      getOrders({page: this.page, 'page-size': this.pageSize})
        .then((res) => {
          this.count = res.data.count
          this.orders = res.data.results
        })
        .catch((error) => {
          console.log(error)
        })
    },
    openSearchMsg () {
      this.$notify({
        title: '检索说明',
        type: 'info',
        customClass: 'search-msg',
        dangerouslyUseHTMLString: true,
        message: `<strong>搜索</strong>：所有数据 <br>
                  <strong>所有</strong>：工号、真名的模糊匹配 <br>
                  <strong>其他</strong>：忽略大小写的精确匹配 <br><br>
                  <strong>过滤</strong>：当前表格中的所有页数据<br><br>
                  <strong>排序</strong>：当前表格中的所有页数据 <br>
                  `,
        position: 'top-left',
        offset: 150
      })
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
    searching () {
      // 搜索后，从第一页开始显示
      this.page = 1
      let params = {page: this.page, 'page-size': this.pageSize}
      if (this.select === 'username') {
        params.username = this.search
      } else if (this.select === 'realname') {
        params.realname = this.search
      } else if (this.select === 'group') {
        params.group = this.search
      } else if (this.select === 'charge_group') {
        params.charge_group = this.search
      } else {
        params.search = this.search
      }
      getOrders(params)
        .then((res) => {
          // searchFlag
          this.searchFlag = true
          this.searchText = this.search
          this.count = res.data.count
          this.orders = res.data.results
        })
        .catch((error) => {
          console.log(error)
        })
    },
    handleCurrentChange (val) {
      let params = {page: this.page, 'page-size': this.pageSize}
      if (this.searchFlag && this.searchText) {
        params.search = this.searchText
      }
      if (this.ordering) {
        params.ordering = this.ordering
      }
      getOrders(params)
        .then((res) => {
          this.count = res.data.count
          this.orders = res.data.results
        })
    },
    sortChange ({column, prop, order}) {
      let params = {page: this.page, 'page-size': this.pageSize}
      if (this.searchFlag && this.searchText) {
        params.search = this.searchText
      }
      if (order === 'descending') {
        prop = '-' + prop
      }
      this.ordering = prop
      params.ordering = prop
      getOrders(params)
        .then((res) => {
          this.count = res.data.count
          this.orders = res.data.results
        })
        .catch((error) => {
          console.log(error)
        })
    },
    filterGroup (value, row, column) {
      return true
      // return row.group.name === value
    },
    filterChargeGroup (value, row, column) {
      return row.charge_group.name === value
    },
    filterChange (filters) {
      console.log('change')
      console.log(filters)
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
.search
  margin 20px 0
  .el-select
    width 100px
.search-msg
  background rgba(255, 255, 255, 0.7)
.searchConent
  margin-bottom 20px
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
