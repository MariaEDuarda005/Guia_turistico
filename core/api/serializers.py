from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico

# Define o model e os campos que eu quero que exiba, apenas a representação do dado
class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado')