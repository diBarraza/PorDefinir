from django.shortcuts import render

# Create your views here.
def mostrar_index(request):
    return render(request, '../templates/main/index.html')
def mostrar_blog(request):
    return render(request, '../templates/main/blog.html')
def mostrar_contacts(request):
    return render(request, '../templates/main/contacts.html')
def mostrar_portafolio(request):
    return render(request, '../templates/main/portafolio.html')





