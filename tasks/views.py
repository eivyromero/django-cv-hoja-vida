from django.shortcuts import render
from .models import Skill, Project, Education

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    education = Education.objects.all()

    return render(request, "home.html", {
        "skills": skills,
        "projects": projects,
        "education": education,
    })
