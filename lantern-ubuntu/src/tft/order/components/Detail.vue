<template>
  <div>
    <el-row>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
        <h1>设备品质异常停机单</h1>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>编号</el-col>
        <el-col :span='16' class='content'>{{ order.id }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>状态</el-col>
        <el-col :span='16' class='content'>{{ order.status.desc }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>开单工程</el-col>
        <el-col :span='16' class='content'>{{ order.group.name }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>开单人员</el-col>
        <el-col :span='16' class='content'>{{ order.user.username }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>开单时间</el-col>
        <el-col :span='16' class='content'>{{ order.created | formatDate}}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>修改人员</el-col>
        <el-col :span='16' class='content'>{{ order.mod_user.username}}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>修改时间</el-col>
        <el-col :span='16' class='content'>{{ order.modified | formatDate}}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>发现站点</el-col>
        <el-col :span='16' class='content'>{{ order.found_step }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>发现时间</el-col>
        <el-col :span='16' class='content'>{{ order.found_time | formatDate }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>责任工程</el-col>
        <el-col :span='16' class='content'>{{ order.charge_group.name }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>停机设备</el-col>
        <el-col :span='16' class='content'>{{ order.eq }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>停机机种</el-col>
        <el-col :span='16' class='content'>{{ order.kind }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>停机站点</el-col>
        <el-col :span='16' class='content'>{{ order.step }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>停机原因</el-col>
        <el-col :span='16' class='content'>{{ order.reason }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>通知生产人员</el-col>
        <el-col :span='16' class='content'>{{ order.users}}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>通知制程人员</el-col>
        <el-col :span='16' class='content'>{{ order.charge_users }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>异常描述</el-col>
        <el-col :span='16' class='content'>{{ order.desc }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>受害开始时间</el-col>
        <el-col :span='16' class='content'>{{ order.start_time | formatDate }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>受害结束时间</el-col>
        <el-col :span='16' class='content'>{{ order.end_time | formatDate }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>受害批次数</el-col>
        <el-col :span='16' class='content'>{{ order.lot_num }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>异常批次/基板</el-col>
        <el-col :span='16' class='content'>{{ order.lots }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>复机条件</el-col>
        <el-col :span='16' class='content'>{{ order.condition }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>绝对不良</el-col>
        <el-col :span='16' class='content'>{{ order.defect_type }}</el-col>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { getOrder } from '@/api/tft'
import { formatDate } from '@/common/js/date.js'

export default {
  name: 'Detail',
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      order: {
        user: {},
        status: {},
        mod_user: {},
        group: {},
        charge_group: []
      }
    }
  },
  methods: {
    getOrder () {
      getOrder(this.id)
        .then((res) => {
          this.order = res.data
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  filters: {
    formatDate (time) {
      let date = new Date(time)
      return formatDate(date, 'yyyy-MM-dd hh:mm:ss')
    }
  },
  mounted () {
    this.getOrder()
  }
}

</script>

<style lang='stylus' scoped>
.el-row
  // margin 10px 0
.el-col
  // border 1px dashed #5098E3
.el-form-item
  word-break break-all
.label
  font-size 1rem
  // border 1px solid red
  text-align right
  min-height 1rem
  line-height 1rem
  margin-bottom 20px
  word-break break-all
  word-wrap break-word
.content
  // border 1px solid red
  font-size .8rem
  text-align left
  min-height 1rem
  line-height 1rem
  margin-bottom 20px
  padding-left 0.5rem
  word-break break-all
  word-wrap break-word
</style>
