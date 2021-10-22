from rest_framework.generics import ListAPIView
from apps.api.models.doc_type_model import DocType
from apps.api.serializers import DoctypeSerializer

class DoctypeApiView(ListAPIView):
    serializer_class = DoctypeSerializer
    queryset = DocType.objects.all()
