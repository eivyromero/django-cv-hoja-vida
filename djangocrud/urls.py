from django.contrib import admin
from django.urls import path, include
from tasks.views import create_admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('tasks.urls')),
    path("create-admin/", create_admin),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
