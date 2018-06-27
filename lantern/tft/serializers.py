from rest_framework import serializers

from .models import Lot, HoldLot
from account.serializers import UserSerializer


class LotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lot
        fields = '__all__'


class HoldLotSerializer(serializers.ModelSerializer):
    lot = LotSerializer()
    applicant = UserSerializer()
    verifier = UserSerializer()

    class Meta:
        model = HoldLot
        fields = '__all__'
