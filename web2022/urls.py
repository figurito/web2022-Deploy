
from django.contrib.auth import views
from django.contrib import admin
from django.urls import path, include
from core.views import frontpage, tienda, SignUpView
from productos.views import producto
from django.views.generic.base import TemplateView

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('signup1/', SignUpView.as_view(), name='signup1'),
    path('tienda/', tienda, name='tienda'),
    path('principal/', frontpage, name='principal'),
    path('producto/', producto, name='producto'),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='core/frontpage.html'), name='frontpage'),

]
