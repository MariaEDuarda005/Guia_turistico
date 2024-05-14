from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

# bibliooteca de imagens 
from django.conf import settings
from django.conf.urls.static import static

from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from rest_framework.authtoken.views import obtain_auth_token

# criou as rotas
router = routers.DefaultRouter()
# registrou uma rota que recebe o viewset
router.register(r'pontoturistico', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token), # endpoint para autenticação
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
