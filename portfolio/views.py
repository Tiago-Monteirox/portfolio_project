from django.shortcuts import render
from .models import Project, Profile

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {
        'profile': profile,
        'projects': projects
    })