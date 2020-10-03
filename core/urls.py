from django.urls import path, include
from . import views
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'solar', views.SolarViewSet)


urlpatterns = [
    path('', views.main, name='main'),
    path('rest/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),




]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)