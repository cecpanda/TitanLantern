<template>
  <div>
    <div class="order">
      <el-row>
        <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
          <h1 class='title'>设备品质异常停机单</h1>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>编号</el-col>
          <el-col :span='16' class='content'>{{ order.id }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>状态</el-col>
          <el-col :span='16' class='content'>{{ order.status.desc }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>开单工程</el-col>
          <el-col :span='16' class='content'>{{ order.group.name }}</el-col>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>开单人员</el-col>
          <el-col :span='16' class='content'>
            {{ order.user.username }} {{ order.user.realname }}
          </el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>开单时间</el-col>
          <el-col :span='16' class='content'>{{ order.created | formatDate}}</el-col>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>修改人员</el-col>
          <el-col :span='16' class='content'>
            <span v-if='order.mod_user'>
              {{ order.mod_user.username}} {{ order.mod_user.realname }}
            </span>
            <span v-else></span>
          </el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>修改时间</el-col>
          <el-col :span='16' class='content'>{{ order.modified | formatDate}}</el-col>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>发现站点</el-col>
          <el-col :span='16' class='content'>{{ order.found_step }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>发现时间</el-col>
          <el-col :span='16' class='content'>{{ order.found_time | formatDate }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>责任工程</el-col>
          <el-col :span='16' class='content'>{{ order.charge_group.name }}</el-col>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>停机设备</el-col>
          <el-col :span='16' class='content'>{{ order.eq }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>停机机种</el-col>
          <el-col :span='16' class='content'>{{ order.kind }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>停机站点</el-col>
          <el-col :span='16' class='content'>{{ order.step }}</el-col>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='24' :md='24' :lg='16' :xl='16'>
          <el-col :span='4' class='label'>停机原因</el-col>
          <el-col :span='20' class='content'>{{ order.reason }}</el-col>
        </el-col>
        <!-- <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>通知生产人员</el-col>
          <el-col :span='16' class='content'>{{ order.users}}</el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>通知制程人员</el-col>
          <el-col :span='16' class='content'>{{ order.charge_users }}</el-col>
        </el-col> -->
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-row>
            <el-col :span='8' class='label'>通知生产人员</el-col>
            <el-col :span='16' class='content'>{{ order.users}}</el-col>
          </el-row>
          <el-row>
            <el-col :span='8' class='label'>通知制程人员</el-col>
            <el-col :span='16' class='content'>{{ order.charge_users}}</el-col>
          </el-row>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='24' :md='24' :lg='16' :xl='16'>
          <el-col :span='4' class='label'>异常描述</el-col>
          <el-col :span='20' class='content'>{{ order.desc }}</el-col>
        </el-col>
        <!-- <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>受害开始时间</el-col>
          <el-col :span='16' class='content'>{{ order.start_time | formatDate }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>受害结束时间</el-col>
          <el-col :span='16' class='content'>{{ order.end_time | formatDate }}</el-col>
        </el-col> -->
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-row>
            <el-col :span='8' class='label'>受害开始时间</el-col>
            <el-col :span='16' class='content'>{{ order.start_time | formatDate }}</el-col>
          </el-row>
          <el-row>
            <el-col :span='8' class='label'>受害结束时间</el-col>
            <el-col :span='16' class='content'>{{ order.end_time | formatDate }}</el-col>
          </el-row>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='24' :md='24' :lg='16' :xl='16'>
          <el-col :span='4' class='label'>异常批次/基板</el-col>
          <el-col :span='20' class='content'>{{ order.lots }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='24' :lg='8' :xl='8'>
          <el-col :span='8' class='label'>受害批次数</el-col>
          <el-col :span='16' class='content'>{{ order.lot_num }}</el-col>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='24' :md='24' :lg='16' :xl='16'>
          <el-col :span='4' class='label'>复机条件</el-col>
          <el-col :span='20' class='content'>{{ order.condition }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-col :span='8' class='label'>绝对不良</el-col>
          <el-col :span='16' class='content'>
            <span v-if='order.defect_type === true'>是</span>
            <span v-else-if='order.defect_type === false'>否</span>
            <span v-else>未知</span>
          </el-col>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='12' :md='12' :lg='16' :xl='18'>
          <el-col :span='4' class='label'>
            批注 <AddRemark :order='id' @change='handleChange'></AddRemark>
          </el-col>
          <el-col :span='20' class='content'>
            <span
              v-for='(remark, index) in order.remarks'
              :key='index'
            >
              <span class='remark-user'>
                {{ remark.user.username }}
                {{ remark.user.realname }}
                {{ remark.created | formatDate }}:
              </span>
              {{ remark.content }} <br>
            </span>
          </el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
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
      </el-row>
      <el-row>
        <el-col :span='4' :offset='20'>
          <router-link :to='"/tft/order/update/" + order.id'>
            <el-button
              type='warning'
              icon='el-icon-edit'
              v-if="canBeUpdated"
            >修改停机</el-button>
          </router-link>
        </el-col>
      </el-row>

      <el-row>
        <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
          <h3 class='title'>停机签核</h3>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
          <el-col :span='8' class='label'>生产领班签核</el-col>
          <el-col :span='16' class='content'>
            <template v-if='order.status.code === "1"'>
              <ProductAudit :order='id' @change='handleChange'></ProductAudit>
            </template>
            <template v-else>{{ order.startaudit.p_signer.username }}</template>
          </el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
          <el-col :span='8' class='label'>生产签字时间</el-col>
          <el-col :span='16' class='content'>{{ order.startaudit.p_time | formatDate }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
          <el-col :span='8' class='label'>Recipe关闭人员</el-col>
          <el-col :span='16' class='content'>{{ order.startaudit.recipe_close }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
          <el-col :span='8' class='label'>Recipe确认人员</el-col>
          <el-col :span='16' class='content'>{{ order.startaudit.recipe_confirm }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
          <el-col :span='8' class='label'>责任工程签字</el-col>
          <el-col :span='16' class='content'>
            <template v-if='order.status.code === "2"'>
              <ChargeAudit :order='id' :group-name='order.charge_group.name' @change='handleChange'></ChargeAudit>
            </template>
            <template v-else>{{ order.startaudit.c_signer.username }}</template>
          </el-col>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
          <el-col :span='8' class='label'>工程签字时间</el-col>
          <el-col :span='16' class='content'>{{ order.startaudit.c_time | formatDate }}</el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
          <el-col :span='4' class='label'>是否拒签</el-col>
          <el-col :span='20' class='content'>
            <span v-if='order.startaudit.rejected === true'>是</span>
            <span v-else>否</span>
          </el-col>
        </el-col>
        <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
          <el-col :span='4' class='label'>拒签理由</el-col>
          <el-col :span='20' class='content'>{{ order.startaudit.reason }}</el-col>
        </el-col>
      </el-row>
    </div>

    <RecoverOrders :recoverorders='order.recoverorders'></RecoverOrders>

    <div class='button'>
      <OrderStatus :order='id'></OrderStatus>
    </div>

    <el-row>
      <el-col :span='4' :offset='20'>
        <CreateRecoverOrder :order='id'></CreateRecoverOrder>
      </el-col>
    </el-row>

    <BackTop></BackTop>

  </div>
</template>

<script>
import { getOrder, canUpdate } from '@/api/tft'
import { formatDate } from '@/common/js/date.js'
import BackTop from '@/common/components/BackTop'
import OrderStatus from './detail/OrderStatus'
import AddRemark from './detail/AddRemark'
import ProductAudit from './detail/ProductAudit'
import ChargeAudit from './detail/ChargeAudit'
import RecoverOrders from './detail/RecoverOrders'
import CreateRecoverOrder from './detail/CreateRecoverOrder'

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
        },
        recoverorders: []
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
      this.canUpdate()
    },
    handleChange () {
      this.getOrder()
    },
    canUpdate () {
      canUpdate(this.id)
        .then((res) => {
          this.canBeUpdated = res.data.can
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  components: {
    BackTop,
    OrderStatus,
    AddRemark,
    ProductAudit,
    ChargeAudit,
    RecoverOrders,
    CreateRecoverOrder
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
.order
.recover-orders
  border 1px solid #0E67CC
  border-radius 20px
  box-shadow -8px 8px 5px #888888
  margin-bottom 20px
  .recover-order
    border 2px double #4FA110
    .recover-order-title
      text-align center
      color #2E77C2
      // text-shadow 2px 2px 5px #2E77C2
.title
  text-align center
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
  a
    text-decoration none
    color #22558B
  .remark-user
    color #000
.button
  position fixed
  top 61.8%
  right 0px
.tip
  color #67A3E1
  font-size .5em
</style>
