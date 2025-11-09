from persona import Persona
from cola import Cola
import os
from typing import Tuple

class Logica:
    def __init__(self):
        self.cola = Cola()
        self.total_entregado = 0
        self.archivo = "beneficiarios.txt"
        self.cargar_historial()

    def generar_cola(self, cantidad: int = 50) -> Cola:
    #Llena self.cola con `cantidad` personas (edades aleatorias)."""
        self.cola = Cola()
        for _ in range(cantidad):
            self.cola.encolar(Persona())
        return self.cola

    def procesar_subsidios(self) -> Tuple[int, int]:
        """
        Procesa (desencola) todas las personas de self.cola,
        guarda cada persona en el archivo y devuelve (total_personas, total_dinero).
        """
        total_personas = 0
        total_dinero = 0

        while not self.cola.esta_vacia():
            persona = self.cola.desencolar()
            total_personas += 1

            monto = self._obtener_subsidio_de_persona(persona)
            total_dinero += monto

            # Guardar registro de la persona atendida
            self.guardar_persona(persona, monto)

        self.total_entregado += total_dinero
        return total_personas, total_dinero

    def atender_una_persona(self):
        """
        Atender solo la primera persona en la cola (útil para tu botón 'Atender').
        Devuelve la persona atendida y el monto entregado (o (None, 0) si cola vacía).
        """
        if self.cola.esta_vacia():
            return None, 0

        persona = self.cola.desencolar()
        monto = self._obtener_subsidio_de_persona(persona)
        self.total_entregado += monto
        self.guardar_persona(persona, monto)
        return persona, monto

    def guardar_persona(self, persona, monto: int):
      #Guarda la información de la persona atendida en self.archivo.
        with open(self.archivo, "a", encoding="utf-8") as f:
            # Si tienes nombre/apellidos/documento en la clase Persona, puedes añadirlos aquí.
            nombre = getattr(persona, "get_nombre", lambda: "")()
            apellido = getattr(persona, "get_apellido", lambda: "")()
            documento = getattr(persona, "get_documento", lambda: "")()

            f.write(f"Edad: {getattr(persona, 'edad', '')} | ")
            f.write(f"Nombre: {nombre} {apellido} | ")
            f.write(f"Documento: {documento} | ")
            f.write(f"Subsidio: {monto}\n")

    def cargar_historial(self):
        #Carga el total_entregado sumando los montos que haya en el archivo si existe
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    if "Subsidio:" in linea:
                        try:
                            monto = int(linea.split("Subsidio:")[1].strip())
                            self.total_entregado += monto
                        except Exception:
                            pass

    def _obtener_subsidio_de_persona(self, persona) -> int:
        """
        Devuelve el subsidio de la persona. Soporta:
        - persona.subsidio  (atributo)
        - persona.subsidio() (método)
        - o un método get_subsidio()
        """
        # Priorizar método callable
        attr = getattr(persona, "subsidio", None)
        if callable(attr):
            try:
                return int(attr())
            except Exception:
                pass
        # Si es atributo
        if attr is not None:
            try:
                return int(attr)
            except Exception:
                pass
        # Intentar otros nombres comunes
        method = getattr(persona, "get_subsidio", None)
        if callable(method):
            try:
                return int(method())
            except Exception:
                pass

        # Si no se encuentra, devolver 0
        return 0


# --- Función de compatibilidad
def generar_cola(cantidad: int = 50) -> Cola:
    c = Cola()
    for _ in range(cantidad):
        c.encolar(Persona())
    return c
