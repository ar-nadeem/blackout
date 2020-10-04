from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import HeroSerializer, SolarSerializer
from .models import Hero, Solar
from django.shortcuts import render

from django.http import HttpResponse


def main(request):
    import http.client
    import json

    conn = http.client.HTTPSConnection('api.pipedream.com')
    conn.request("GET", '/v1/sources/dc_lVuxEY/event_summaries?limit=1', '', {
        'Authorization': 'Bearer b6283d5b52f9bc13ac965d5c8282ad60',
    })

    res = conn.getresponse()
    data = res.read()
    body = data.decode("utf-8")
    body = body[body.find('"{\\"mode') + 1:body.find('"metadata') - 2]
    body = body.replace("\\", "")
    body = body.replace(" ", "")


    def get_me(x):
        x = body[body.find('"'+x+'":') + 3+len(x):]
        x = x[:x.find(",")]
        return x


    mode = get_me("mode")
    if mode == "Sola":
        mode = "Solar / Battery"
    else:
        mode = "Grid"


    stuff_for_frontend = {
        'mode': mode,

        'gridVoltage': get_me("gridVoltage"),
        'gridFreq': get_me("gridFreq"),
        'outputVoltage': get_me("outputVoltage"),
        'outputFreq': get_me("outputFreq"),

        'outputPowerApparent': get_me("outputPowerApparent"),
        'outputPowerActive': get_me("outputPowerActive"),
        'loadPercent': get_me("loadPercent"),

        'busVoltage': get_me("busVoltage"),
        'batteryVoltage': get_me("batteryVoltage"),
        'batteryCurrent': get_me("batteryCurrent"),
        'batteryCapacity': get_me("batteryCapacity"),
        'batteryVoltageSCC': get_me("batteryVoltageSCC"),
        'batteryDischargeCurrent': get_me("batteryDischargeCurrent"),

        'temperature': get_me("temperature"),
        'solarCurrent': get_me("solarCurrent"),
        'solarVoltage': get_me("solarVoltage"),


        'status': get_me("status"),
        'warning': get_me("warning"),



    }

    return render(request, 'index.html', stuff_for_frontend)