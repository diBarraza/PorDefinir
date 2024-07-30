"""
"MIME""
URL configuration for ventaSitiosWebBack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
urlpatterns = [
    path('index/',views.mostrar_index,name='mostrar_index'),
    path('blog/', views.mostrar_blog, name='mostrar_blog'),
    path('contacts/', views.mostrar_contacts,name = 'mostrar_contacts'),
    path('portafolio/', views.mostrar_portafolio ,name = 'mostrar_portafolio'),
    path('', views.mostrar_index ,name = 'mostrar_index'),
]
