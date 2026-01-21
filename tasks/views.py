from django.shortcuts import render
from .models import Project, Education, Skill

def home(request):
    projects = Project.objects.all() if Project.objects.exists() else []
    education = Education.objects.all() if Education.objects.exists() else []
    skills = Skill.objects.all() if Skill.objects.exists() else []

    return render(request, "home.html", {
        "projects": projects,
        "education": education,
        "skills": skills,
    })
