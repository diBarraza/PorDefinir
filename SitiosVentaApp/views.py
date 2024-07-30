from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request, '../templates/main/index.html', {'current_page': 'home'})

def mostrar_blog(request):
    return render(request, '../templates/main/blog.html', {'current_page': 'blog'})

def mostrar_portafolio(request):
    return render(request, '../templates/main/portafolio.html', {'current_page': 'portfolio'})

def mostrar_contacto(request):
    return render(request, '../templates/main/contacts.html', {'current_page': 'contacto'})

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
    return render(request, '../templates/Template7/public_html/index.html')

def mostrar_template8(request):
    return render(request, '../templates/Template8/index.html')

def mostrar_template9(request):
    return render(request, '../templates/Template9/index.html')

def mostrar_template10(request):
    return render(request, '../templates/Template10/mediumish-html/index.html')

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




