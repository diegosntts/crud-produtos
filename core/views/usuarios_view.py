from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import InvalidPage, Paginator
from django.shortcuts import redirect, render, get_object_or_404

@login_required
def home_usuarios(request, template_name='usuarios/home.html'):
    return render (request, template_name)