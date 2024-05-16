from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer

# Define o model e os campos que eu quero que exiba, apenas a representação do dado
class PontoTuristicoSerializer(ModelSerializer):
    # formas de incluir informações de outras classes no core
    atracoes = AtracaoSerializer(many=True, read_only=True) # um ponto turistico pode ter muitas atrações 
    endereco = EnderecoSerializer(read_only=True) # e só um endereço
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)

    # descricao_completa = SerializerMethodField()

    # read_only -> Os campos não vão ser mais obrigatorios 

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes',
                  'comentarios', 'avaliacoes', 'endereco', 'descricao_completa2')
        
    # read_only_fields = ('comentarios', 'avaliacao') - se o campo não estier aqui só serializer, so colocar esta linha de codigo
        
    # Forma de colocar informações comlementares dentro do serializer   
    # Mas o @property é mais utilizado
    # def get_descricao_completa(self, obj):
    #     return '%s + %s' % (obj.nome, obj.descricao)