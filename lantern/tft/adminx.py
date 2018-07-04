import xadmin

from .models import EqKind, Eq, Step, \
                    Lot, \
                    Order, \
                    StartOrder, StartAudit, \
                    RecoverOrder, RecoverAudit, \
                    ReportFile, Remark


class EqKindAdmin(object):
    list_display = ['name', 'group']
    # list_filter = []
    # search_fields = []

class EqAdmin(object):
    list_display = ['name', 'kind']


class StepAdmin(object):
    list_display = ['name', 'eq']


class OrderAdmin(object):
    list_display = ['sn', 'status']


class StartOrderAdmin(object):
    list_display = ['order', 'appl', 'created']


class StartAuditAdmin(object):
    list_display = ['order', 'p_signer', 'c_signer', 'rejected']


class RecoverOrderAdmin(object):
    list_display = ['order', 'appl', 'partial', 'created']


class RecoverAuditAdmin(object):
    list_display = ['recover_order', 'qc_signer', 'p_signer', 'rejected', 'created']


xadmin.site.register(EqKind, EqKindAdmin)
xadmin.site.register(Eq, EqAdmin)
xadmin.site.register(Step, StepAdmin)

xadmin.site.register(Lot)

xadmin.site.register(Order, OrderAdmin)
xadmin.site.register(StartOrder, StartOrderAdmin)
xadmin.site.register(StartAudit, StartAuditAdmin)
xadmin.site.register(RecoverOrder, RecoverOrderAdmin)
xadmin.site.register(RecoverAudit, RecoverAuditAdmin)
xadmin.site.register(ReportFile)
xadmin.site.register(Remark)
