from django.db import models
from django.utils.text import slugify
from ..abstracts import TimestampsAbstract
from django.urls import reverse

# Timestamps
class Produtos(TimestampsAbstract, models.Model):
    ESTADO = (
        ('Novo', 'Novo'),
        ('Usado', 'Usado')
    )
    nome = models.CharField('Nome', max_length=254, null=False)
    preco = models.CharField('Preço', max_length=254, null=False)
    descricao = models.TextField('Descrição', max_length=254, null=False, blank=True)
    estado = models.CharField('Estado', choices=ESTADO, max_length=50)
    
    def __str__(self):
        return f'{self.nome}'

    class Meta:
        app_label = 'core'