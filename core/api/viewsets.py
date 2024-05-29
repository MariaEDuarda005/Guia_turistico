# separar das views nativas do django
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponse


# Fez todas as operações do crud, conjunção de varias outras classes
# é a implementação de um viewset que apenas define um queryset e um serialize
class PontoTuristicoViewSet(ModelViewSet):

    # metodo para as filtragens, apenas os aprovados
    # PontoTuristico.objects.filter(aprovado=True)

    serializer_class = PontoTuristicoSerializer

    # habilitando mais buscas no endpoint

    filter_backends = [SearchFilter]

    # fazendo a busca pelo endereço e mudando o lockup_prefixes
    #  lookup_prefixes = {
    #     '^': 'istartswith', 
    #     '=': 'iexact',
    #     '@': 'search',
    #     '$': 'iregex',
    # }

    # https://www.django-rest-framework.org/api-guide/permissions/
    
    # 'permission_classes' permite você setar permissões para cada endPoint
    # no caso estamos pedindo que o usuário no minimo esteja autenticado.
    
    # AllowAny - permitirá acesso irrestrito
    
    # IsAuthenticated - Vai negar acesso a qualquer usuário não autenticado
    
    # IsAdminUser - vai negar acesso a qualquer usuário que não tenha o 'is_staff' como 'true'

    # IsAuthenticatedOrReadOnly - permitirá que usuários autenticados executem qualquer solicitação.
    # Solicitações para usuários não autenticados somente serão permitidas se o método de solicitação for um dos métodos “seguros” por exemplo um 'GET'
    # só permitira você ver as informações caso não autenticado

    # DjangoModelPermissions - Ele mostra um resultado porem não autoriza que você faça alguma ação se não tiver a permissão especifica para aquele método ou tabela
    # O próprio django ja ve as opções que o seu backend possuem e ja cria um sistema de permissões para os usuários só precisa definir

    # permission_classes = (IsAuthenticated, ) # solicitar que para fazer a autenticação - pode ser qualquer um desses IsAuthenticated, IsAdminUser
    permission_classes = ()
    authentication_classes = (TokenAuthentication,)

    # endereco__linha1 - fazendo referencia a outra classe
    search_fields = ['^nome', '^descricao', '^endereco__linha1'] # ^ se a palavra começa com aquilo, ele vai trazer, se quiser a busca exata coloque =

    # lookup_field = 'nome' # ao inves de fazer a pesquisa pelo id, será pelo nome, o unico problema é que se tiver dois pontos com o mesmo nome vai dar erro

    def get_queryset(self):
        id = self.request.query_params.get('id', None) # Se a pessoa não passar o id atribui como none 
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all() # pegar todos os pontos turisicos do banco de dados e coloca no objeto queryset

        # "__iexact" nos filtros de nome e descrição. Isso significa que a comparação será feita sem diferenciar maiúsculas de minúsculas.

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset
    
    # sobreescrevendo os metodos 
    
    # action ligada ao verbo http GET, está dando erro no serializer, por isso está comentada
    # def list(self, request, *args, **kwargs):
    #     return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)
    
    # action ligada ao verbo http POST
    def create(self, request, *args, **kwargs):
        # chamando este mesmo metodo lá na super mãe
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
    
    # action ligada ao verbo http DELETE
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    # funciona para um GET de um recurso especifico. Exemplo: '/pontoturistico/4'
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    # put
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    # patch
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    
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

    # atrelar os objetos
    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, pk=None):
        atracoes = request.data['ids']
        
        ponto = self.get_object()  # Obtenha o objeto PontoTuristico associado ao 'pk'
        ponto.atracoes.set(atracoes)
        ponto.save()
        
        return Response('Ok!')