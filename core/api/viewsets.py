# separar das views nativas do django

from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

# é a implementação de um viewset que apenas define um queryset e um serialize
class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # pegar todos os pontos turisicos do banco de dados e coloca no objeto queryset
    queryset = PontoTuristico.objects.all()

    serializer_class = PontoTuristicoSerializer