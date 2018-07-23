import xadmin

from .models import ID, Order, \
                    Report, Remark


class EqKindAdmin(object):
    list_display = ['name', 'group']
    # list_filter = []
    # search_fields = []

class EqAdmin(object):
    list_display = ['name', 'kind']


class OrderAdmin(object):
    list_display = ['id', 'status', 'appl', 'created']


# class AuditAdmin(object):
#     list_display = ['order', 'p_signer', 'c_signer', 'rejected']
#
#
# class RecoverOrderAdmin(object):
#     list_display = ['order', 'appl', 'partial', 'created']
#
#
# class RecoverAuditAdmin(object):
#     list_display = ['recover_order', 'qc_signer', 'p_signer', 'rejected', 'created']


# xadmin.site.register(EqKind, EqKindAdmin)
# xadmin.site.register(Eq, EqAdmin)
#
# xadmin.site.register(Lot)

xadmin.site.register(ID)
xadmin.site.register(Order, OrderAdmin)
# xadmin.site.register(Audit, AuditAdmin)
# xadmin.site.register(RecoverOrder, RecoverOrderAdmin)
# xadmin.site.register(RecoverAudit, RecoverAuditAdmin)
xadmin.site.register(Report)
xadmin.site.register(Remark)
