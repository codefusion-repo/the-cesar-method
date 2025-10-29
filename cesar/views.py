from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
import random

    
def metodocesar(texto, desplazamiento=None) -> str:
    if desplazamiento is None:
        desplazamiento = random.randint(1, 27)  
    
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            resultado += char
    return resultado, desplazamiento


def metodoCesar(texto) -> str:
    if len(texto) == 0:
        return "Debe ingresar un texto"
    

    
def index(request):

    if request.method == 'GET':
        print("Ingreso de solicitud GET")

    if request.method == 'POST':
        data = request.POST
        texto = data.get('texto', '')
        text_cesarizado, d = metodocesar(texto)
        print("texto recibido: " + texto)
        print("text cesarizado: " + text_cesarizado)
        print("se desplazo: " + str(d))

    return render(request, 'index.html')