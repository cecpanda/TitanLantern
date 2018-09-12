<template>
  <div>
    <h1>复机单 - 待审核</h1>
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
            :to="'/tft/order/detail/' + scope.row.id"
            target='_blank'
            class='id-href'
          >
            {{ scope.row.id }}
          </router-link>
        </template>
      </el-table-column>
      <el-table-column prop="status.desc" label="状态" min-width='180'></el-table-column>
      <el-table-column label="序号" min-width='60'>
        <template slot-scope="scope">
          {{ scope.$index + 1 }}
        </template>
      </el-table-column>
      <!-- <el-table-column label="申请人" min-width='80'>
        <template slot-scope="scope">
          {{ recoverorders[scope.$index].user.username }}
        </template>
      </el-table-column>
      <el-table-column label="申请时间" min-width='150'>
        <template slot-scope="scope">
          {{ recoverorders[scope.$index].created | formatDate }}
        </template>
      </el-table-column>
      <el-table-column label="修改人" min-width='80'>
        <template slot-scope="scope">
          {{ recoverorders[scope.$index].mod_user.username }}
        </template>
      </el-table-column>
      <el-table-column label="修改时间" min-width='150'>
        <template slot-scope="scope">
          {{ recoverorders[scope.$index].modified | formatDate }}
        </template>
      </el-table-column>
      <el-table-column label="责任单位对策说明" min-width='150' show-overflow-tooltip>
        <template slot-scope="scope">
          {{ recoverorders[scope.$index].solution }}
        </template>
      </el-table-column>
      <el-table-column label="先行 lot 结果说明" min-width='150' show-overflow-tooltip>
        <template slot-scope="scope">
          {{ recoverorders[scope.$index].explain }}
        </template>
      </el-table-column>
      <el-table-column label="部分复机" min-width='100'>
        <template slot-scope="scope">
          <span v-if='recoverorders[scope.$index].partial'>是</span>
          <span v-else>否</span>
        </template>
      </el-table-column> -->
    </el-table>
    总数: {{ this.count }}
    <!-- <el-pagination
      background
      @current-change="handleCurrentChange"
      :current-page.sync="page"
      :page-size='pageSize'
      layout="total, prev, pager, next, jumper"
      :total="count">
    </el-pagination> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getOrders } from '@/api/tft'
import { getUser } from '@/api/user'
import { formatDate } from '@/common/js/date.js'

export default {
  name: 'ToRecoverAudit',
  data () {
    return {
      // page: 1,
      // pageSize: 15,
      count: null,
      group: {},
      orders: []
    }
  },
  computed: {
    ...mapGetters({
      username: 'username'
    })
    // recoverorders () {
    //   return this.orders.length ? this.orders[0].recoverorders : []
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

      if (this.group.name === 'QC') {
        params = {status: 5}
      } else if (this.group.name === 'MFG') {
        params = {status: 6}
      }

      if (params) {
        getOrders(params)
          .then((res) => {
            this.count = res.data.count
            // 这是没有办法的事情，防止后端的默认分页小于此处应有的数据
            getOrders(params)
              .then((res) => {
                this.orders = res.data.results
              })
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    // handleCurrentChange (val) {
    //   this.getOrders()
    // },
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
