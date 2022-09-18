from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from productos.models import Producto
from .forms import SignUpForm

def frontpage(request):
    productos= Producto.objects.all()[0:8]
    return render(request, 'core/frontpage.html', {'productos':productos})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def tienda(request):
    productos= Producto.objects.all()
    return render(request, 'core/tienda.html', {'productos':productos})
