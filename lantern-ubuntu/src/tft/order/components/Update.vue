<template>
  <div>
    <el-row>
      <el-col :xs="24" :sm="24" :md="16" :lg="16" :xl="16">
        <h1>设备品质异常停机单 - 修改</h1>
      </el-col>
      <el-col :xs="24" :sm="24" :md="8" :lg="8" :xl="8" class='user'>
        <span class='user-info'>当前用户:</span>
        <span class='user-content'>{{ username }}</span><br>
        <span class='user-info'>当前时间:</span>
        <span class='user-content'>{{ date | formatDate }}</span>
      </el-col>
    </el-row>
    <el-form
      ref="form"
      :model="order"
      :rules="rules"
      label-width="120px"
      status-icon
    >
      <el-row>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-form-item label="编号" prop='id'>
            <el-input v-model="order.id" disabled></el-input>
          </el-form-item>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-form-item label="状态" prop='status'>
            <el-input v-model="order.status.desc" disabled></el-input>
          </el-form-item>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-form-item label="开单工程" prop='group'>
            <el-input v-model="order.group.name" disabled></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-form-item label="开单人员" prop='user'>
            <el-input v-model="order.user.username" disabled></el-input>
          </el-form-item>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-form-item label="开单时间" prop='created'>
            <el-date-picker
              v-model="order.created"
              type="datetime"
              placeholder="选择日期时间"
              disabled
            >
            </el-date-picker>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-form-item label="修改人员" prop='mod_user'>
            <el-input v-model="order.mod_user.username" disabled></el-input>
          </el-form-item>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-form-item label="修改时间" prop='modified'>
            <el-date-picker
              v-model="order.modified"
              type="datetime"
              placeholder="选择日期时间"
              disabled
            >
            </el-date-picker>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-form-item label="发现站点" prop='found_step'>
            <el-input v-model="order.found_step"></el-input>
          </el-form-item>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-form-item label="发现时间" prop='found_time'>
            <el-date-picker
              v-model="order.found_time"
              type="datetime"
              placeholder="选择日期时间"
            >
            </el-date-picker>
          </el-form-item>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-form-item label="责任工程" prop='charge_group'>
            <el-select v-model="order.charge_group" clearable>
              <el-option
                v-for="group in groups"
                :key="group.id"
                :label="group.name"
                :value="group.id"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-form-item label="停机设备" prop='eq'>
            <el-input v-model="order.eq"></el-input>
          </el-form-item>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-form-item label="停机机种" prop='kind'>
            <el-input v-model="order.kind"></el-input>
          </el-form-item>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-form-item label="停机站点" prop='step'>
            <el-input v-model="order.step"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='24' :md='24' :lg='16' :xl='16'>
          <el-form-item label="停机原因" prop='reason'>
            <el-input
              v-model="order.reason"
              type="textarea"
              :rows="4"
              placeholder="请输入内容"
            >
            </el-input>
          </el-form-item>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-row>
            <el-form-item label="通知生产人员" prop='users'>
              <el-input v-model="order.users"></el-input>
            </el-form-item>
          </el-row>
          <el-row>
            <el-form-item label="通知制程人员" prop='charge_users'>
              <el-input v-model="order.charge_users"></el-input>
            </el-form-item>
          </el-row>
        </el-col>
      </el-row>
      <h3>异常状况描述（不良现象说明）</h3>
      <el-row>
        <el-col :xs='24' :sm='24' :md='24' :lg='16' :xl='16'>
          <el-form-item label="异常描述" prop='desc'>
            <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="order.desc">
            </el-input>
          </el-form-item>
        </el-col>
        <el-col :xs='24' :sm='12' :md='12' :lg='8' :xl='6'>
          <el-row>
            <el-form-item label="受害开始时间">
              <el-date-picker
                v-model="order.start_time"
                type="datetime"
                placeholder="选择日期时间">
              </el-date-picker>
            </el-form-item>
          </el-row>
          <el-row>
            <el-form-item label="受害结束时间">
              <el-date-picker
                v-model="order.end_time"
                type="datetime"
                placeholder="选择日期时间">
              </el-date-picker>
            </el-form-item>
          </el-row>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='24' :md='24' :lg='16' :xl='16'>
          <el-form-item label="异常批次/基板" prop='lots'>
            <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="order.lots">
            </el-input>
          </el-form-item>
        </el-col>
        <el-col :xs='24' :sm='24' :md='24' :lg='8' :xl='8'>
          <el-form-item label="受害批次数" prop='lot_num'>
            <el-input v-model="order.lot_num"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='24' :md='24' :lg='16' :xl='16'>
          <el-form-item label="复机条件" prop='condition'>
            <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="order.condition">
            </el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='24' :md='24' :lg='16' :xl='16'>
          <el-form-item label="不良类型">
            <el-radio v-model="order.defect_type" :label="null">默认选项</el-radio>
            <el-radio v-model="order.defect_type" :label="true">绝对不良</el-radio>
            <el-radio v-model="order.defect_type" :label="false">非绝对不良</el-radio>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='24' :md='24' :lg='16' :xl='16'>
          <el-form-item label="调查报告">
            <el-upload
              multiple
              action=''
              :on-change='handleChange'
              :limit="20"
              :on-exceed="handleExceed"
              :before-upload="beforeUpload"
            >
              <el-button size="small" type="primary">点击上传</el-button>
            </el-upload>
          </el-form-item>
          <!-- <input type="file" @change="getFile($event)"> -->
        </el-col>
      </el-row>
      <el-row>
        pizhu
      </el-row>
    </el-form>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getUser, getAllGroups } from '@/api/user'
