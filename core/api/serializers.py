from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from atracoes.models import Atracao
from enderecos.models import Endereco

# Define o model e os campos que eu quero que exiba, apenas a representação do dado
class PontoTuristicoSerializer(ModelSerializer):
    # formas de incluir informações de outras classes no core
    atracoes = AtracaoSerializer(many=True) # um ponto turistico pode ter muitas atrações 
    endereco = EnderecoSerializer(read_only=True) # e só um endereço
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)

    # descricao_completa = SerializerMethodField()

    # read_only -> Os campos não vão ser mais obrigatorios, APENAS PARA LEITURA 

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes',
                  'comentarios', 'avaliacoes', 'endereco', 'descricao_completa2')
        
    # read_only_fields = ('comentarios', 'avaliacao') - se o campo não estiver aqui, só no serializer, colocar esta linha de codigo


    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data["atracoes"]
        del validated_data['atracoes']

        endereco = validated_data["endereco"]
        del validated_data['endereco']

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end

        ponto = PontoTuristico.objects.create(**validated_data) # ** o proprio python vai interar nesta lista chave valor, ela é de duas dimensoes, por isso 2 asteriscos e automaticamente pegar atributo por atributo e criar o ponto 
        self.cria_atracoes(atracoes, ponto)

        return ponto


    # Forma de colocar informações comlementares dentro do serializer   
    # Mas o @property é mais utilizado
    # def get_descricao_completa(self, obj):
    #     return '%s + %s' % (obj.nome, obj.descricao)