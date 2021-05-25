# Chamada 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings

# view pagina inicial
@login_required
def home_page(request, template_name="home.html"):
    return render(request, template_name)

