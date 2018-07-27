import axios from './http'
import conf from './config'

let host = conf.host

export const startOrder = (order) => {
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
