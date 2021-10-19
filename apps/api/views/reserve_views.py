from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from apps.api.models.reserve_model import Reserve
from apps.api.serializers import ReserveSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Class to handle reserves
class ReservsApiView(ListCreateAPIView):
    serializer_class = ReserveSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Reserve.objects.all()


class ReservsDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReserveSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        print(self)
        return []

    def get_queryset(self):
        return Reserve.objects.all()
