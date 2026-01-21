from django.http import HttpResponse

def home(request):
    return HttpResponse("La vista funciona correctamente ✅")
