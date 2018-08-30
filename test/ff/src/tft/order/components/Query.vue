<template>
  <div class='table'>
    <h1>报表查询</h1>
    <el-row class='search'>
      <el-col :span='12'>
        <el-input v-model='search' placeholder="请输入内容" @keyup.enter.native='searching'>
          <el-select v-model="select" slot="prepend" placeholder="请选择">
            <el-option-group
              v-for="group in selectOptions"
              :key="group.label"
              :label="group.label"
            >
              <el-option
                v-for='option in group.options'
                :label="option.label"
                :value="option.value"
                :key='option.label'
              ></el-option>
            </el-option-group>
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
      <el-col :span='11' :offset='1'>
        <el-date-picker
          v-model="created"
          type="datetimerange"
          :picker-options="pickerClock"
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
          align="right">
        </el-date-picker>
      </el-col>
    </el-row>
    <el-row
      v-if='searchFlag && Object.getOwnPropertyNames(this.searchText).length'
      class='searchConent'
    >
      <el-col :span='12' :offset='12'>
        <i class="el-icon-info"></i> {{ searchText.label }}: {{ searchText.text }} <br>
        <i class="el-icon-info"></i> 数量: {{ count }} <br>
        <i class="el-icon-time"></i> 开始时间: {{ this.showCreatedAfter | formatDate }} <br>
        <i class="el-icon-time"></i> 结束时间: {{ this.showCreatedBefore | formatDate }}
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
      <el-table-column prop="found_step" label="发现站点" min-width='100' :show-overflow-tooltip='true'></el-table-column>
      <el-table-column prop="found_time" label="发现时间" :formatter='formatDate' min-width='150'></el-table-column>
      <el-table-column
        prop="charge_group.name"
        label="责任工程"
        min-width='100'
        :filters='chargeGroupFilters'
        :filter-method='filterChargeGroup'
        column-key='charge_group'
      ></el-table-column>
      <el-table-column prop="eq" label="停机设备" min-width='100' :show-overflow-tooltip='true'></el-table-column>
      <el-table-column prop="kind" label="停机机种" min-width='100' :show-overflow-tooltip='true'></el-table-column>
      <el-table-column prop="step" label="停机站点" min-width='100' :show-overflow-tooltip='true'></el-table-column>
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
import DetailDialog from './DetailDialog'

