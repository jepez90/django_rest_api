from rest_framework.decorators import api_view
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.response import Response
from apps.api.models.doc_type_model import DocType
from apps.api.serializers import DocTypeSerializer

# Create your views here.


# view doc_types list
@api_view(['GET'])
@cache_page(60*60*12)
def doctypes_list_view(request):
    """ list all doc_types """

    # get all doctype objects from database in a list
    doc_types = DocType.objects.all()

    # serialize the list of instances
    doc_types_serialized = DocTypeSerializer(doc_types, many=True)

    # return the serialized data
    return Response(doc_types_serialized.data, status=status.HTTP_200_OK)


# view doc_types details
@api_view(['GET'])
@cache_page(60*60*12)
def doctypes_detail_view(request, id=None):
    """ show a doc_type info by its id """

    # get the object with the given id
    doc_type = DocType.objects.all().filter(id=id)

    # Check if exist any instance with the given id
    if len(doc_type) == 0:
        # return error if no instance found
        msg = 'Doesn´t exist a doc_type with id={}'.format(id)
        return Response({'message': msg}, status=status.HTTP_404_NOT_FOUND)

    # serialize the found instance
    doc_type_serialized = DocTypeSerializer(doc_type[0])

    # return the serialized data
    return Response(doc_type_serialized.data, status=status.HTTP_200_OK)
