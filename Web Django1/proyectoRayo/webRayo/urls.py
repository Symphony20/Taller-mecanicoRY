""
from django.contrib import admin
from django.urls import path
from.views import* 

urlpatterns = [
    path('',index,name='INIC'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formularioCliente,name='FORMU'),
    path('login/',login,name='LOG'),
    path('AdministracionVehiculo/',AdministracionVehiculo,name='ADM'),
    
]
