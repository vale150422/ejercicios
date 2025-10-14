from django.shortcuts import render
from rest_framework import viewsets
from .models import Ropa
from .serializers import RopaSerializer

class RopaViewSet(viewsets.ModelViewSet):
    queryset = Ropa.objects.all()
    serializer_class = RopaSerializer

def inicio(request):
    return render(request, 'inicio.html')
