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
from django.http import HttpResponse
from django.contrib.auth import get_user_model

def create_admin(request):
    User = get_user_model()

    if User.objects.filter(username="admin").exists():
        return HttpResponse("El superusuario ya existe ✅")

    User.objects.create_superuser(
        username="admin",
        email="admin@admin.com",
        password="Admin1234"
    )
    return HttpResponse("Superusuario creado correctamente 🎉")
