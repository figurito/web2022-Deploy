import imp
from django.contrib import admin

from .models import Categoria, Producto

admin.site.register(Categoria)
admin.site.register(Producto)