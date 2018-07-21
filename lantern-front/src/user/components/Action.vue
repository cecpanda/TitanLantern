<template>
  <div>
    <h1>我的动态</h1>
    <el-row
      v-for='action in actions'
      :key='action.id'
    >
      {{ action.created | formatDate}}
      {{ action.user.username }} {{ action.verb }}
      {{ action.target.id }}
    </el-row>
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
import { getAction } from '@/api/user'
import { formatDate } from '@/common/js/date.js'

export default {
  name: 'Action',
  data () {
    return {
      page: 1,
      pageSize: 10,
      count: null,
      actions: []
    }
  },
  computed: {
    ...mapGetters({
      username: 'username'
    })
  },
  methods: {
    getAction () {
      getAction(this.page, this.pageSize)
        .then((res) => {
          this.count = res.data.count
          this.actions = res.data.results
        })
    },
    handleCurrentChange (val) {
      this.getAction()
    }
  },
  created () {
    this.getAction()
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

</style>
