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
    """Vista principal que renderiza el CV con todos los datos"""
    profile, created = Profile.objects.get_or_create(id=1)

    context = {
        'profile': profile,
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all().order_by('-start_date'),
        'education': Education.objects.all().order_by('-start_date'),
        'courses': Course.objects.all().order_by('-date'),
        'awards': Award.objects.all().order_by('-date'),
        'projects': Project.objects.all(),
        'services': Service.objects.all(),
    }

    return render(request, 'home.html', context)


# ==================== API - PERFIL ====================
def api_profile(request):
    """Obtener información del perfil"""
    profile, created = Profile.objects.get_or_create(id=1)

    data = {
        'id': profile.id,
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
    """Actualizar información del perfil"""
    try:
        data = json.loads(request.body)
        profile, _ = Profile.objects.get_or_create(id=1)

        profile.name = data.get('name', profile.name)
        profile.title = data.get('title', profile.title)
        profile.email = data.get('email', profile.email)
        profile.phone = data.get('phone', profile.phone)
        profile.location = data.get('location', profile.location)
        profile.description = data.get('description', profile.description)
        profile.save()

        return JsonResponse({'success': True, 'message': 'Perfil actualizado correctamente'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


# ==================== API - HABILIDADES ====================
def api_skills(request):
    """Obtener todas las habilidades"""
    skills = Skill.objects.all()
    data = [{
        'id': s.id,
        'name': s.name,
        'category': s.category,
        'icon': s.icon,
        'level': s.level,
    } for s in skills]

    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def api_skill_create(request):
    """Crear nueva habilidad"""
    try:
        data = json.loads(request.body)
        
        skill = Skill.objects.create(
            name=data['name'],
            category=data.get('category', ''),
            icon=data.get('icon', ''),
            level=data.get('level', 0),
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Habilidad creada correctamente',
            'id': skill.id
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def api_skill_update(request, skill_id):
    """Actualizar habilidad existente"""
    try:
        data = json.loads(request.body)
        skill = get_object_or_404(Skill, id=skill_id)
        
        skill.name = data.get('name', skill.name)
        skill.category = data.get('category', skill.category)
        skill.icon = data.get('icon', skill.icon)
        skill.level = data.get('level', skill.level)
        skill.save()
        
        return JsonResponse({'success': True, 'message': 'Habilidad actualizada correctamente'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def api_skill_delete(request, skill_id):
    """Eliminar habilidad"""
    try:
        get_object_or_404(Skill, id=skill_id).delete()
        return JsonResponse({'success': True, 'message': 'Habilidad eliminada correctamente'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


# ==================== API - EXPERIENCIAS ====================
def api_experiences(request):
    """Obtener todas las experiencias laborales"""
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
    """Crear nueva experiencia laboral"""
    try:
        data = json.loads(request.body)

        experience = Experience.objects.create(
            company=data['company'],
            position=data['position'],
            description=data['description'],
            start_date=data['start_date'],
            end_date=data.get('end_date'),
            is_current=data.get('is_current', False),
            technologies=data.get('technologies', ''),
        )

        return JsonResponse({
            'success': True,
            'message': 'Experiencia creada correctamente',
            'id': experience.id
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def api_experience_update(request, exp_id):
    """Actualizar experiencia laboral existente"""
    try:
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

        return JsonResponse({'success': True, 'message': 'Experiencia actualizada correctamente'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def api_experience_delete(request, exp_id):
    """Eliminar experiencia laboral"""
    try:
        get_object_or_404(Experience, id=exp_id).delete()
        return JsonResponse({'success': True, 'message': 'Experiencia eliminada correctamente'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


# ==================== API - EDUCACIÓN ====================
def api_education(request):
    """Obtener toda la educación"""
    education = Education.objects.all().order_by('-start_date')
    data = [{
        'id': e.id,
        'institution': e.institution,
        'degree': e.degree,
        'start_date': e.start_date,
        'end_date': e.end_date,
        'description': e.description,
    } for e in education]

    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def api_education_create(request):
    """Crear nueva educación"""
    try:
        data = json.loads(request.body)
        
        education = Education.objects.create(
            institution=data['institution'],
            degree=data['degree'],
            start_date=data['start_date'],
            end_date=data.get('end_date'),
            description=data.get('description', ''),
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Educación creada correctamente',
            'id': education.id
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def api_education_update(request, edu_id):
    """Actualizar educación existente"""
    try:
        data = json.loads(request.body)
        edu = get_object_or_404(Education, id=edu_id)
        
        edu.institution = data['institution']
        edu.degree = data['degree']
        edu.start_date = data['start_date']
        edu.end_date = data.get('end_date')
        edu.description = data.get('description', '')
        edu.save()
        
        return JsonResponse({'success': True, 'message': 'Educación actualizada correctamente'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def api_education_delete(request, edu_id):
    """Eliminar educación"""
    try:
        get_object_or_404(Education, id=edu_id).delete()
        return JsonResponse({'success': True, 'message': 'Educación eliminada correctamente'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


# ==================== API - CURSOS ====================
def api_courses(request):
    """Obtener todos los cursos"""
    courses = Course.objects.all().order_by('-date')
    data = [{
        'id': c.id,
        'name': c.name,
        'institution': c.institution,
        'date': c.date,
        'description': c.description,
    } for c in courses]

    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def api_course_create(request):
    """Crear nuevo curso"""
    try:
        data = json.loads(request.body)
        
        course = Course.objects.create(
            name=data['name'],
            institution=data['institution'],
            date=data['date'],
            description=data.get('description', ''),
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Curso creado correctamente',
            'id': course.id
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def api_course_update(request, course_id):
    """Actualizar curso existente"""
    try:
        data = json.loads(request.body)
        course = get_object_or_404(Course, id=course_id)
        
        course.name = data['name']
        course.institution = data['institution']
        course.date = data['date']
        course.description = data.get('description', '')
        course.save()
        
        return JsonResponse({'success': True, 'message': 'Curso actualizado correctamente'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def api_course_delete(request, course_id):
    """Eliminar curso"""
    try:
        get_object_or_404(Course, id=course_id).delete()
        return JsonResponse({'success': True, 'message': 'Curso eliminado correctamente'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


# ==================== API - RECONOCIMIENTOS ====================
def api_awards(request):
    """Obtener todos los reconocimientos"""
    awards = Award.objects.all().order_by('-date')
    data = [{
        'id': a.id,
        'title': a.title,
        'organization': a.organization,
        'date': a.date,
        'description': a.description,
    } for a in awards]

    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def api_award_create(request):
    """Crear nuevo reconocimiento"""
    try:
        data = json.loads(request.body)
        
        award = Award.objects.create(
            title=data['title'],
            organization=data['organization'],
            date=data['date'],
            description=data.get('description', ''),
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Reconocimiento creado correctamente',
            'id': award.id
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def api_award_update(request, award_id):
    """Actualizar reconocimiento existente"""
    try:
        data = json.loads(request.body)
        award = get_object_or_404(Award, id=award_id)
        
        award.title = data['title']
        award.organization = data['organization']
        award.date = data['date']
        award.description = data.get('description', '')
        award.save()
        
        return JsonResponse({'success': True, 'message': 'Reconocimiento actualizado correctamente'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def api_award_delete(request, award_id):
    """Eliminar reconocimiento"""
    try:
        get_object_or_404(Award, id=award_id).delete()
        return JsonResponse({'success': True, 'message': 'Reconocimiento eliminado correctamente'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


# ==================== API - PROYECTOS ====================
def api_projects(request):
    """Obtener todos los proyectos"""
    projects = Project.objects.all()
    data = [{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'technologies': p.technologies,
        'url': p.url,
        'image': p.image.url if p.image else None,
    } for p in projects]

    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def api_project_create(request):
    """Crear nuevo proyecto"""
    try:
        data = json.loads(request.body)
        
        project = Project.objects.create(
            name=data['name'],
            description=data['description'],
            technologies=data.get('technologies', ''),
            url=data.get('url', ''),
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Proyecto creado correctamente',
            'id': project.id
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def api_project_delete(request, project_id):
    """Eliminar proyecto"""
    try:
        get_object_or_404(Project, id=project_id).delete()
        return JsonResponse({'success': True, 'message': 'Proyecto eliminado correctamente'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


# ==================== API - SERVICIOS ====================
def api_services(request):
    """Obtener todos los servicios"""
    services = Service.objects.all()
    data = [{
        'id': s.id,
        'name': s.name,
        'description': s.description,
        'icon': s.icon,
    } for s in services]

    return JsonResponse(data, safe=False)