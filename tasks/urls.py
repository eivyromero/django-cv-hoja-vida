from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('api/profile/', views.api_profile),
    path('api/profile/update/', views.api_profile_update),

    path('api/experiences/', views.api_experiences),
    path('api/experiences/create/', views.api_experience_create),
    path('api/experiences/<int:exp_id>/update/', views.api_experience_update),
    path('api/experiences/<int:exp_id>/delete/', views.api_experience_delete),
]
