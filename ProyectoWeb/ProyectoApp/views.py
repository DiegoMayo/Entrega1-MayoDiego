from django.shortcuts import render

from ProyectoApp.models import Tienda, Juego, Cliente

# Create your views here.


def mostrar_tienda(request):
    tienda_1=Tienda(nombre="ZonaGames", direccion="Sanchez 1900", email="ZonaGames@coder.com")
    tienda_2=Tienda(nombre="PlayMania", direccion="Av Rivadavia 16500", email="PlayMania@coder.com")
    tienda_3=Tienda(nombre="TodoJuegos", direccion="Av Juan B Justo 11000", email="TodoJuegos@coder.com")
    
    contexto={"tienda_1": tienda_1, "tienda_2": tienda_2, "tienda_3": tienda_3}
    return render(request, "ProyectoApp/Tienda.html", contexto)
    
def mostrar_juego(request):
    juego_1=Juego(nombre="FIFA 23", codigo="2323", precio="17000", fecha_de_entrega="26 de noviembre del 2022")
    juego_2=Juego(nombre="Elden Ring", codigo="1712", precio="20000", fecha_de_entrega="25 de octubre del 2022")
    juego_3=Juego(nombre="Dead Island 2", codigo="26266", precio="25000", fecha_de_entrega="24 de diciembre del 2022")
     
    contexto={"juego_1": juego_1, "juego_2": juego_2, "juego_3": juego_3}
    return render(request, "ProyectoApp/Juego.html", contexto)
    

def mostrar_cliente(request):
    cliente_1=Cliente(nombre="Sebastian", apellido="Altamirano", email="seba@coder.com", dni="32.591.254", entregado="26 de noviembre del 2022")
    cliente_2=Cliente(nombre="Carlos", apellido="Garcia", email="carlos@coder.com", dni="45.591.585", entregado="25 de octubre del 2022")  
    cliente_3=Cliente(nombre="Marcos", apellido="Santillan", email="marcos@coder.com", dni="48.555.278", entregado="24 de diciembre del 2022")
    
    contexto={"cliente_1": cliente_1, "cliente_2": cliente_2, "celinte_3": cliente_3}
    return render(request, "ProyectoApp/Cliente.html", contexto)
    
