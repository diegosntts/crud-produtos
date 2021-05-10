from django.db import models
from django.utils.text import slugify
from ..abstracts import TimestampsAbstract
from django.urls import reverse

# Timestamps
class Produtos(TimestampsAbstract, models.Model):
    CIDADE = (
        ('Macapá', 'Macapá'),
        ('Belém', 'Belém')
    )
    nome = models.CharField('Nome', max_length=254, null=False)
    preco = models.CharField('Preço', max_length=254, null=False)
    cidade = models.CharField('cidade', choices=CIDADE, max_length=50)

    def __str__(self):
        return f'{self.nome} - {self.cidade}'

    class Meta:
        app_label = 'core'