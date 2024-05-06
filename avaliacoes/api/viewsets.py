# separar das views nativas do django
from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer