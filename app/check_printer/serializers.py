from rest_framework.serializers import Serializer, CharField, IntegerField, ModelSerializer

from check_printer.models import Check


class ItemSerializer(Serializer):
    name = CharField()
    quantity = IntegerField()
    unit_price = IntegerField()


class ClientSerializer(Serializer):
    name = CharField()
    phone = CharField()


class OrderSerializer(Serializer):
    id = IntegerField()
    price = IntegerField()
    items = ItemSerializer(many=True)
    address = CharField()
    client = ClientSerializer()
    point_id = IntegerField()


class CheckSerializer(ModelSerializer):
    class Meta:
        model = Check
        fields = ['id', ]


class OkResponse(Serializer):
    ok = CharField()


class ErrorResponse(Serializer):
    error = CharField()
