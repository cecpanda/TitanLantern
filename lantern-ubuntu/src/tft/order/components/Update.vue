<template>
  <div>
    <el-row>
      <el-col :xs="24" :sm="24" :md="16" :lg="16" :xl="16">
        <h1>设备品质异常停机单 - 修改</h1>
      </el-col>
      <el-col :xs="24" :sm="24" :md="8" :lg="8" :xl="8" class='user'>
        <span class='user-info'>开单工程:</span>
        <span v-for='group of user.groups' :key='group.id' class='user-content'>
          {{ group.name }}
        </span>
        <br>
        <span class='user-info'>修改人员:</span>
        <span class='user-content'>{{ username }}</span>
        <br>
        <span class='user-info'>当前时间:</span>
        <span class='user-content'>{{ date | formatDate }}</span>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getUser, getAllGroups } from '@/api/user'
import { formatDate } from '@/common/js/date.js'
import { getOrder, canUpdate } from '@/api/tft'

export default {
  name: 'Update',
  props: {
    id: {type: String, required: true}
  },
  data () {
    return {
      user: {},
      date: new Date(),
      canBeUpdated: false,
      order: {
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
