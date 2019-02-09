from django.contrib.auth.models import User, Group
from rest_framework import serializers
from delivery.models import DeliveryHead, DeliveryType
from operations.models import Order

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class DeliveryTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeliveryType
        fields = ('id', 'name', 'short','status', 'erp_link')

class DeliverySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeliveryHead
        fields = ('id','delivery_type', 'partner', 'date_create')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    #delivery_type = serializers.CharField('delivery_type', max_length=10)
    class Meta:
        model = Order
        fields = ('id', 'status', 'order_creator')
