# separar das views nativas do django

from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

# Fez todas as operações do crud, conjunção de varias outras classes
# é a implementação de um viewset que apenas define um queryset e um serialize
class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # pegar todos os pontos turisicos do banco de dados e coloca no objeto queryset
    # queryset = PontoTuristico.objects.all()
    # queryset = PontoTuristico.objects.filter(aprovado=True) # para mostrar apenas os aprovados

    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        # metodo para as filtragens
        return PontoTuristico.objects.filter(aprovado=True)
    
    def list(self, request, *args, **kwargs):
        pass