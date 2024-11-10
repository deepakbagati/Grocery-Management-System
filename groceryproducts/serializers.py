from rest_framework import serializers
from groceryproducts.models import Grocery

class GrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        fields = ['id', 'name', 'price', 'quantity']
