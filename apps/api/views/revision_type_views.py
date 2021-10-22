from rest_framework.generics import ListAPIView
from apps.api.models.revision_type_model import RevisionType
from apps.api.serializers import RevtypeSerializer

class RevisiontypeApiView(ListAPIView):
    serializer_class = RevtypeSerializer
    queryset = RevisionType.objects.all()
