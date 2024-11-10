from django.shortcuts import render

# Create your views here
from rest_framework import generics
from groceryproducts.models import Grocery
from groceryproducts.serializers import GrocerySerializer

class GroceryList(generics.ListCreateAPIView):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer

class GroceryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer
