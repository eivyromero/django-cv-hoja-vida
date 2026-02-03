import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import (
    Profile, Skill, Experience, Education,
    Course, Award, Project, Service
)

# ==================== VISTA PRINCIPAL ====================
def home(request):
    profile, created = Profile.objects.get_or_create(id=1)

    context = {
        'profile': profile,
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'education': Education.objects.all(),
        'courses': Course.objects.all(),
        'awards': Award.objects.all(),
        'projects': Project.objects.all(),
        'services': Service.objects.all(),
    }

    return render(request, 'home.html', context)
# ==================== API - PERFIL ====================
def api_profile(request):
    profile, created = Profile.objects.get_or_create(id=1)

    data = {
        'name': profile.name,
        'title': profile.title,
        'email': profile.email,
        'phone': profile.phone,
        'location': profile.location,
        'description': profile.description,
        'profile_image': profile.profile_image.url if profile.profile_image else None,
    }
    return JsonResponse(data)


@csrf_exempt
@require_http_methods(["POST"])
def api_profile_update(request):
    data = json.loads(request.body)
    profile, _ = Profile.objects.get_or_create(id=1)

    profile.name = data.get('name', profile.name)
    profile.title = data.get('title', profile.title)
    profile.email = data.get('email', profile.email)
    profile.phone = data.get('phone', profile.phone)
    profile.location = data.get('location', profile.location)
    profile.description = data.get('description', profile.description)
    profile.save()

    return JsonResponse({'success': True})


# ==================== API - HABILIDADES ====================
def api_skills(request):
    skills = Skill.objects.all()
    data = [{
        'id': s.id,
        'name': s.name,
        'category': s.category,
        'icon': s.icon,
        'level': s.level,
    } for s in skills]

    return JsonResponse(data, safe=False)
# ==================== API - EXPERIENCIAS ====================
def api_experiences(request):
    experiences = Experience.objects.all().order_by('-start_date')

    data = [{
        'id': e.id,
        'company': e.company,
        'position': e.position,
        'description': e.description,
        'start_date': e.start_date,
        'end_date': e.end_date,
        'is_current': e.is_current,
        'technologies': e.technologies,
    } for e in experiences]

    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def api_experience_create(request):
    data = json.loads(request.body)

    Experience.objects.create(
        company=data['company'],
        position=data['position'],
        description=data['description'],
        start_date=data['start_date'],
        end_date=data.get('end_date'),
        is_current=data.get('is_current', False),
        technologies=data.get('technologies', ''),
    )

    return JsonResponse({'success': True})


@csrf_exempt
@require_http_methods(["PUT"])
def api_experience_update(request, exp_id):
    data = json.loads(request.body)
    exp = get_object_or_404(Experience, id=exp_id)

    exp.company = data['company']
    exp.position = data['position']
    exp.description = data['description']
    exp.start_date = data['start_date']
    exp.end_date = data.get('end_date')
    exp.is_current = data.get('is_current', False)
    exp.technologies = data.get('technologies', '')
    exp.save()

    return JsonResponse({'success': True})


@csrf_exempt
@require_http_methods(["DELETE"])
def api_experience_delete(request, exp_id):
    get_object_or_404(Experience, id=exp_id).delete()
    return JsonResponse({'success': True})
# ==================== API - EDUCACIÓN ====================
def api_education(request):
    education = Education.objects.all()
    data = [{
        'id': e.id,
        'institution': e.institution,
        'degree': e.degree,
        'start_date': e.start_date,
        'end_date': e.end_date,
        'description': e.description,
    } for e in education]

    return JsonResponse(data, safe=False)


# ==================== API - CURSOS ====================
def api_courses(request):
    courses = Course.objects.all()
    data = [{
        'id': c.id,
        'name': c.name,
        'institution': c.institution,
        'date': c.date,
        'description': c.description,
    } for c in courses]

    return JsonResponse(data, safe=False)


# ==================== API - RECONOCIMIENTOS ====================
def api_awards(request):
    awards = Award.objects.all()
    data = [{
        'id': a.id,
        'title': a.title,
        'organization': a.organization,
        'date': a.date,
        'description': a.description,
    } for a in awards]

    return JsonResponse(data, safe=False)
