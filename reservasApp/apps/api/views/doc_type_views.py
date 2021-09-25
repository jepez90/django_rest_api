from rest_framework.decorators import api_view
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.response import Response
from apps.api.models.doc_type_model import DocType
from apps.api.serializers import DocTypeSerializer

# Create your views here.


# view doc_types
@api_view(['GET'])
@cache_page(60*60*12)
def doc_types_api_view(request):
    """ list doc_types """
    if request.method == 'GET':
        doc_types = DocType.objects.all()
        doc_types_serialized = DocTypeSerializer(doc_types, many=True)
        return Response(doc_types_serialized.data, status=status.HTTP_200_OK)
