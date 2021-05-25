# Chamada
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404


def home_dashboard(request, template_name="dashboard/home.html"):
    return render(request, template_name)
