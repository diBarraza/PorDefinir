from django.shortcuts import render
import time 
STATIC_VERSION = str(int(time.time()))
version = {'STATIC_VERSION':STATIC_VERSION}
# Create your views here.
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

def mostrar_template4(request):
    return render(request, '../templates/Template4/index.html')

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




