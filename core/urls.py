from django.urls import path, include
from . import views
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.main, name='main'),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)