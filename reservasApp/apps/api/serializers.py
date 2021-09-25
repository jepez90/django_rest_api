from rest_framework import serializers
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
