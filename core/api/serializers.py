from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico, DocIdentificacao, Atracao
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from atracoes.models import Atracao
from enderecos.models import Endereco


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


# Define o model e os campos que eu quero que exiba, apenas a representação do dado
class PontoTuristicoSerializer(ModelSerializer):
    # formas de incluir informações de outras classes no core
    atracoes = AtracaoSerializer(many=True) # um ponto turistico pode ter muitas atrações 
    endereco = EnderecoSerializer() # e só um endereço
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    # descricao_completa = SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()


    # descricao_completa = SerializerMethodField()

    # read_only -> Os campos não vão ser mais obrigatorios, APENAS PARA LEITURA 

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes',
                  'comentarios', 'avaliacoes', 'endereco', 'descricao_completa2', 'doc_identificacao')
        
    # read_only_fields = ('comentarios', 'avaliacao') - se o campo não estiver aqui, só no serializer, colocar esta linha de codigo


    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    # def create(self, validated_data):
    #     atracoes = validated_data["atracoes"]
    #     del validated_data['atracoes']
    #     endereco = validated_data["endereco"]
    #     del validated_data['endereco']
    #     end = Endereco.objects.create(**endereco)
    #     ponto.endereco = end # atrelando ao ponto turistico
    #     ponto = PontoTuristico.objects.create(**validated_data)
    #     self.cria_atracoes(atracoes, ponto)
    #     return ponto

    # Nesta versão corrigida, criou o ponto turístico e o endereço com os dados fornecidos. 
    # Em seguida, juntamos com os dados das atrações, criando cada uma delas e associando-as ao ponto turístico recém-criado.

    def create(self, validated_data):
        atracoes_data = validated_data.pop('atracoes') # Remova os dados de atrações antes de criar o ponto turístico
        endereco_data = validated_data.pop('endereco') # Remova os dados de endereço antes de criar o ponto turístico
        doc_data = validated_data.pop('doc_identificacao')

        doci = DocIdentificacao.objects.create(**doc_data)
        validated_data['doc_identificacao'] = doci

        end = Endereco.objects.create(**endereco_data) # cria um novo objeto Endereco no banco de dados usando o método create. Os dados para criar o endereço são fornecidos como **endereco_data, onde o ** é usado para desempacotar o dicionário endereco_data em argumentos nomeados.
        validated_data['endereco'] = end # atribuir o objeto ao campo endereco dos validated_data. Isso é necessário para garantir que, quando criarmos o objeto PontoTuristico, ele tenha uma referência ao endereço associado.

        ponto = PontoTuristico.objects.create(**validated_data) # ** o proprio python vai interar nesta lista chave valor, ela é de duas dimensoes, por isso 2 asteriscos e automaticamente pegar atributo por atributo e criar o ponto 

        for atracao_data in atracoes_data:
            # atrações está em um for poist pode ser varias atrações para um ponto turistico
            atracao = Atracao.objects.create(**atracao_data)
            ponto.atracoes.add(atracao)

        return ponto



    # Forma de colocar informações comlementares dentro do serializer   
    # Mas o @property é mais utilizado
    # def get_descricao_completa(self, obj):
    #     return '%s + %s' % (obj.nome, obj.descricao)