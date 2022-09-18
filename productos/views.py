from django.shortcuts import render

def producto(request):
    return render(request, 'producto/producto.html')
