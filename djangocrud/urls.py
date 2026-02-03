from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Proyecto funcionando</title>
    </head>
    <body>
        <h1>Proyecto desplegado correctamente en Render</h1>
        <p>Sin base de datos</p>
    </body>
    </html>
    """)

urlpatterns = [
    path('', home),
]
