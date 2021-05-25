# Chamada
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

@login_required
def home_dashboard(request, template_name="dashboard/home.html"):
    return render(request, template_name)
