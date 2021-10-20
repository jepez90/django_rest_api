from django_filters.filters import OrderingFilter
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from apps.api.models.reserve_model import Reserve
from apps.api.serializers import ReserveSerializer
from apps.api.pagination import CustomPagination


# Class to handle reserves
class ReservsApiView(ListCreateAPIView):
    """ GET:----retrive a list of reserves
        ------->you can use the next query params
        ------->order_by=date-time [id, plate, date, time, date-time]
        ------->count=100 [1 - 500]
        ------->date=curdate [yyyy-mm-dd]
        ------->filter=plate []

    """
    serializer_class = ReserveSerializer
    pagination_class = CustomPagination

    queryset = Reserve.objects.all()
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('id', 'date', 'ended', 'plate',
                        'owner', 'driver', 'car_type', 'rev_type')
    search_fields = ['date', 'plate']
    ordering_fields = ['id', 'date', 'plate']

    def perform_create(self, serializer):
        return serializer.save()


class ReservsDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReserveSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        print(self)

        msg = 'Client deleted successfully'
        return Response({'message': msg}, status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        return Reserve.objects.all()
