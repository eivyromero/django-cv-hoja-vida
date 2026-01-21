from django.shortcuts import render
from .models import Skill, Project, Education

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    education = Education.objects.all()
    
    context = {
        'skills': skills,
        'projects': projects,
        'education': education,
    }
    return render(request, 'base.html', context)