<template>
  <div>
    <el-row>
      <el-col :span='16'>
        <h1>设备品质异常停机单</h1>
      </el-col>
      <el-col :span='8' class='user'>
        <span class='user-info'>开单工程:</span>
        <span v-for='group of user.groups' :key='group.id' class='user-content'>
          {{ group.name }}
        </span>
        <br>
        <span class='user-info'>开单人员:</span>
        <span class='user-content'>{{ username }}</span>
        <br>
        <span class='user-info'>当前时间:</span>
        <span class='user-content'>{{ date | formatDate }}</span>
      </el-col>
    </el-row>
    <el-form
      ref="form"
      :model="order"
      label-width="120px"
      :rules="rules"
      status-icon
    >
      <el-row>
        <el-col :span='8'>
          <el-form-item label="发现站点" prop='found_step'>
            <el-input v-model="order.found_step"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span='8'>
          <el-form-item label="发现时间" prop='found_time'>
            <el-date-picker
              v-model="order.found_time"
              type="datetime"
              placeholder="选择日期时间"
            >
            </el-date-picker>
          </el-form-item>
        </el-col>
        <el-col :span='8'>
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
        <el-col :span='8'>
          <el-form-item label="停机设备" prop='eq'>
            <el-input
              v-model="order.eq"
              type="textarea"
              :rows="2"
              placeholder="请输入内容"
            >
            </el-input>
          </el-form-item>
        </el-col>
        <el-col :span='8'>
          <el-form-item label="停机机种" prop='kind'>
            <el-input
              v-model="order.kind"
              type="textarea"
              :rows="2"
              placeholder="请输入内容"
            >
            </el-input>
          </el-form-item>
        </el-col>
        <el-col :span='8'>
          <el-form-item label="停机站点" prop='step'>
            <el-input
              v-model="order.step"
              type="textarea"
              :rows="2"
              placeholder="请输入内容"
            >
            </el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span='16'>
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
        <el-col :span='8'>
          <el-form-item label="通知生产人员" prop='users'>
            <el-input v-model="order.users"></el-input>
          </el-form-item>
          <el-form-item label="通知制程人员" prop='charge_users'>
            <el-input v-model="order.charge_users"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <h3>异常状况描述（不良现象说明）</h3>
      <el-row>
        <el-col :span='16'>
          <el-form-item label="异常描述" prop='desc'>
            <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="order.desc">
            </el-input>
          </el-form-item>
        </el-col>
        <el-col :span='8'>
          <el-form-item label="受害开始时间">
            <el-date-picker
              v-model="order.start_time"
              type="datetime"
              placeholder="选择日期时间">
            </el-date-picker>
          </el-form-item>
          <el-form-item label="受害结束时间">
            <el-date-picker
              v-model="order.end_time"
              type="datetime"
              placeholder="选择日期时间">
            </el-date-picker>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span='16'>
          <el-form-item label="复机条件" prop='condition'>
            <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="order.condition">
            </el-input>
          </el-form-item>
          <!-- <el-form-item label="批注" prop='remark'>
            <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="order.remark">
            </el-input>
          </el-form-item> -->
        </el-col>
        <el-col :span='8'>
          <el-form-item label="受害批次数" prop='lot_num'>
            <el-input v-model="order.lot_num"></el-input>
          </el-form-item>
          <el-form-item label="异常批次/基板" prop='lots'>
            <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="order.lots">
            </el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span='24'>
          <el-form-item label="不良类型">
            <el-radio v-model="order.defect_type" label="">默认选项</el-radio>
            <el-radio v-model="order.defect_type" :label="true">绝对不良</el-radio>
            <el-radio v-model="order.defect_type" :label="false">非绝对不良</el-radio>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span='8'>
          <el-form-item label="调查报告">
            <el-upload
              multiple
              action=''
              :on-change='handleChange'
              :limit="20"
              :on-exceed="handleExceed"
              :before-upload="beforeUpload"
              :http-request='upload'
            >
              <el-button size="small" type="primary">点击上传</el-button>
            </el-upload>
          </el-form-item>
          <!-- <input type="file" @change="getFile($event)"> -->
        </el-col>
      </el-row>
      <el-row>
        <el-form-item>
          <el-button @click="resetForm('form')">重置</el-button>
          <el-button type="primary" round @click="submitForm('form')">
            立即创建
          </el-button>
        </el-form-item>
      </el-row>
    </el-form>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getUser, getAllGroups } from '@/api/user'
import { startOrder } from '@/api/tft'
import { formatDate } from '@/common/js/date.js'

export default {
  name: 'StartOrder',
  data () {
    return {
      user: {},
      groups: [], // 责任工程用
      order: {
        found_step: '',
        found_time: '',
        charge_group: null,
        eq: '',
        kind: '',
        step: '',
        reason: '',
        users: '',
        charge_users: '',
        desc: '',
        start_time: '',
        end_time: '',
        lot_num: '',
        lots: '',
        condition: '',
        // remark: '',
        defect_type: '',
        reports: []
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
      },
      date: new Date()
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
    },
    getFile (e) {
      let file = e.target.files[0]
      console.log(file)
      console.log(typeof file)
    },
    upload (item) {
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          startOrder(this.order)
            .then((res) => {
              this.$notify({
                title: '成功',
                message: res.data,
                type: 'success'
              })
              this.$router.push({path: '/tft/order/mystart'})
            })
            .catch((error) => {
              this.$notify({
                title: '错误',
                message: error,
                type: 'error'
              })
            })
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
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

<style lang="stylus" scoped>
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
