<template>
  <div>
    <template>
      <el-table :data="orders" style="width: 100%" border stripe @row-dblclick='rowdbClick'>
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="table-expand">
              <el-form-item label="编号">
                <span>{{ props.row.id }}</span>
              </el-form-item>
              <el-form-item label="状态">
                <span>{{ props.row.status.desc }}</span>
              </el-form-item>
              <el-form-item label="开单人">
                <span>{{ props.row.user.username }}</span>
              </el-form-item>
              <el-form-item label="开单工程">
                <span>{{ props.row.group.name }}</span>
              </el-form-item>
              <el-form-item label="开单时间">
                <span>{{ props.row.created|formatDate }}</span>
              </el-form-item>
              <el-form-item label="修改人">
                <span>{{ props.row.mod_user }}</span>
              </el-form-item>
              <el-form-item label="修改时间">
                <span>{{ props.row.modified|formatDate }}</span>
              </el-form-item>
              <el-form-item label="发现站点">
                <span>{{ props.row.found_step }}</span>
              </el-form-item>
              <el-form-item label="发现时间">
                <span>{{ props.row.found_time|formatDate }}</span>
              </el-form-item>
              <el-form-item label="责任工程">
                <span>{{ props.row.charge_group.name }}</span>
              </el-form-item>
              <el-form-item label="停机设备">
                <span>{{ props.row.eq }}</span>
              </el-form-item>
              <el-form-item label="停机机种">
                <span>{{ props.row.kind }}</span>
              </el-form-item>
              <el-form-item label="停机设备">
                <span>{{ props.row.eq }}</span>
              </el-form-item>
              <el-form-item label="停机站点">
                <span>{{ props.row.step }}</span>
              </el-form-item>
              <el-form-item label="停机原因">
                <span>{{ props.row.reason }}</span>
              </el-form-item>
              <el-form-item label="通知生产人员">
                <span>{{ props.row.users }}</span>
              </el-form-item>
              <el-form-item label="通知制程人员">
                <span>{{ props.row.charge_users }}</span>
              </el-form-item>
              <el-form-item label="异常描述">
                <span>{{ props.row.desc }}</span>
              </el-form-item>
              <el-form-item label="受害开始时间">
                <span>{{ props.row.start_time|formatDate }}</span>
              </el-form-item>
              <el-form-item label="受害结束时间">
                <span>{{ props.row.end_time|formatDate }}</span>
              </el-form-item>
              <el-form-item label="受害批次数">
                <span>{{ props.row.lot_num }}</span>
              </el-form-item>
              <el-form-item label="异常批次/基板">
                <span>{{ props.row.lots }}</span>
              </el-form-item>
              <el-form-item label="复机条件">
                <span>{{ props.row.condition }}</span>
              </el-form-item>
              <el-form-item label="绝对不良">
                <span>{{ props.row.defect_type }}</span>
              </el-form-item>
              <el-form-item label="调查报告">
                <span v-for='(value, key) of props.row.reports' :key='key'>
                  <a :href='value'>{{ key }}</a> <br>
                </span>
              </el-form-item>
              <el-form-item label="最新批注">
                <span v-if='props.row.remarks.length'>{{ props.row.remarks[0].content }}</span>
                <span v-else></span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column prop="id" label="编号" width='100'></el-table-column>
        <el-table-column prop="status.desc" label="状态" width='180'></el-table-column>
        <el-table-column prop="user.username" label="开单人"></el-table-column>
        <el-table-column prop="group.name" label="开单工程"></el-table-column>
        <el-table-column prop="created" label="开单时间" :formatter='formatDate' width='150'></el-table-column>
        <!-- <el-table-column prop="mod_user" label="修改人"></el-table-column>
        <el-table-column prop="modified" label="修改时间"  :formatter='formatDate'></el-table-column> -->
        <el-table-column prop="found_step" label="发现站点"></el-table-column>
        <el-table-column prop="found_time" label="发现时间" :formatter='formatDate' width='150'></el-table-column>
        <el-table-column prop="charge_group.name" label="责任工程"></el-table-column>
        <el-table-column prop="eq" label="停机设备"></el-table-column>
        <el-table-column prop="kind" label="停机机种"></el-table-column>
        <el-table-column prop="step" label="停机站点"></el-table-column>
        <!-- <el-table-column prop="reason" label="停机原因"></el-table-column>
        <el-table-column prop="users" label="通知生产人员"></el-table-column>
        <el-table-column prop="charge_users" label="通知制程人员"></el-table-column>
        <el-table-column prop="desc" label="异常描述"></el-table-column>
        <el-table-column prop="start_time" label="受害开始时间"></el-table-column>
        <el-table-column prop="end_time" label="受害结束时间"></el-table-column>
        <el-table-column prop="lot_num" label="受害批次数"></el-table-column>
        <el-table-column prop="lots" label="异常批次/基板"></el-table-column>
        <el-table-column prop="condition" label="复机条件"></el-table-column> -->
        <el-table-column prop="defect_type" label="绝对不良"></el-table-column>
        <!-- <el-table-column prop="reports" label="调查报告"></el-table-column> -->
        <el-table-column prop="remarks[0].content" label="最新批注"></el-table-column>
      </el-table>
    </template>
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
import { getUserOrders } from '@/api/tft'

export default {
  name: 'MyStart',
  data () {
    return {
      page: 1,
      pageSize: 10,
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
      getUserOrders(this.page, this.pageSize, this.username)
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

<style lang="stylus" scoped>
.table-expand
  font-size: 0
.table-expand label
  width 90px
  color #5AA1EB
.table-expand .el-form-item
  margin-right: 10px
  margin-bottom: 0
  width: 23%
  overflow hidden
  text-overflow ellipsis
  white-space nowrap
  word-break keep-all
  span
    color #5AA1E2
</style>
