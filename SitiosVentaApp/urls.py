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
    path('contacts/', views.mostrar_contacto,name = 'mostrar_contacto'),
    path('portafolio/', views.mostrar_portafolio ,name = 'mostrar_portafolio'),
    path('', views.mostrar_index ,name = 'mostrar_index'),
    path('template1/', views.mostrar_template1 ,name = 'mostrar_template1'),
    path('template2/', views.mostrar_template2 ,name = 'mostrar_template2'),
    path('template3/', views.mostrar_template3 ,name = 'mostrar_template3'),
    path('template4/', views.mostrar_template4 ,name = 'mostrar_template4'),
    path('template5/', views.mostrar_template5 ,name = 'mostrar_template5'),
    path('template6/', views.mostrar_template6 ,name = 'mostrar_template6'),
    path('template7/', views.mostrar_template7 ,name = 'mostrar_template7'),
    path('template8/', views.mostrar_template8 ,name = 'mostrar_template8'),
    path('template9/', views.mostrar_template9 ,name = 'mostrar_template9'),
    path('template10/', views.mostrar_template10 ,name = 'mostrar_template10'),
    path('template11/', views.mostrar_template11 ,name = 'mostrar_template11'),
    path('template12/', views.mostrar_template12 ,name = 'mostrar_template12'),
    path('template13/', views.mostrar_template13 ,name = 'mostrar_template13'),
    path('template14/', views.mostrar_template14 ,name = 'mostrar_template14'),
    path('template15/', views.mostrar_template15 ,name = 'mostrar_template15'),
]
