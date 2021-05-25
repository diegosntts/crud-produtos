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
    path('produtos/info/<int:pk>', info_produtos, name="info_produtos"),
    
    # Rotas de dasboard
    
    path('dashboard', home_dashboard, name="home_dashboard"),

    # Rotas de login
    path('login', home_login, name="home_login")
]
