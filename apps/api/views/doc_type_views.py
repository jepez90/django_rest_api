from rest_framework.generics import ListAPIView
from rest_framework import permissions
from apps.api.models.doc_type_model import DocType
from apps.api.serializers import DoctypeSerializer

class DoctypeApiView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DoctypeSerializer
    queryset = DocType.objects.all()
