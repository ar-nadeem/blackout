from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import HeroSerializer, SolarSerializer
from .models import Hero, Solar

from django.http import HttpResponse


def main(request):
    line = "Hello World"
    Solar.objects.all().delete()
    return HttpResponse(line)


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class SolarViewSet(viewsets.ModelViewSet):
    queryset = Solar.objects.all().order_by('gridvoltage')
    serializer_class = SolarSerializer
