from rest_framework import viewsets

from ..serializers import ItemSerializer
from ..models import Item

class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer