from django.urls import path
from . import views

urlpatterns = [
    # ==================== VISTA PRINCIPAL ====================
    path('', views.home, name='home'),

    # ==================== API - PERFIL ====================
    path('api/profile/', views.api_profile, name='api_profile'),
    path('api/profile/update/', views.api_profile_update, name='api_profile_update'),

    # ==================== API - HABILIDADES ====================
    path('api/skills/', views.api_skills, name='api_skills'),
    path('api/skills/create/', views.api_skill_create, name='api_skill_create'),
    path('api/skills/<int:skill_id>/update/', views.api_skill_update, name='api_skill_update'),
    path('api/skills/<int:skill_id>/delete/', views.api_skill_delete, name='api_skill_delete'),

    # ==================== API - EXPERIENCIAS ====================
    path('api/experiences/', views.api_experiences, name='api_experiences'),
    path('api/experiences/create/', views.api_experience_create, name='api_experience_create'),
    path('api/experiences/<int:exp_id>/update/', views.api_experience_update, name='api_experience_update'),
    path('api/experiences/<int:exp_id>/delete/', views.api_experience_delete, name='api_experience_delete'),

    # ==================== API - EDUCACIÓN ====================
    path('api/education/', views.api_education, name='api_education'),
    path('api/education/create/', views.api_education_create, name='api_education_create'),
    path('api/education/<int:edu_id>/update/', views.api_education_update, name='api_education_update'),
    path('api/education/<int:edu_id>/delete/', views.api_education_delete, name='api_education_delete'),

    # ==================== API - CURSOS ====================
    path('api/courses/', views.api_courses, name='api_courses'),
    path('api/courses/create/', views.api_course_create, name='api_course_create'),
    path('api/courses/<int:course_id>/update/', views.api_course_update, name='api_course_update'),
    path('api/courses/<int:course_id>/delete/', views.api_course_delete, name='api_course_delete'),

    # ==================== API - RECONOCIMIENTOS ====================
    path('api/awards/', views.api_awards, name='api_awards'),
    path('api/awards/create/', views.api_award_create, name='api_award_create'),
    path('api/awards/<int:award_id>/update/', views.api_award_update, name='api_award_update'),
    path('api/awards/<int:award_id>/delete/', views.api_award_delete, name='api_award_delete'),

    # ==================== API - PROYECTOS ====================
    path('api/projects/', views.api_projects, name='api_projects'),
    path('api/projects/create/', views.api_project_create, name='api_project_create'),
    path('api/projects/<int:project_id>/delete/', views.api_project_delete, name='api_project_delete'),

    # ==================== API - SERVICIOS ====================
    path('api/services/', views.api_services, name='api_services'),
]