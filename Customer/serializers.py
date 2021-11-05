from rest_framework import serializers
from .models import *
from bakery.serializers import *
class OrderHistorySer(serializers.ModelSerializer):
    class Meta:
        model=order_history
        fields=["id"]

class OrderSer(serializers.ModelSerializer):
    amount=serializers.SerializerMethodField()
    productKey=Market(read_only=True)
    class Meta:
        model=orders
        fields=["productKey","date","freq","order_id","amount"]

    def get_amount(self,obj):
        return int(obj.productKey.SP * obj.freq)
