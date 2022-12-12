from django.shortcuts import render

from .models import Project


def index(request):
    projects = Project.objects.all()
    context = {
        'title': 'Портфолио',
        'projects': projects
               }
    return render(request, 'portfolio/index.html', context=context)