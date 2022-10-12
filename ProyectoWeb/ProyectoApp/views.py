from django.shortcuts import render
from django.http import HttpResponse
from ProyectoApp.models import Tienda, Juego, Cliente

# Create your views here.


def mostrar_tienda(request):
    tienda_1=Tienda(nombre="ZonaGames", direccion="Sanchez 1900", email="ZonaGames@coder.com")
    tienda_2=Tienda(nombre="PlayMania", direccion="Av Rivadavia 16500", email="PlayMania@coder.com")
    tienda_3=Tienda(nombre="TodoJuegos", direccion="Av Juan B Justo 11000", email="TodoJuegos@coder.com")
    
def mostrar_juego(request):
    juego_1=Juego(nombre="FIFA 23", codigo="2323", precio="17000", fecha_de_entrega="26 de noviembre del 2022")
    juego_2=Juego(nombre="Elden Ring", codigo="1712", precio="20000", fecha_de_entrega="25 de octubre del 2022")
    juego_3=Juego(nombre="Dead Island 2", codigo="26266", precio="25000", fecha_de_entrega="24 de diciembre del 2022")
    

def mostrar_cliente(request):
    cliente_1=Cliente(nombre="Sebastian", apellido="Altamirano", email="seba@coder.com", dni="32.591.254", entregado="26 de noviembre del 2022")
    cliente_2=Cliente(nombre="Carlos", apellido="Garcia", email="carlos@coder.com", dni="45.591.585", entregado="25 de octubre del 2022")  
    cliente_3=Cliente(nombre="Marcos", apellido="Santillan", email="marcos@coder.com", dni="48.555.278", entregado="24 de diciembre del 2022")
    
