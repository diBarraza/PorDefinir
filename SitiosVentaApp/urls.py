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
         
    path('dashboard/',views.mostrar_admin,name='mostrar_admin'),
    path('ingresar/',views.mostrar_login,name='mostrar_login'),
    path('registrar/',views.mostrar_registrar,name='mostrar_registrar'),
    path('olvidopsw/',views.mostrar_olvidopws,name='mostrar_olvidopws'),
    path('registrar_post/',views.post_registrar,name='registrar_post'),
    path('indice/',views.mostrar_index,name='mostrar_index'),
    path('sobre_nosotros/', views.mostrar_about, name='mostrar_about'),
    path('contacto/', views.mostrar_contact,name = 'mostrar_contact'),
    path('caracteristicas/', views.mostrar_feature ,name = 'mostrar_feature'),
    path('', views.mostrar_index ,name = 'mostrar_index'),
    path('portafolio', views.mostrar_portafolio, name = 'mostrar_portafolio'),
    path('template1/', views.mostrar_template1 ,name = 'mostrar_template1'),
    path('template2/', views.mostrar_template2 ,name = 'mostrar_template2'),
    path('template3/', views.mostrar_template3 ,name = 'mostrar_template3'),
    path('template4/', views.mostrar_template4 ,name = 'mostrar_template4'),
    path('template4/sobre_nosotros', views.mostrar_template4_about ,name = 'mostrar_template4_about'),
    path('template4/servicios', views.mostrar_template4_services ,name = 'mostrar_template4_services'),
    path('template4/contactanos', views.mostrar_template4_contact ,name = 'mostrar_template4_contact'),
    
    path('carserv', views.mostrar_carserv_index ,name = 'mostrar_carserv'),
#    path('carserv/sobre_nosotros', views.mostrar_carserv_about ,name = 'mostrar_carserv_about'),
#    path('carserv/contactanos', views.mostrar_carserv_contact ,name = 'mostrar_carserv_contact'),
#    path('carserv/servicios', views.mostrar_carserv_service ,name = 'mostrar_carserv_service'),
 

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
    path('template16/', views.mostrar_template16 ,name = 'mostrar_template16')
]
