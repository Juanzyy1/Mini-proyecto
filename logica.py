from persona import Persona
from cola import Cola
import os
from typing import Tuple, Optional


class Logica:
    """
    Gestiona la atención de personas que reciben subsidios mediante una cola (FIFO).
    
    Funcionalidades principales:
    - Generar una cola de personas con edades aleatorias.
    - Atender a todas o una sola persona por vez.
    - Registrar historial en archivo de texto.
    - Calcular monto total entregado incluyendo sesiones pasadas.
    """

    def __init__(self):
        self.cola: Cola = Cola()
        self.total_entregado: int = 0
        self.archivo: str = "beneficiarios.txt"
        self.cargar_historial()

    def generar_cola(self, cantidad: int = 50) -> Cola:
        """
        Llena la cola con `cantidad` de personas nuevas generadas aleatoriamente.
        
        Args:
            cantidad (int): Número de personas a encolar.
        
        Returns:
            Cola: Cola generada con nuevas personas.
        """
        self.cola = Cola()
        for _ in range(cantidad):
            self.cola.encolar(Persona())
        return self.cola

    def procesar_subsidios(self) -> Tuple[int, int]:
        """
        Atiende a todas las personas en la cola hasta dejarla vacía.
        Cada persona atendida se registra en archivo.

        Returns:
            Tuple[int, int]:
                - Total de personas atendidas.
                - Total de dinero entregado en esta ejecución.
        """
        total_personas = 0
        total_dinero = 0

        while not self.cola.esta_vacia():
            persona = self.cola.desencolar()
            total_personas += 1

            monto = self._obtener_subsidio_de_persona(persona)
            total_dinero += monto

            self.guardar_persona(persona, monto)

        self.total_entregado += total_dinero
        return total_personas, total_dinero

    def atender_una_persona(self) -> Tuple[Optional[Persona], int]:
        """
        Atiende únicamente a la primera persona de la cola (si existe).
        
        Returns:
            (Persona, int): Persona atendida y monto entregado.
            Si la cola está vacía → (None, 0)
        """
        if self.cola.esta_vacia():
            return None, 0

        persona = self.cola.desencolar()
        monto = self._obtener_subsidio_de_persona(persona)

        self.total_entregado += monto
        self.guardar_persona(persona, monto)

        return persona, monto

    def guardar_persona(self, persona: Persona, monto: int) -> None:
        """
        Guarda en archivo la información de una persona atendida.

        Formato del archivo:
            Edad | Nombre Apellido | Documento | Subsidio
        """
        with open(self.archivo, "a", encoding="utf-8") as f:
            # Se obtienen datos si existen en la clase Persona
            nombre = getattr(persona, "get_nombre", lambda: "")()
            apellido = getattr(persona, "get_apellido", lambda: "")()
            documento = getattr(persona, "get_documento", lambda: "")()

            f.write(
                f"Edad: {getattr(persona, 'edad', '')} | "
                f"Nombre: {nombre} {apellido} | "
                f"Documento: {documento} | "
                f"Subsidio: {monto}\n"
            )

    def cargar_historial(self) -> None:
        """
        Carga los valores de subsidio ya registrados en el archivo.
        Suma al total_entregado para mantener persistencia entre ejecuciones.
        """
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    if "Subsidio:" in linea:
                        try:
                            monto = int(linea.split("Subsidio:")[1].strip())
                            self.total_entregado += monto
                        except ValueError:
                            pass  # Ignora líneas mal formadas

    def _obtener_subsidio_de_persona(self, persona: Persona) -> int:
        """
        Obtiene el subsidio según la implementación en Persona.

        Compatible con:
        - Atributo: persona.subsidio
        - Método: persona.subsidio()
        - Método alterno: persona.get_subsidio()

        Returns:
            int: Monto del subsidio; 0 si no se puede obtener.
        """
        attr = getattr(persona, "subsidio", None)
        if callable(attr):
            try:
                return int(attr())
            except Exception:
                pass

        if attr is not None:
            try:
                return int(attr)
            except Exception:
                pass

        method = getattr(persona, "get_subsidio", None)
        if callable(method):
            try:
                return int(method())
            except Exception:
                pass

        return 0  # Valor seguro si no hay subsidio definido


# --- Función de compatibilidad ----
def generar_cola(cantidad: int = 50) -> Cola:
    """
    Función auxiliar para crear una cola rápida sin instanciar Logica.
    """
    c = Cola()
    for _ in range(cantidad):
        c.encolar(Persona())
    return c
