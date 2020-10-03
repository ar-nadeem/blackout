from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class SolarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solar
        fields = ('created',
        'mode', 'gridvoltage', 'gridfreq', 'outputvoltage', 'outputfreq', 'outputpowerapparent', 'outputpoweractive',
        'loadpercent', 'busvoltage', 'batteryvoltage', 'batterycurrent', 'battery_capacity', 'temperature',
        'solar_current', 'solar_voltage', 'battery_voltage_scc', 'battery_dis_current', 'status', 'warning')