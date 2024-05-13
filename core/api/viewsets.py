# separar das views nativas do django
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

# Fez todas as operações do crud, conjunção de varias outras classes
# é a implementação de um viewset que apenas define um queryset e um serialize
class PontoTuristicoViewSet(ModelViewSet):

    # pegar todos os pontos turisicos do banco de dados e coloca no objeto queryset
    # queryset = PontoTuristico.objects.all()
    # queryset = PontoTuristico.objects.filter(aprovado=True) # para mostrar apenas os aprovados

    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        # metodo para as filtragens
        return PontoTuristico.objects.filter(aprovado=True)
    
    # sobreescrevendo os metodos 
    
    # action ligada ao verbo http GET
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()  # Obter o queryset filtrado
        # many=true - serializando uma coleção de objetos ao invés de um único objeto
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)  # Retornar uma resposta HTTP com os dados serializados
    
    # action ligada ao verbo http POST
    def create(self, request, *args, **kwargs):
        # chamando este mesmo metodo lá na super mãe
        return super(PontoTuristico, self).create(request, *args, **kwargs)
    
    # action ligada ao verbo http DELETE
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristico, self).destroy(request, *args, **kwargs)

    # funciona para um GET de um recurso especifico. Exemplo: '/pontoturistico/4'
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristico, self).retrieve(request, *args, **kwargs)

    # put
    def update(self, request, *args, **kwargs):
        return super(PontoTuristico, self).update(request, *args, **kwargs)

    # patch
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristico, self).partial_update(request, *args, **kwargs)

    
    # ACTIONS
    # método para caso deseje denunciar um ponto turistico
    # para um recurso especifico '/pontoturistico/4/denunciar'
    # uso geral '/pontoturistico/teste'

    # delete=false - action relativa ao endpoint não ao  recurso
    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass
