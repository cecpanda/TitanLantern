import xadmin

from .models import ID, Order, Audit, \
                    RecoverOrder, RecoverAudit, \
                    Report, Remark


class EqKindAdmin(object):
    list_display = ['name', 'group']
    # list_filter = []
    # search_fields = []

class EqAdmin(object):
    list_display = ['name', 'kind']


class OrderAdmin(object):
    list_display = ['id', 'status', 'next', 'user', 'defect_type', 'created']



class AuditAdmin(object):
    list_display = ['order', 'p_signer', 'c_signer', 'rejected']


class RecoverOrderAdmin(object):
    list_display = ['order', 'user', 'partial', 'created']


class RecoverAuditAdmin(object):
    list_display = ['recover_order', 'qc_signer', 'p_signer', 'rejected']


# xadmin.site.register(EqKind, EqKindAdmin)
# xadmin.site.register(Eq, EqAdmin)
#
# xadmin.site.register(Lot)


class FlowAdmin(object):
    list_display = ['order', 'pre_node', 'next_node']


xadmin.site.register(ID)
xadmin.site.register(Order, OrderAdmin)
xadmin.site.register(Audit, AuditAdmin)
xadmin.site.register(RecoverOrder, RecoverOrderAdmin)
xadmin.site.register(RecoverAudit, RecoverAuditAdmin)
xadmin.site.register(Report)
xadmin.site.register(Remark)
