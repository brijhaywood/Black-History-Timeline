from django.shortcuts import render
from .serializers import FactsSerializer 
from rest_framework import viewsets      
from .models import Facts

# Create your views here.
class FactsView(viewsets.ModelViewSet):  
    serializer_class = FactsSerializer   
    queryset = Facts.objects.all() 