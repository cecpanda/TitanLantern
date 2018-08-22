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
        <el-col :span='16' class='content'>
          <span v-if='order.mod_user'>{{ order.mod_user.username}}</span>
          <span v-else></span>
        </el-col>
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
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>调查报告</el-col>
        <el-col :span='16' class='content'>
          <span
            v-for='(url, name, index) in order.reports'
            :key='index'
          >
            <a :href='url'>{{ name }}</a> <br>
          </span>
        </el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
        <el-col :span='8' class='label'>批注</el-col>
        <el-col :span='16' class='content'>
          <span
            v-for='(remark, index) in order.remarks'
            :key='index'
          >
            {{ remark.content }} <br>
          </span>
        </el-col>
      </el-col>
    </el-row>

    <el-row v-if="canBeUpdated">
      <el-button type="primary">修改</el-button>
    </el-row>

    <el-row>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
        <h3>停机签核</h3>
      </el-col>
    </el-row>
    <el-row v-if='order.startaudit'>
      <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>生产领班签核</el-col>
        <el-col :span='16' class='content'>
          {{ order.startaudit.p_signer.username }}
        </el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>生产签字时间</el-col>
        <el-col :span='16' class='content'>{{ order.startaudit.p_time | formatDate }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>Recipe关闭人员</el-col>
        <el-col :span='16' class='content'>{{ order.startaudit.recipe_close }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>Recipe确认人员</el-col>
        <el-col :span='16' class='content'>{{ order.startaudit.recipe_confirm }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>责任工程签字</el-col>
        <el-col :span='16' class='content'>{{ order.startaudit.c_signer.username }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>工程签字时间</el-col>
        <el-col :span='16' class='content'>{{ order.startaudit.c_time | formatDate }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>是否拒签</el-col>
        <el-col :span='16' class='content'>{{ order.startaudit.rejected }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>拒签理由</el-col>
        <el-col :span='16' class='content'>{{ order.startaudit.reason }}</el-col>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
        <h1>设备品质异常复机单</h1>
      </el-col>
    </el-row>
    <div
      v-for='(recoverorder, index) in order.recoverorders'
      :key='index'
    >
      <el-row>
        <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
          <h4>复机单-{{ index }}</h4>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='12'>
          <el-col :span='8' class='label'>申请人</el-col>
          <el-col :span='16' class='content'>{{ recoverorder.user.username }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='12'>
          <el-col :span='8' class='label'>申请时间</el-col>
          <el-col :span='16' class='content'>{{ recoverorder.created | formatDate }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='12'>
          <el-col :span='8' class='label'>修改人</el-col>
          <el-col :span='16' class='content'>{{ recoverorder.mod_user.username }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='12'>
          <el-col :span='8' class='label'>修改时间</el-col>
          <el-col :span='16' class='content'>{{ recoverorder.modified | formatDate }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
          <el-col :span='4' class='label'>责任单位对策说明</el-col>
          <el-col :span='20' class='content'>{{ recoverorder.solution }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
          <el-col :span='4' class='label'>先行lot结果说明</el-col>
          <el-col :span='20' class='content'>{{ recoverorder.explain }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='6'>
          <el-col :span='8' class='label'>部分复机</el-col>
          <el-col :span='16' class='content'>{{ recoverorder.partial }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='6'>
          <el-col :span='8' class='label'>部分复机设备</el-col>
          <el-col :span='16' class='content'>{{ recoverorder.eq }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='6'>
          <el-col :span='8' class='label'>部分复机机种</el-col>
          <el-col :span='16' class='content'>{{ recoverorder.kind }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='12' :lg='12' :xl='6'>
          <el-col :span='8' class='label'>部分复机站点</el-col>
          <el-col :span='16' class='content'>{{ recoverorder.step }}</el-col>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
          <h6>审核</h6>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>工程品质签字</el-col>
          <el-col :span='16' class='content'>
            <span v-if='recoverorder.audit.qc_signer'>{{ recoverorder.audit.qc_signer.username }}</span>
          </el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>品质签复时间</el-col>
          <el-col :span='16' class='content'>{{ recoverorder.audit.qc_time | formatDate }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>生产领班签复</el-col>
          <el-col :span='16' class='content'>
            <span v-if='recoverorder.audit.p_signer'>{{ recoverorder.audit.p_signer.username }}</span>
          </el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>生产签复时间</el-col>
          <el-col :span='16' class='content'>{{ recoverorder.audit.p_time | formatDate }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>是否拒签</el-col>
          <el-col :span='16' class='content'>{{ recoverorder.audit.rejected }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>拒签理由</el-col>
          <el-col :span='16' class='content'>{{ recoverorder.audit.reason }}</el-col>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import { getOrder, canUpdate } from '@/api/tft'
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
        charge_group: [],
        startaudit: {
          p_signer: {},
          c_signer: {}
        }
      },
      canBeUpdated: false
    }
  },
  computed: {
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
    },
    canUpdate () {
      canUpdate(this.id)
        .then((res) => {
          console.log(res.data)
          this.canBeUpdated = res.data.can
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  filters: {
    formatDate (time) {
      let date = new Date(time)
      return formatDate(date, 'yyyy-MM-dd hh:mm:ss')
    }
  },
  beforeMount () {
    this.getOrder()
    this.canUpdate()
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
  background-color #C1C8CF
.content
  // border 1px solid red
  color #1B7FE5
  font-size .8rem
  text-align left
  min-height 1rem
  line-height 1rem
  margin-bottom 20px
  padding-left 0.5rem
  word-break break-all
  word-wrap break-word
</style>
