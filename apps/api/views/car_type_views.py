from rest_framework.generics import ListAPIView
from apps.api.models.car_type_model import CarType
from apps.api.serializers import CartypeSerializer

class CartypeApiView(ListAPIView):
    serializer_class = CartypeSerializer
    queryset = CarType.objects.filter(active=1)
