from rest_framework import serializers
from .models import User, Refrigerator, Food, Item

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["mail", "username", "bio", "avatar", "refrigerator"]

class RefrigeratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Refrigerator
        fields = ["id", "name", "description"]

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ["id", "name", "quantity", "quantity_unit"]

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "expirationDate", "price", "food", "refrigerator"]