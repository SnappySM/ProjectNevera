from rest_framework import viewsets

from ..serializers import RefrigeratorSerializer
from ..models import Refrigerator

class RefrigeratorViewset(viewsets.ModelViewSet):
    queryset = Refrigerator.objects.all()
    serializer_class = RefrigeratorSerializer