import { formatDate } from '@/common/js/date.js'
import { getOrder, canUpdate, getReport } from '@/api/tft'

export default {
  name: 'Update',
  props: {
    id: {type: String, required: true}
  },
  data () {
    return {
      user: {},
      date: new Date(),
      groups: [],
      canBeUpdated: false,
      order: {
        status: {},
        user: {},
        group: {},
        mod_user: {},
        charge_group: {}
      },
      rules: {
        found_step: [
          { required: true, message: '请输入发现站点', trigger: 'blur' },
          { min: 1, max: 30, message: '长度在 1 到 30 个字符', trigger: 'blur' }
        ],
        found_time: [
          { required: true, message: '请选择时间', trigger: 'blur' }
        ],
        charge_group: [
          { required: true, message: '请输入责任工程', trigger: 'change' }
        ],
        eq: [
          { required: true, message: '请输入停机设备', trigger: 'blur' },
          { min: 1, max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
        ],
        kind: [
          { required: true, message: '请输入停机机种', trigger: 'blur' },
          { min: 1, max: 30, message: '长度在 1 到 30 个字符', trigger: 'blur' }
        ],
        step: [
          { required: true, message: '请输入停机站点', trigger: 'blur' },
          { min: 1, max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
        ],
        reason: [
          { required: true, message: '请输入停机原因', trigger: 'blur' },
          { min: 1, max: 100, message: '长度在 1 到 100 个字符', trigger: 'blur' }
        ],
        users: [
          { required: true, message: '请输入通知生产人员', trigger: 'blur' },
          { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur' }
        ],
        charge_users: [
          { required: true, message: '请输入制程生产人员', trigger: 'blur' },
          { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur' }
        ],
        desc: [
          { required: true, message: '请输入异常描述', trigger: 'blur' },
          { min: 1, max: 300, message: '长度在 1 到 300 个字符', trigger: 'blur' }
        ],
        lot_num: [
          { min: 0, max: 10, message: '长度不能超过 10 个字符', trigger: 'blur' }
        ],
        lots: [
          { min: 0, max: 100, message: '长度不能超过 100 个字符', trigger: 'blur' }
        ],
        condition: [
          { required: true, message: '请输入复机条件', trigger: 'blur' },
          { min: 1, max: 200, message: '长度在 1 到 200 个字符', trigger: 'blur' }
        ]
        // remark: [
        //   { min: 0, max: 300, message: '长度不能超过 300 个字符', trigger: 'blur' }
        // ]
      }
    }
  },
  computed: {
    ...mapGetters({
      username: 'username'
    })
  },
  methods: {
    getUser (username) {
      getUser(username)
        .then((response) => {
          this.user = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getAllGroups () {
      getAllGroups()
        .then((res) => {
          this.groups = res.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
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
    getReport (url) {
      getReport(url)
        .then((res) => {
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    handleExceed (files, fileList) {
      this.$message.warning(`当前限制选择 20 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`)
    },
    handleChange (file, files) {
      
      console.log(file)
      console.log(typeof file)
      console.log(files)

      this.order.reports = []
      files.forEach((file) => {
        this.order.reports.push(file.raw)
      })
      // 上传文件必须是 FormData，内容是 file.raw
      // var formdata = new FormData()
      // formdata.append('avatar', file.raw)
      // formdata.append('realname', 'woca')
      // testAvatar(formdata)
    },
    beforeUpload (file) {
      const isJpgPng = file.type === 'image/jpeg' || file.type === 'image/png'
      const isLt10M = file.size / 1024 / 1024 < 10
      if (!isJpgPng) {
        this.$message.error('上传头像图片只能是 JPG/PNG 格式!')
      }
      if (!isLt10M) {
        this.$message.error('上传文件大小不能超过 10MB!')
      }
      return isLt10M && isJpgPng
    }
  },
  filters: {
    formatDate (time) {
      let date = new Date(time)
      return formatDate(date, 'yyyy-MM-dd hh:mm:ss')
    }
  },
  mounted () {
    this.getUser(this.username)
    this.getAllGroups()
    this.getOrder()
    var _this = this // 声明一个变量指向vue实例this,保证作用域一致
    this.timer = setInterval(() => {
      _this.date = new Date() // 修改数据date
    }, 1000)
  },
  beforeDestroy () {
    if (this.timer) {
      clearInterval(this.timer) // 在vue实例销毁钱，清除我们的定时器
    }
  }
}
</script>

<style lang='stylus' scoped>
h1
  font-size 30px
h3
  font-size 20px
  margin-top 50px
.el-col
  // border 1px solid #8FA5BC
  border-radius 8px
.user
  background #CDD1D4
  margin-bottom 20px
  .user-info
    font-size 18px
  .user-content
    font-size 15px
    color #38739F
</style>
