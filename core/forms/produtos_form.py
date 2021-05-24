from django import forms
from django_select2 import forms as select
from ..models import Produtos


class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'preco', 'descricao', 'estado']

        widgets = {
            'estado': select.Select2Widget(attrs={'style': 'width: 100%'})
        }
        help_texts = {
            'nome': 'Informe o nome do produto',
            'preco': 'Informe o preço do produto',
            'descricao': 'Informe uma descrição',
            'estado': 'Informe o estado do produto'
        }