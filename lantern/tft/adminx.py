import xadmin

from .models import EqKind, Eq, Step, \
                    LotInfo, Lot, \
                    Order# , OpenOrder, RecoverOrder


# class LotAdmin(object):
#     list_display = ['id', 'kind', 'num', 'created']
#     search_fields = ['kind', 'num']
#     list_filter = ['kind', 'num', 'created']
#
# xadmin.site.register(Lot, LotAdmin)

class EqAdmin(object):
    list_display = ['name', 'kind']

class StepAdmin(object):
    list_display = ['name', 'eq']


class OrderAdmin(object):
    pass


xadmin.site.register(EqKind)
xadmin.site.register(Eq, EqAdmin)
xadmin.site.register(Step, StepAdmin)

xadmin.site.register(LotInfo)
xadmin.site.register(Lot)

xadmin.site.register(Order)
# xadmin.site.register(OpenOrder)
# xadmin.site.register(RecoverOrder)
