from django.shortcuts import render
from .models import Skill, Project, Education

def home(request):
    skills = []
    projects = []
    education = []

    try:
        skills = Skill.objects.all()
    except Exception as e:
        print("Skill error:", e)

    try:
        projects = Project.objects.all()
    except Exception as e:
        print("Project error:", e)

    try:
        education = Education.objects.all()
    except Exception as e:
        print("Education error:", e)

    return render(request, 'home.html', {
        'skills': skills,
        'projects': projects,
        'education': education
    })
