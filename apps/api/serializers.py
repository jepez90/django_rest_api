from rest_framework import serializers

from .models.reserve_model import Reserve
from .models.client_model import Client
from .models.doc_type_model import DocType


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class DocTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocType
        fields = '__all__'


class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'
