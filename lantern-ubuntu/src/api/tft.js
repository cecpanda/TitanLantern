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
  console.log(order.found_time, typeof order.found_time)
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

// update order
export const updateOrder = (order) => {
  // 这几个时间这里有坑
  // 如果原来已经有的时间为字符串
  // 新选的时间为对象
  let foundTime
  let startTime
  let endTime
  if (typeof order.found_time === 'object') {
    foundTime = order.found_time.toISOString()
  } else {
    foundTime = order.found_time
  }
  if (order.start_time) {
    if (typeof order.start_time === 'object') {
      startTime = order.start_time.toISOString()
    } else {
      startTime = order.start_time
    }
  } else {
    startTime = undefined
  }
  if (order.end_time) {
    if (typeof order.end_time === 'object') {
      endTime = order.end_time.toISOString()
    } else {
      endTime = order.end_time
    }
  } else {
    endTime = undefined
  }
  return axios({
    method: 'put',
    url: `${host}/tft/order/start/${order.id}/`,
    data: {
      found_step: order.found_step,
      found_time: foundTime,
      charge_group: order.charge_group,
      eq: order.eq,
      kind: order.kind,
      step: order.step,
      reason: order.reason,
      users: order.users,
      charge_users: order.charge_users,
      desc: order.desc,
      condition: order.condition,
      start_time: startTime,
      end_time: endTime,
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

export const canUpdate = (id) => {
  return axios.get(`${host}/tft/order/start/${id}/can-update/`)
}

// query orders
// paarams = {
//   page: page,
//   'page-size': pageSize,
//   username: username,
//   realname: realname,
//   group: group,
//   charge_group: charge_group,
//   search: search,
//   ordering: ordering
// }
export const getOrders = (params) => {
  return axios.get(`${host}/tft/order/query/`, {
    params: params
  })
}

// query order
export const getOrder = (order) => {
  return axios.get(`${host}/tft/order/query/${order}/`)
}

// query recover orders
export const getRecoverOrders = (params) => {
  return axios.get(`${host}/tft/order/recover/`, {
    params: params
  })
}

// query recover order
export const getRecoverOrder = (id) => {
  return axios.get(`${host}/tft/order/recover/${id}/`)
}

// update order
// get report handler
export const getReport = (url) => {
  return axios.get(url)
}

// add remark
export const addRemark = (order, content) => {
  return axios.post(`${host}/tft/order/remark/`, {
    order: order,
    content: content
  })
}

// product audit
// export const productAudit = (order, recipeClose, recipeConfirm, remark) => {
//   return axios.post(`${host}/tft/order/audit/product/`, {
//     order: order,
//     recipe_close: recipeClose,
//     recipe_confirm: recipeConfirm,
//     remark: remark
//   })
// }
export const productAudit = (params) => {
  return axios.post(`${host}/tft/order/audit/product/`, params)
}

// charge audit
export const chargeAudit = (params) => {
  return axios.post(`${host}/tft/order/audit/charge/`, params)
}

// whether I could create a recover order for a definite order
export const canCreate = (order) => {
  return axios.get(`${host}/tft/order/recover/can-create/`, {
    params: {
      order: order
    }
  })
}

// create recover order
export const createRecoverOrder = (params) => {
  return axios.post(`${host}/tft/order/recover/`, params)
}

// update recover order
export const updateRecoverOrder = (id, params) => {
  return axios.put(`${host}/tft/order/recover/${id}/`, params)
}

// can update recover order
export const canUpdateRecoverOrder = (id) => {
  return axios.get(`${host}/tft/order/recover/${id}/can-update/`)
}

// can update recover orders
export const canUpdateRecoverOrders = () => {
  return axios.get(`${host}/tft/order/recover/all-can-update/`)
}

// recover order QC audit
export const recoverQcAudit = (params) => {
  return axios.post(`${host}/tft/order/recover-audit/qc/`, params)
}

// recover order product audit
export const recoverProductAudit = (params) => {
  return axios.post(`${host}/tft/order/recover-audit/product/`, params)
}
