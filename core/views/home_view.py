# Chamada 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

# view pagina inicial
def home_page(request, template_name="home.html"):
    return render(request, template_name)

