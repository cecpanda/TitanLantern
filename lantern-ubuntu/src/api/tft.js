import axios from './http'
import conf from './config'

let host = conf.host

export const startOrderFail = (order) => {
  return axios.post(`${host}/tft/order/start/`, {
    found_step: order.found_step,
    found_time: order.found_time.toISOString(),
    charge_group: order.charge_group,
    eq: order.eq,
    kind: order.kind,
    step: order.step,
    reason: order.reason,
    users: order.users,
    charge_users: order.charge_users,
    desc: order.desc,
    condition: order.condition,
    start_time: order.start_time ? order.start_time.toISOString() : null,
    end_time: order.end_time ? order.end_time.toISOString() : null,
    lot_num: order.lot_num,
    lots: order.lots,
    defect_type: order.defect_type,
    reports: order.reports,
    remark: order.remark ? order.remark : undefined
  })
}

export const testAvatar = (params) => {
  return axios.put(`${host}/account/user/change-profile/`, params)
}

export const startOrder = (order) => {
  return axios({
    method: 'post',
    url: `${host}/tft/order/start/`,
    data: {
      found_step: order.found_step,
      found_time: order.found_time.toISOString(),
      charge_group: order.charge_group,
      eq: order.eq,
      kind: order.kind,
      step: order.step,
      reason: order.reason,
      users: order.users,
      charge_users: order.charge_users,
      desc: order.desc,
      condition: order.condition,
      start_time: order.start_time ? order.start_time.toISOString() : undefined,
      end_time: order.end_time ? order.end_time.toISOString() : undefined,
      lot_num: order.lot_num,
      lots: order.lots,
      defect_type: order.defect_type,
      reports: order.reports,
      remark: order.remark ? order.remark : undefined
    },
    transformRequest: [
      (data) => {
        // let ret = ''
        // for (let it in data) {
        //   if (data[it]) {
        //     ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
        //   }
        // }
        // return ret
        let fd = new FormData()
        for (let key in data) {
          if (data.hasOwnProperty(key)) {
            if (typeof (data[key]) === 'undefined') {
            } else {
              fd.append(key, data[key])
            }
          }
        }
        fd.delete('reports')
        if (data.reports.length) {
          data.reports.forEach((value) => {
            fd.append('reports', value)
          })
        }
        return fd
      }]
    // headers: {
    //   'Content-Type': 'multipart/form-data'
    // }
  })
}

// query orders

export const getOrders = (page, pageSize, ordering) => {
  return axios.get(`${host}/tft/order/query/`, {
    params: {
      page: page,
      'page-size': pageSize,
      ordering: ordering
    }
  })
}

export const getUserOrders = (page, pageSize, username) => {
  return axios.get(`${host}/tft/order/query/`, {
    params: {
      page: page,
      'page-size': pageSize,
      username: username
    }
  })
}

// query order
export const getOrder = (order) => {
  return axios.get(`${host}/tft/order/query/${order}/`)
}
