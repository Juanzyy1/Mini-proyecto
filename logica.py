# logica.py
from persona import Persona
from cola import Cola

def generar_cola(cantidad=50):
    cola = Cola()
    for i in range(1, cantidad + 1):
        cola.encolar(Persona(i))
    return cola

def procesar_subsidios(cola):
    total_personas = 0
    total_dinero = 0

    while not cola.esta_vacia():
        persona = cola.desencolar()
        total_personas += 1
        total_dinero += persona.subsidio()

    return total_personas, total_dinero
