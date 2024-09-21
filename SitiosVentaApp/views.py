from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import time 
STATIC_VERSION = str(int(time.time()))
version = {'STATIC_VERSION':STATIC_VERSION}
# Create your views here.

def user_login(request):
        return render(request, 'dashboard/ingresar.html')

def mostrar_admin(request):
    return render (request,'../templates/dashboard/index.html')

def mostrar_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("Hola login")
        remember_me = request.POST.get('remember_me', None)  # Capturar la opción de "recordarme"
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Si "recordarme" no está marcado, caduca la sesión al cerrar el navegador
            if remember_me:
                request.session.set_expiry(1209600)  # 2 semanas
            else:
                request.session.set_expiry(0)  # La sesión expira al cerrar el navegador
            
            return redirect('mostrar_admin')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return redirect('mostrar_login')
    return render(request,'../templates/dashboard/ingresar.html')
def mostrar_registrar(request):
    return render(request,'../templates/dashboard/register.html')
def mostrar_olvidopws(request):
    return render(request,'../templates/dashboard/forgot-password.html')

def post_registrar(request):
   if request.method == 'POST':
        nombres =request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        correo =  request.POST.get('correo')
        # Puedes capturar múltiples valores
        password = request.POST.get('password')

        # Procesa los datos como necesites
        print(nombres,apellidos,correo,password)
        return redirect('mostrar_admin')

        # Retorna una respuesta, redirige o renderiza otra página
        #return render(request, 'success.html', {'input_value': input_value})
   return redirect('mostrar_login') 

def mostrar_index(request):
    return render(request, '../templates/newsoftMain/index.html',version)

def mostrar_about(request):
    return render(request, '../templates/newsoftMain/about.html',version)

def mostrar_feature(request):
    return render(request, '../templates/newsoftMain/feature.html',version)

def mostrar_contact(request):
    return render(request, '../templates/newsoftMain/contact.html',version)

def mostrar_portafolio(request):
    return render(request, '../templates/newsoftMain/portafolio.html',version)

def mostrar_template1(request):
    return render(request, '../templates/Template1/index.html')

def mostrar_template2(request):
    return render(request, '../templates/Template2/index.html')

def mostrar_template3(request):
    return render(request, '../templates/Template3/index.html')

def mostrar_carserv_index(request):
    return render (request, '../templates/carserv/index.html')
def mostrar_carserv_about(request):
    return render (request, '../templates/carserv/about.html')
def mostrar_carserv_contact(request):
    return render (request, '../templates/carserv/contact.html')
def mostrar_carserv_service(request):
    return render (request, '../templates/carserv/service.html')




def mostrar_template4(request):
    context = {
        'active_page': 'home'
    }
    return render(request, '../templates/Template4/index.html', context)
def mostrar_template4_about(request):
    context = {
        'active_page': 'about'
    }
    return render(request, '../templates/Template4/about.html', context)
def mostrar_template4_services(request):
    context = {
        'active_page': 'services'
    }
    return render(request, '../templates/Template4/service.html', context)
def mostrar_template4_contact(request):
    context = {
        'active_page': 'contact'
    }
    return render(request, '../templates/Template4/contact.html', context)




def mostrar_template5(request):
    return render(request, '../templates/Template5/index.html')

def mostrar_template6(request):
    return render(request, '../templates/Template6/index.html')

def mostrar_template7(request):
    return render(request, '../templates/Template7/index.html')

def mostrar_template8(request):
    return render(request, '../templates/Template8/index.html')

def mostrar_template9(request):
    return render(request, '../templates/Template9/index.html')

def mostrar_template10(request):
    return render(request, '../templates/Template10/index.html')

def mostrar_template11(request):
    return render(request, '../templates/Template11/index.html')

def mostrar_template12(request):
    return render(request, '../templates/Template12/index.html')

def mostrar_template13(request):
    return render(request, '../templates/Template13/index.html')

def mostrar_template14(request):
    return render(request, '../templates/Template14/index.html')

def mostrar_template15(request):
    return render(request, '../templates/Template15/index.html')

def mostrar_template16(request):
    return render(request, '../templates/Template16/index.html')




