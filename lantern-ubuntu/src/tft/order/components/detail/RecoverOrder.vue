<template>
  <div>
    <el-row>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
        <h5 class='recover-order-title'>复机申请-{{ index }}</h5>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>申请人</el-col>
        <el-col :span='16' class='content'>{{ recoverorder.user.username }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>申请时间</el-col>
        <el-col :span='16' class='content'>{{ recoverorder.created | formatDate }}</el-col>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>修改人</el-col>
        <el-col :span='16' class='content'>{{ recoverorder.mod_user.username }}</el-col>
      </el-col>
      <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>修改时间</el-col>
        <el-col :span='16' class='content'>{{ recoverorder.modified | formatDate }}</el-col>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
        <el-col :span='4' class='label'>责任单位对策说明</el-col>
        <el-col :span='16' class='content'>{{ recoverorder.solution }}</el-col>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
        <el-col :span='4' class='label'>先行 lot 结果说明</el-col>
        <el-col :span='16' class='content'>{{ recoverorder.explain }}</el-col>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
        <el-col :span='4' class='label'>部分复机</el-col>
        <el-col :span='16' class='content'>
          <el-radio v-model="recoverorder.partial" :label="true">是</el-radio>
          <el-radio v-model="recoverorder.partial" :label="false">否</el-radio>
        </el-col>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
        <el-col :span='4' class='label'>部分复机设备</el-col>
        <el-col :span='16' class='content'>{{ recoverorder.eq }}</el-col>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
        <el-col :span='4' class='label'>部分复机机种</el-col>
        <el-col :span='16' class='content'>{{ recoverorder.kind }}</el-col>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
        <el-col :span='4' class='label'>部分复机站点</el-col>
        <el-col :span='16' class='content'>{{ recoverorder.step }}</el-col>
        <el-col :span='4' v-if='canBeUpdated'>
          <UpdateRecoverOrder :recoverorder='recoverorder' @change='handleChange'></UpdateRecoverOrder>
        </el-col>
      </el-col>
    </el-row>

    <el-row>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
        <h5 class='recover-order-title'>复机申请-{{ index }}-签核</h5>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>工程品质签复</el-col>
        <el-col :span='16' class='content'>
          <template v-if='status === "5" && !recoverorder.audit.qc_signer.username'>
            <RecoverQcAudit
              :recoverorder='recoverorder'
              @change='handleChange'
            ></RecoverQcAudit>
          </template>
          <span>{{ recoverorder.audit.qc_signer.username }}</span>
        </el-col>
      </el-col>
      <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>品质签复时间</el-col>
        <el-col :span='16' class='content'>{{ recoverorder.audit.qc_time | formatDate }}</el-col>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>生产领班签复</el-col>
        <el-col :span='16' class='content'>
          <template v-if='status === "6" && !recoverorder.audit.p_signer.username'>
            <RecoverProductAudit
              :recoverorder='recoverorder'
              @change='handleChange'
            ></RecoverProductAudit>
          </template>
          {{ recoverorder.audit.p_signer.username }}
        </el-col>
      </el-col>
      <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>生产签复时间</el-col>
        <el-col :span='16' class='content'>{{ recoverorder.audit.p_time | formatDate }}</el-col>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
        <el-col :span='4' class='label'>是否拒签</el-col>
        <el-col :span='16' class='content'>
          <el-radio v-model="recoverorder.audit.rejected" :label="true">是</el-radio>
          <el-radio v-model="recoverorder.audit.rejected" :label="false">否</el-radio>
        </el-col>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
        <el-col :span='4' class='label'>拒签理由</el-col>
        <el-col :span='16' class='content'>{{ recoverorder.audit.reason }}</el-col>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { formatDate } from '@/common/js/date.js'
import { canUpdateRecoverOrder } from '@/api/tft'
import UpdateRecoverOrder from './UpdateRecoverOrder'
import RecoverQcAudit from './RecoverQcAudit'
import RecoverProductAudit from './RecoverProductAudit'

export default {
  name: 'RecoverOrder',
  props: {
    status: {
      required: true
    },
    recoverorder: {
      type: Object,
      required: true
    },
    index: {}
  },
  data () {
    return {
      canBeUpdated: false
    }
  },
  methods: {
    canUpdate () {
      canUpdateRecoverOrder(this.recoverorder.id)
        .then((res) => {
          if (res.data.can) {
            this.canBeUpdated = true
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    handleChange () {
      this.canUpdate()
      this.$emit('change')
    }
  },
  components: {
    UpdateRecoverOrder,
    RecoverQcAudit,
    RecoverProductAudit
  },
  mounted () {
    this.canUpdate()
  },
  filters: {
    formatDate (time) {
      let date = new Date(time)
      return formatDate(date, 'yyyy-MM-dd hh:mm:ss')
    }
  }
}
</script>

<style lang='stylus' scoped>
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
</style>
