import random
from typing import Optional

nombres = ["Juan", "María", "Carlos", "Luisa", "Daniel", "Valentina", "Andrés", "Sofía"]
apellidos = ["García", "López", "Rodríguez", "Martínez", "Morales", "Gómez", "Ruiz"]


class Persona:
    """
    Representa a un niño o adolescente beneficiario del subsidio.

    Atributos:
        nombre (str): Nombre del beneficiario.
        apellido (str): Apellido del beneficiario.
        edad (int): Edad entre 5 y 17 años.
        tipo_doc (str): 'TI' si es menor de 18, si fuera adulto sería 'CC'.
        documento (str): Número de documento entre 7 y 10 dígitos.

    Métodos relevantes:
        subsidio() -> int: Retorna el monto del subsidio según la edad.
        info_corta() -> str: Representación resumida del beneficiario.
    """

    def __init__(
        self,
        nombre: Optional[str] = None,
        apellido: Optional[str] = None,
        edad: Optional[int] = None,
        documento: Optional[str] = None
    ):
        self._nombre = nombre or random.choice(nombres)
        self._apellido = apellido or random.choice(apellidos)
        self._edad = edad if edad is not None else random.randint(5, 17)

        # Tipo de documento basado en la edad
        self._tipo_doc = "TI" if self._edad < 18 else "CC"

        self._documento = (
            documento if documento 
            else str(random.randint(10_000_000, 999_999_9999))
        )

    # ---------(Getters) Consultores---------
    def get_nombre(self) -> str:
        return self._nombre

    def get_apellido(self) -> str:
        return self._apellido

    def get_edad(self) -> int:
        return self._edad

    def get_documento(self) -> str:
        return self._documento

    def get_tipo_doc(self) -> str:
        return self._tipo_doc

    # ---------(Setters) Modificadores---------
    def set_nombre(self, nombre: str) -> None:
        if nombre.strip():
            self._nombre = nombre

    def set_apellido(self, apellido: str) -> None:
        if apellido.strip():
            self._apellido = apellido

    def set_edad(self, edad: int) -> None:
        if 5 <= edad <= 17:
            self._edad = edad
            self._tipo_doc = "TI"
        else:
            raise ValueError("La edad debe estar entre 5 y 17 años.")

    def set_documento(self, documento: str) -> None:
        if documento.isdigit() and 7 <= len(documento) <= 10:
            self._documento = documento
        else:
            raise ValueError("Documento inválido. Debe tener 7 a 10 dígitos.")

    # --------- Lógica del subsidio ---------
    def subsidio(self) -> int:
        """Devuelve el subsidio según la edad."""
        if 5 <= self._edad <= 9:
            return 60_000
        elif 10 <= self._edad <= 13:
            return 80_000
        return 100_000

    # --------- Representaciones ---------
    def info_corta(self) -> str:
        """Forma resumida para mostrar en colas o UI."""
        return f"{self._nombre} {self._apellido} - {self._edad} años"

    def __str__(self) -> str:
        """Forma detallada para guardar o imprimir en historial."""
        return (
            f"{self._nombre} {self._apellido} | "
            f"Edad: {self._edad} | "
            f"{self._tipo_doc}: {self._documento}"
        )
