from rest_framework import viewsets

from ..serializers import FoodSerializer
from ..models import Food

class FoodViewset(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer