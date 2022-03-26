import datetime
from rest_framework import status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from apps.api.models.reserve_model import Reserve
from apps.api.serializers import ReserveSerializer
from apps.api.pagination import CustomPagination
from rest_framework.exceptions import ParseError


# Class to handle reserves
class ReservesListApiView(ListCreateAPIView):
    """ GET:[retrive a list of reserves]
        [you can use the next query params]
        [order_by=date-time [id, plate, date, time, date-time]]
        [count=100 [1 - 500]]
        [date=curdate [yyyy-mm-dd]]
        [filter=plate []]

    """
    serializer_class = ReserveSerializer
    pagination_class = CustomPagination

    queryset = Reserve.objects.all()
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('id', 'date', 'ended', 'plate',
                        'owner', 'driver', 'car_type', 'rev_type')
    search_fields = ['date', 'plate']
    ordering_fields = ['id', 'date', 'plate', 'hour']

    def perform_create(self, serializer):
        return serializer.save()


class ReservesDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReserveSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        msg = 'Client deleted successfully'
        return Response({'message': msg}, status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        objects = Reserve.objects.all()
        return objects

# Class to handle reserves by date
class ReservesListApiViewDate(ListAPIView):
    """ GET:[retrive a list of reserves]
        [you can use the next query params]
        [count=100 [1 - 500]]
        [filter=plate []]

    """
    serializer_class = ReserveSerializer
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('id', 'date', 'ended', 'plate',
                        'owner', 'driver', 'car_type', 'rev_type')
    search_fields = ['date', 'plate']
    ordering_fields = ['id', 'date', 'plate', 'hour']

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """

        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        try:
            date = datetime.datetime(year, month, day)
        except ValueError as err:
            raise ParseError(detail="Fecha No Valida", code=400)
        return Reserve.objects.filter(date=date).order_by("hour")
