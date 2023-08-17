from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home" ),
    path('empresa/', empresa, name="empresa" ),
    path('empresaform/',empresaform, name = "empresaform"),
    path('buscarEmpresa/', buscarEmpresa, name="buscarEmpresa" ),
    path('buscarEmpresa2/', buscarEmpresa2, name="buscarEmpresa2" ),
    path('garantia/', garantia, name="garantia" ),
    path('ingreso_exitoso/',ingreso_exitoso, name='ingreso_exitoso' ),
    path('clientes/',clientes, name='clientes' ),
]