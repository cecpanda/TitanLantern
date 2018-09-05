<template>
  <div ref='container'>
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
      <!-- <el-row v-if="canBeUpdated">
        <el-col :span='2' :offset='20'>
          <router-link :to='"/tft/order/update/" + order.id'>
            <el-button type="warning" icon='el-icon-edit' round>修改</el-button>
          </router-link>
        </el-col>
      </el-row> -->
      <el-row>
        <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
          <h3 class='title'>停机签核</h3>
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
          <el-col :span='8' class='label'>生产领班签核</el-col>
          <el-col :span='16' class='content'>
            <span v-if='order.status.code === "1"' @click='productAuditVisible = true'>
              <i class="el-icon-star-off"></i>
              <i class="el-icon-star-off"></i>
              <i class="el-icon-star-off"></i>
            </span>
            <span v-else>{{ order.startaudit.p_signer.username }}</span>
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
            <span v-if="order.status.code === '2'" @click='chargeAuditVisible = true'>
              <i class="el-icon-star-off"></i>
              <i class="el-icon-star-off"></i>
              <i class="el-icon-star-off"></i>
            </span>
            <span v-else>{{ order.startaudit.c_signer.username }}</span>
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

    <div class="recover-orders">
      <el-row>
        <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
          <h1 class=title>设备品质异常复机单</h1>
        </el-col>
      </el-row>

      <div v-for='(recoverOrder, index) in order.recoverorders' :key='index' class='recover-order'>
        <el-row>
          <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
            <h5 class='recover-order-title'>复机申请-{{ index }}</h5>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
            <el-col :span='8' class='label'>申请人</el-col>
            <el-col :span='16' class='content'>{{ recoverOrder.user.username }}</el-col>
          </el-col>
          <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
            <el-col :span='8' class='label'>申请时间</el-col>
            <el-col :span='16' class='content'>{{ recoverOrder.created | formatDate }}</el-col>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
            <el-col :span='8' class='label'>修改人</el-col>
            <el-col :span='16' class='content'>{{ recoverOrder.mod_user.username }}</el-col>
          </el-col>
          <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
            <el-col :span='8' class='label'>修改时间</el-col>
            <el-col :span='16' class='content'>{{ recoverOrder.modified | formatDate }}</el-col>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
            <el-col :span='4' class='label'>责任单位对策说明</el-col>
            <el-col :span='16' class='content'>{{ recoverOrder.solution }}</el-col>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
            <el-col :span='4' class='label'>先行 lot 结果说明</el-col>
            <el-col :span='16' class='content'>{{ recoverOrder.explain }}</el-col>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
            <el-col :span='4' class='label'>部分复机</el-col>
            <el-col :span='16' class='content'>
              <el-radio v-model="recoverOrder.partial" :label="true">是</el-radio>
              <el-radio v-model="recoverOrder.partial" :label="false">否</el-radio>
            </el-col>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
            <el-col :span='4' class='label'>部分复机设备</el-col>
            <el-col :span='16' class='content'>{{ recoverOrder.eq }}</el-col>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
            <el-col :span='4' class='label'>部分复机机种</el-col>
            <el-col :span='16' class='content'>{{ recoverOrder.kind }}</el-col>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
            <el-col :span='4' class='label'>部分复机站点</el-col>
            <el-col :span='16' class='content'>{{ recoverOrder.step }}</el-col>
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
            <el-col :span='16' class='content'>{{ recoverOrder.audit.qc_signer.username }}</el-col>
          </el-col>
          <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
            <el-col :span='8' class='label'>品质签复时间</el-col>
            <el-col :span='16' class='content'>{{ recoverOrder.audit.qc_time | formatDate }}</el-col>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
            <el-col :span='8' class='label'>生产领班签复</el-col>
            <el-col :span='16' class='content'>{{ recoverOrder.audit.p_signer.username }}</el-col>
          </el-col>
          <el-col :xs='24' :sm='12' :md='12' :lg='12' :xl='6'>
            <el-col :span='8' class='label'>生产签复时间</el-col>
            <el-col :span='16' class='content'>{{ recoverOrder.audit.p_time | formatDate }}</el-col>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
            <el-col :span='4' class='label'>是否拒签</el-col>
            <el-col :span='16' class='content'>
              <el-radio v-model="recoverOrder.audit.rejected" :label="true">是</el-radio>
              <el-radio v-model="recoverOrder.audit.rejected" :label="false">否</el-radio>
            </el-col>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs='24' :sm='24' :md='24' :lg='24' :xl='24'>
            <el-col :span='4' class='label'>拒签理由</el-col>
            <el-col :span='16' class='content'>{{ recoverOrder.audit.reason }}</el-col>
          </el-col>
        </el-row>
      </div>
    </div>

    <div class='button'>
      <el-button type='info'>{{ order.status.desc }}</el-button><br>
      <router-link :to='"/tft/order/update/" + order.id'>
        <el-button
          type='warning'
          icon='el-icon-edit'
          v-if="canBeUpdated"
        >修改停机</el-button>
      </router-link>
      <br>
      <el-button
        type='primary'
        icon='el-icon-plus'
        @click='recoverOrderVisible = true'
      >申请复机</el-button>
      <BackTop></BackTop>
    </div>
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

      <el-dialog title="生产签核" :visible.sync="productAuditVisible">
        <el-form :model='productAudit' :rules='productRules' ref='productForm'>
          <el-form-item label="Recipe关闭人员" prop='recipe_close' label-width='20%'>
            <el-input v-model="productAudit.recipe_close"></el-input>
          </el-form-item>
          <el-form-item label="Recipe确认人员" prop='recipe_confirm' label-width='20%'>
            <el-input v-model="productAudit.recipe_confirm"></el-input>
          </el-form-item>
          <el-form-item label="添加批注" prop='remark' label-width='20%'>
            <el-input
              type='textarea'
              :rows='4'
              v-model="productAudit.remark"
              placeholder='不能超过 500 字符'
            ></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="productAuditVisible = false">取 消</el-button>
          <el-button type="primary" @click="addProductAudit">确 定</el-button>
        </div>
      </el-dialog>

      <el-dialog :title="'责任工程审核 - ' + order.charge_group.name" :visible.sync="chargeAuditVisible">
        <el-form :model='chargeAudit' :rules='chargeRules' ref='chargeForm'>
          <el-form-item label="是否拒签" prop='rejected' label-width='20%'>
            <el-radio v-model="chargeAudit.rejected" :label="true">是</el-radio>
            <el-radio v-model="chargeAudit.rejected" :label="false">否</el-radio>
          </el-form-item>
          <el-form-item label="拒签理由" prop='reason' label-width='20%'>
            <el-input
              type='textarea'
              :rows='4'
              v-model="chargeAudit.reason"
              placeholder='不能超过 100 字符'
            ></el-input>
            拒签时必填
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="chargeAuditVisible = false">取 消</el-button>
          <el-button type="primary" @click="addChargeAudit">确 定</el-button>
        </div>
      </el-dialog>

      <el-dialog title="申请复机" :visible.sync="recoverOrderVisible" width='65%'>
        <el-form :model='recoverOrder' :rules='recoverOrderRules' ref='recoverOrderForm' v-if='canCreateRecoverOrder'>
          <el-form-item label="责任单位对策说明" prop='solution' label-width='15%'>
            <el-input
              type='textarea'
              :rows='3'
              v-model="recoverOrder.solution"
              placeholder='不能超过 200 字符'
            ></el-input>
          </el-form-item>
          <el-form-item label="先行lot结果说明" prop='explain' label-width='15%'>
            <el-input
              type='textarea'
              :rows='3'
              v-model="recoverOrder.explain"
              placeholder='不能超过 200 字符'
            ></el-input>
          </el-form-item>
          <el-form-item label="是否部分复机" prop='partial' label-width='15%'>
            <el-radio v-model="recoverOrder.partial" :label="true">是</el-radio>
            <el-radio v-model="recoverOrder.partial" :label="false">否</el-radio>
          </el-form-item>
          <el-form-item label="部分复机设备" prop='eq' label-width='15%'>
            <el-input v-model="recoverOrder.eq" placeholder='不能超过 50 字符'></el-input>
            <span class='tip'>部分复机时必填, 否则被忽略</span>
          </el-form-item>
          <el-form-item label="部分复机机种" prop='kind' label-width='15%'>
            <el-input v-model="recoverOrder.kind" placeholder='不能超过 30 字符'></el-input>
            <span class='tip'>部分复机时必填, 否则被忽略</span>
          </el-form-item>
          <el-form-item label="部分复机站点" prop='step' label-width='15%'>
            <el-input v-model="recoverOrder.step" placeholder='不能超过 50 字符'></el-input>
            <span class='tip'>部分复机时必填, 否则被忽略</span>
          </el-form-item>
        </el-form>
        <div v-else>
          {{ canCreateRecoverOrderError }}
        </div>
        <div slot="footer" class="dialog-footer" v-if='canCreateRecoverOrder'>
          <el-button @click="recoverOrderVisible = false">取 消</el-button>
          <el-button type="primary" @click="createRecoverOrder">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import {
  getOrder, canUpdate, addRemark, productAudit, chargeAudit,
  canCreate, createRecoverOrder
} from '@/api/tft'
import { formatDate } from '@/common/js/date.js'
import BackTop from '@/common/components/BackTop'

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
      },
      productAuditVisible: false,
      productAudit: {
        recipe_close: '',
        recipe_confirm: '',
        remark: ''
      },
      productRules: {
        recipe_close: [
          { required: true, message: '请输入 Recipe 关闭人员', trigger: 'blur' },
          { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur' }
        ],
        recipe_confirm: [
          { required: true, message: '请输入 Recipe 确认人员', trigger: 'blur' },
          { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur' }
        ],
        remark: [
          { min: 1, max: 500, message: '长度在 1 到 500 个字符', trigger: 'blur' }
        ]
      },
      chargeAuditVisible: false,
      chargeAudit: {
        rejected: false,
        reason: ''
      },
      chargeRules: {
        rejected: [
          { required: true, message: '是否拒签', trigger: 'blur' }
        ],
        reason: [
          { min: 1, max: 100, message: '长度在 1 到 100 个字符', trigger: 'blur' }
        ]
      },
      canCreateRecoverOrder: false,
      canCreateRecoverOrderError: '',
      recoverOrderVisible: false,
      recoverOrder: {
        solution: '',
        explain: '',
        partial: false,
        eq: '',
        kind: '',
        step: ''
      },
      recoverOrderRules: {
        solution: [
          { required: true, message: '请输入责任单位对策说明', trigger: 'blur' },
          { min: 1, max: 200, message: '长度不超过 200 个字符', trigger: 'blur' }
        ],
        explain: [
          { required: true, message: '请输入先行lot结果说明', trigger: 'blur' },
          { min: 1, max: 200, message: '长度不超过 200 个字符', trigger: 'blur' }
        ],
        partial: [
          { required: true, message: '是否部分复机', trigger: 'blur' }
        ],
        eq: [
          { min: 0, max: 50, message: '长度不超过 50 个字符', trigger: 'blur' }
        ],
        kind: [
          { min: 0, max: 30, message: '长度不超过 30 个字符', trigger: 'blur' }
        ],
        step: [
          { min: 0, max: 50, message: '长度不超过 50 个字符', trigger: 'blur' }
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
    },
    addProductAudit () {
      this.$refs['productForm'].validate((valid) => {
        if (valid) {
          let params = {
            order: this.id,
            recipe_close: this.productAudit.recipe_close,
            recipe_confirm: this.productAudit.recipe_confirm
          }
          if (this.productAudit.remark) {
            params.remark = this.productAudit.remark
          }
          productAudit(params)
            .then((res) => {
              this.$notify({
                title: '成功',
                message: '生产签核成功',
                type: 'success'
              })
              this.productAudit = {recipe_close: '', recipe_confirm: '', remark: ''}
              this.productAuditVisible = false
              this.getOrder()
            })
            .catch((err) => {
              console.log(err)
              this.$notify({
                title: '错误',
                message: err,
                type: 'error'
              })
              this.productAudit = {recipe_close: '', recipe_confirm: '', remark: ''}
              this.productAuditVisible = false
            })
        }
      })
    },
    addChargeAudit () {
      this.$refs['chargeForm'].validate((valid) => {
        if (valid) {
          let params = {
            order: this.id,
            rejected: this.chargeAudit.rejected
          }
          if (this.chargeAudit.reason) {
            params.reason = this.chargeAudit.reason
          }
          chargeAudit(params)
            .then((res) => {
              this.$notify({
                title: '成功',
                message: '责任工程审核成功',
                type: 'success'
              })
              this.chargeAudit = {rejected: false, reason: ''}
              this.chargeAuditVisible = false
              this.getOrder()
            })
            .catch((err) => {
              console.log(err)
              this.$notify({
                title: '错误',
                message: err,
                type: 'error'
              })
              this.chargeAudit = {rejected: false, reason: ''}
              this.chargeAuditVisible = false
            })
        }
      })
    },
    canCreate () {
      canCreate(this.id)
        .then((res) => {
          this.canCreateRecoverOrder = res.data.can
        })
        .catch((err) => {
          console.log(err)
          this.canCreateRecoverOrderError = err
        })
    },
    createRecoverOrder () {
      this.$refs['recoverOrderForm'].validate((valid) => {
        if (valid) {
          let params = {
            order: this.id,
            solution: this.recoverOrder.solution,
            explain: this.recoverOrder.explain,
            partial: this.recoverOrder.partial
          }
          if (params.partial) {
            params.eq = this.recoverOrder.eq
            params.kind = this.recoverOrder.kind
            params.step = this.recoverOrder.step
          }
          createRecoverOrder(params)
            .then((res) => {
              this.$notify({
                title: '成功',
                message: '复机申请成功',
                type: 'success'
              })
              this.recoverOrder = {solution: '', explain: '', partial: false, eq: '', kind: '', step: ''}
              this.recoverOrderVisible = false
              this.getOrder()
            })
            .catch((err) => {
              this.$notify({
                title: '失败',
                message: err,
                type: 'error'
              })
              this.recoverOrder = {solution: '', explain: '', partial: false, eq: '', kind: '', step: ''}
              this.recoverOrderVisible = false
            })
        }
      })
    }
  },
  components: {
    BackTop
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
    this.canCreate()
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
    border 1px dashed #4FA110
    .recover-order-title
      text-align center
      color #2E77C2
      text-shadow 2px 2px 5px #2E77C2
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
