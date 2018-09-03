<template>
  <div>
    <el-row>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
        <h1>设备品质异常停机单</h1>
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
          批注 <i class="el-icon-plus" @click='addRemarkVisible = true'></i>
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
    <el-row v-if="canBeUpdated" class='button'>
      <el-col :span='2' :offset='20'>
        <router-link :to='"/tft/order/update/" + order.id'>
          <el-button type="warning" icon='el-icon-edit' round>修改</el-button>
        </router-link>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
        <h3>停机签核</h3>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
        <el-col :span='8' class='label'>生产领班签核</el-col>
        <el-col :span='16' class='content'>
          {{ order.startaudit.p_signer.username }}
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
          {{ order.startaudit.c_signer.username }}
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
    <div class='dialog'>
      <el-dialog title="添加批注" :visible.sync="addRemarkVisible">
        <el-form :model='remark' :rules='remarkRules' ref='remarkForm'>
          <el-form-item label="" prop='content'>
            <el-input
              type='textarea'
              :rows='5'
              v-model="remark.content"
              placeholder='批注内容'
            ></el-input>
            不能超过 500 字符
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="addRemarkVisible = false">取 消</el-button>
          <el-button type="primary" @click="addRemark">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import { getOrder, canUpdate, addRemark } from '@/api/tft'
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
      canBeUpdated: false,
      addRemarkVisible: false,
      remark: {
        content: ''
      },
      remarkRules: {
        content: [
          { required: true, message: '请输入批注内容', trigger: 'blur' },
          { min: 1, max: 500, message: '长度在 1 到 500 个字符', trigger: 'blur' }
        ]
      }
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
    },
    addRemark () {
      this.$refs['remarkForm'].validate((valid) => {
        if (valid) {
          addRemark(this.order.id, this.remark.content)
            .then((res) => {
              this.$notify({
                title: '成功',
                message: '添加成功',
                type: 'success'
              })
              this.remark.content = ''
              this.addRemarkVisible = false
              this.getOrder()
            })
            .catch((err) => {
              this.$notify({
                title: '错误',
                message: err,
                type: 'error'
              })
              this.remark.content = ''
              this.addRemarkVisible = false
            })
        }
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
  a
    text-decoration none
    color #22558B
  .remark-user
    color #000
</style>
