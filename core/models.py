from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

class DocIdentificacao(models.Model):
    # 1 para 1
    description = models.CharField(max_length=100)

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
    # criar um OneToOne
    doc_identificacao = models.OneToOneField(DocIdentificacao, on_delete=models.CASCADE, null=True, blank=True)

    # upload_to - pasta onde vai fazer o upload da imagem 

    @property
    def descricao_completa2(self):
        return '%s + %s' % (self.nome, self.descricao)

    def __str__(self):
        return self.nome

# ManyToManyField - vai ter varios 
# ForeignKey - apenas um