export default {
  name: 'Query',
  data () {
    return {
      page: 1,
      pageSize: 3,
      count: null,
      orders: [],
      // 留意 methods 中的 valueToLabel
      selectOptions: [{
        label: '模糊匹配',
        options: [
          {label: '所有', value: 'all'}
        ]
      }, {
        label: '精确匹配',
        options: [
          {label: '工号', value: 'username'},
          {label: '真名', value: 'realname'},
          {label: '开单工程', value: 'group'},
          {label: '责任工程', value: 'charge_group'}
        ]
      }],
      search: '',
      select: 'all',
      searchFlag: false,
      // 上次搜索的内容，直接使用 search 会出现动态效果,如 {label: '', value: '', text: ''}
      searchText: {},
      ordering: '',
      // {group: {'cvd', 'pvd'}, charge_group: {'cvd', 'pvd'}}
      filters: {},
      filterFlag: false,
      // search clock
      pickerClock: {
        shortcuts: [{
          text: '最近一周',
          onClick (picker) {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 7)
            picker.$emit('pick', [start, end])
          }
        }, {
          text: '最近一个月',
          onClick (picker) {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 30)
            picker.$emit('pick', [start, end])
          }
        }, {
          text: '最近三个月',
          onClick (picker) {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 90)
            picker.$emit('pick', [start, end])
          }
        }]
      },
      created: '',
      showCreatedAfter: '',
      showCreatedBefore: ''
    }
  },
  computed: {
    created_after () {
      return this.created ? this.created[0].toISOString() : undefined
    },
    created_before () {
      return this.created ? this.created[1].toISOString() : undefined
    },
    params () {
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
      // 从 handleCurrentChange 中转移来的，与上面重复
      // if (this.searchFlag && Object.getOwnPropertyNames(this.searchText).length) {
      //   for (let key in this.searchText) {
      //     if (this.searchText.hasOwnProperty(key)) {
      //       params[key] = this.searchText[key]
      //     }
      //   }
      // }
      if (this.ordering) {
        params.ordering = this.ordering
      }
      // 因为 object 的属性不能重复，需重写同一属性对应多个值的过滤 API
      // if (this.filterFlag && Object.keys(this.filters).length) {
      //   for (let label in Object.keys(this.filters)) {
      //     if (this.filters[label].size) {
      //       this.filters[label].forEach((val) => {

      //       })
      //     }
      //   }
      // }
      if (this.created_after) {
        params.created_after = this.created_after
      }
      if (this.created_before) {
        params.created_before = this.created_before
      }
      return params
    },
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
        message: `<ul>
                    <li>全部忽略大小写</li>
                    <li>所有：包括工号、真名</li>
                    <li>表格头部：当前表格中的当前页的数据</li>
                    <li>其他: 搜索出的内容不再分页</li>
                  </ul>
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
      // this.$router.push({path: `/tft/order/detail/${row.id}`})
      this.visible = true
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
    // 根据 selectOption 中的 value 得到对应的 label，用来渲染
    valueToLabel (val) {
      // return 不能终止 forEach 循环,
      let label = ''
      this.selectOptions.forEach((selectOption) => {
        selectOption.options.forEach((option) => {
          if (option.value === val) {
            label = option.label
          }
        })
      })
      return label
    },
    searching () {
      // 搜索后，从第一页开始显示
      this.page = 1
      // let params = {page: this.page, 'page-size': this.pageSize}
      // if (this.select === 'username') {
      //   params.username = this.search
      // } else if (this.select === 'realname') {
      //   params.realname = this.search
      // } else if (this.select === 'group') {
      //   params.group = this.search
      // } else if (this.select === 'charge_group') {
      //   params.charge_group = this.search
      // } else {
      //   params.search = this.search
      // }
      getOrders(this.params)
        .then((res) => {
          // searchFlag
          this.searchFlag = true
          this.searchText = {} // 清空
          // searchText: {label: '', value: '', text: ''}
          let label = this.valueToLabel(this.select)
          this.searchText = {label: label, value: this.select, text: this.search}
          this.count = res.data.count
          // this.orders = res.data.results
          this.showCreatedAfter = this.created_after
          this.showCreatedBefore = this.created_before
          this.orders = []
          this.pageSize = res.data.count
          getOrders(this.params)
            .then((res) => {
              this.orders = res.data.results
            })
        })
        .catch((error) => {
          console.log(error)
        })
    },
    handleCurrentChange (val) {
      // let params = {page: this.page, 'page-size': this.pageSize}
      // if (this.searchFlag && Object.getOwnPropertyNames(this.searchText).length) {
      //   for (let key in this.searchText) {
      //     if (this.searchText.hasOwnProperty(key)) {
      //       params[key] = this.searchText[key]
      //     }
      //   }
      // }
      // if (this.ordering) {
      //   params.ordering = this.ordering
      // }
      getOrders(this.params)
        .then((res) => {
          this.count = res.data.count
          this.orders = res.data.results
        })
    },
    sortChange ({column, prop, order}) {
      // let params = {page: this.page, 'page-size': this.pageSize}
      // if (this.searchFlag && Object.getOwnPropertyNames(this.searchText).length) {
      //   for (let key in this.searchText) {
      //     if (this.searchText.hasOwnProperty(key)) {
      //       params[key] = this.searchText[key]
      //     }
      //   }
      // }
      if (order === 'descending') {
        prop = '-' + prop
      }
      this.ordering = prop
      // params.ordering = prop
      getOrders(this.params)
        .then((res) => {
          this.count = res.data.count
          this.orders = res.data.results
        })
        .catch((error) => {
          console.log(error)
        })
    },
    filterGroup (value, row, column) {
      // console.log('value:', value)
      // console.log('row:', row)
      // console.log('column:', column)
      return row.group.name === value
    },
    filterChargeGroup (value, row, column) {
      return row.charge_group.name === value
    },
    filterChange (filters) {
      console.log('change')
      // filters = {group: ['cvd', 'pvd']}
      this.filterFlag = true
      for (let key of (Object.keys(filters))) {
        this.filters[key] = new Set()
        filters[key].forEach((val) => {
          this.filters[key].add(val)
        })
      }
      // this.filters = {group: {'cvd', 'pvd'}, charge_group: {'cvd', 'pvd'}}
      // 同一属性对应多个值的过滤 API
      // console.log(this.filters)
    }
  },
  filters: {
    formatDate (time) {
      let date = new Date(time)
      return formatDate(date, 'yyyy-MM-dd hh:mm:ss')
    }
  },
  components: {
    DetailDialog
  },
  mounted () {
    this.getOrders(this.params)
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
.id-href
  text-decoration none
  color #22558B
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
.el-pagination
  margin 20px 0
</style>
