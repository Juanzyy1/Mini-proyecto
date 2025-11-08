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
        
        
#------Métodos consultores--------

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getEdad(self):
        return self.__edad
    
    def getTipo_doc(self):
        return self.__tipo_doc
    
    def getDocumento(self):
        return self.__documento
    
#------Métodos modificadores--------------------

    def setNombre(self, nombre):
        return self.__nombre
        
    def setApellido(self, apellido):
        return self.__apellido
        
    def setEdad(self, edad):
        return self.__edad
        
    def setTipo_doc(self, tipo_doc):
        return self.__tipo_doc
        
    def setDocumento(self, documento):
        return self.__documento
        
#--------------------------------------------------

    def __init__(self, nombre=None, apellido=None, edad=None, documento=None):
        self._nombre = nombre if nombre else random.choice(nombres)
        self._apellido = apellido if apellido else random.choice(apellidos)
        self._edad = edad if edad else random.randint(5, 17)


        # Tipo de documento según edad
        self._tipo_doc = "TI" if self._edad < 18 else "CC"

        self._documento = (
            documento if documento 
            else str(random.randint(10_000_000, 999_999_9999))
        )

    # --------- Métodos Consultores ---------
    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def get_edad(self):
        return self._edad

    def get_documento(self):
        return self._documento

    def get_tipo_doc(self):
        return self._tipo_doc

    # --------- Métodos Modificadores  ---------
    def set_nombre(self, nombre):
        if nombre.strip():
            self._nombre = nombre

    def set_apellido(self, apellido):
        if apellido.strip():
            self._apellido = apellido

    def set_edad(self, edad):
        if 5 <= edad <= 17:
            self._edad = edad
            self._tipo_doc = "TI"
        else:
            raise ValueError("Edad fuera de rango (5-17)")

    def set_documento(self, documento):
        if documento.isdigit() and 7 <= len(documento) <= 10:
            self._documento = documento
        else:
            raise ValueError("Documento inválido")

    # --------- Otros métodos funcionales ---------
    def subsidio(self):
        if 5 <= self._edad <= 9:
            return 60000
        elif 10 <= self._edad <= 13:
            return 80000
        return 100000

    #Representaciones visuales
    def info_corta(self):
        return f"{self._nombre} {self._apellido} - {self._edad} años"

    def __str__(self):
        return (
            f"{self._nombre} {self._apellido} | "
            f"Edad: {self._edad} | "
            f"{self._tipo_doc}: {self._documento}"
        )
