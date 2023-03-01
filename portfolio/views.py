from django.shortcuts import render
from .models import Project

# Create your views here.

# домашня сторінка портфоліо
def portfolio_home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio_home.html', {'projects': projects})
