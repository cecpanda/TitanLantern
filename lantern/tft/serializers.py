from rest_framework import serializers

from .models import Order
from account.serializers import UserSerializer


class OpenOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('sn', 'status', 'open_order_user', 'open_order_department', 'open_order_department_r',
                  'found_step', 'found_time', 'eq', 'kind', 'step', 'reason', 'notice_product_user',
                  'notice_process_user', 'desc', 'start_time', 'end_time', 'report', 'lot_num',
                  'lots', 'recover_condition')
        read_only_fields = ('sn',)
