from django.db import models
import datetime
# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Solar(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    mode = models.CharField(max_length=60,blank=True)
    gridvoltage = models.CharField(max_length=60,blank=True)
    gridfreq = models.CharField(max_length=60,blank=True)
    outputvoltage = models.CharField(max_length=60,blank=True)
    outputfreq = models.CharField(max_length=60,blank=True)
    outputpowerapparent = models.CharField(max_length=60,blank=True)
    outputpoweractive = models.CharField(max_length=60,blank=True)
    loadpercent = models.CharField(max_length=60,blank=True)
    busvoltage = models.CharField(max_length=60,blank=True)
    batteryvoltage = models.CharField(max_length=60,blank=True)
    batterycurrent = models.CharField(max_length=60,blank=True)
    battery_capacity = models.CharField(max_length=60,blank=True)
    temperature = models.CharField(max_length=60,blank=True)
    solar_current = models.CharField(max_length=60,blank=True)
    solar_voltage = models.CharField(max_length=60,blank=True)
    battery_voltage_scc = models.CharField(max_length=60,blank=True)
    battery_dis_current = models.CharField(max_length=60,blank=True)
    status = models.CharField(max_length=60,blank=True)
    warning = models.CharField(max_length=60,blank=True)
    def __str__(self):
        return self.gridvoltage