# Chamada
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404


def home_login(request, template_name="home.html"):
    return render(request, template_name)
