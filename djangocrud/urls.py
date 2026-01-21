from django.contrib import admin
from django.urls import path, include
from tasks.views import create_admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path("create-admin/", create_admin),
]
