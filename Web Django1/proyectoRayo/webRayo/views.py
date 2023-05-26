from django.shortcuts import render
from .views import*
from .models import *
# Create your views here.
def index(request):
    return render(request,"index.html")
def galeria(request):
    return render(request,"galeria.html")
def login(request):
    return render(request,"login.html")
def formularioCliente(request):
    return render(request,"formularioCliente.html")
def Autos(request):
    return render(request,"autos.html")
def AdministracionVehiculo(request):
    return render(request,"AdministracionVehiculo.html")