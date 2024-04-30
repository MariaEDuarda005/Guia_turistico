from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from core.api.viewsets import PontoTuristicoViewSet
from rest_framework import routers

# criou as rotas
router = routers.DefaultRouter()
# registrou uma rota chamada pontoturistico que recebe o viewset
router.register(r'pontoturistico', PontoTuristicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
