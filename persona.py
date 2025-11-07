import random

nombres = ["Juan", "María", "Carlos", "Luisa", "Daniel", "Valentina", "Andrés", "Sofía"]
apellidos = ["García", "López", "Rodríguez", "Martínez", "Morales", "Gómez", "Ruiz"]

class Persona:
    def __init__(self):
        self.nombre = random.choice(nombres)
        self.apellido = random.choice(apellidos)
        self.edad = random.randint(5, 17)
        
        # Documento tipo Tarjeta de Identidad (7 a 10 dígitos)
        self.tipo_doc = "C.C"
        self.documento = str(random.randint(10_000_000, 999_999_9999))

    def subsidio(self):
        if 5 <= self.edad <= 9:
            return 60000
        elif 10 <= self.edad <= 13:
            return 80000
        return 100000

    def info_corta(self):
        return f"{self.nombre} {self.apellido} - {self.edad} años"

    def __str__(self):
        return f"{self.nombre} {self.apellido} | Edad: {self.edad} | {self.tipo_doc}: {self.documento}"
