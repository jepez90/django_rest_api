from rest_framework import serializers

from .models.reserve_model import Reserve
from .models.client_model import Client
from .models.doc_type_model import DocType
from .models.car_type_model import CarType
from .models.revision_type_model import RevisionType


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class DoctypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocType
        fields = '__all__'


class ReserveSerializer(serializers.ModelSerializer):

    driver = serializers.SlugRelatedField(slug_field='full_name',queryset=Client.objects.all())
    class Meta:
        model = Reserve
        fields = '__all__'

class CartypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ['id', 'name']

class RevtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevisionType
        fields = '__all__'
