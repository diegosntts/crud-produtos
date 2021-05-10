# Chamadas 
from django.urls import path, include
from .views import *

urlpatterns = [
    # Rotas de home
    path('', home_page, name="home_page"),

    # Rotas de produtos
    path('produtos/', home_produtos, name="home_produtos"),
    path('produtos/cadastrar', cadastrar_produtos, name="cadastrar_produtos"),
    path('produtos/editar/<int:pk>', editar_produtos, name="editar_produtos"),
    # Rotas de profile

    # Rotas de help
]
