from django.shortcuts import render

# import viewset, local data
from rest_framework import viewsets
from .serializers import apiserializer
from .models import apiModel

# Create your views here.
class apiViewSet(viewsets.ModelViewSet):
    queryset = apiModel.objects.all()
    serializer_class = apiserializer