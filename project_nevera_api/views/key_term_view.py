from rest_framework import viewsets

from ..serializers import KeyTermSerializer
from ..models import KeyTerm

class KeyTermViewset(viewsets.ModelViewSet):
    queryset = KeyTerm.objects.all()
    serializer_class = KeyTermSerializer