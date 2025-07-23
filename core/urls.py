"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!xxx")

def pagina1(request):
    return HttpResponse("Pagina 1")

def pagina2(request):
    return HttpResponse("Pagina 2")

def pagina2(request):
    return HttpResponse("Pagina 3")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('1', pagina1),
    path('2', pagina2),
    path('3', pagina3),
]
