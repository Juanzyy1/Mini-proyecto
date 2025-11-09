class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, persona):
        self.items.append(persona)
        

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def tamaño(self):
        return len(self.items)

    def mostrar(self):
        return [str(p) for p in self.items]
    
    
    
#----Métodos consultores--------


    def getItem(self):
        return self.__items
    
    def getDesencolar(self):
        return self.__desencolar

    def getEsta_vacia(self):
        return self.__esta_vacia
    
    def getTamaño(self):
        return self.__tamaño
    
    def getMostrar(self):
        return self.__mostrar
    
    
    
    def setItem(self):
        return self.__items
    
    def setDesencolar(self):
        return self.__desencolar
    
    def setEsta_vacia(self):
        return self.__esta_vacia
    
    def setTamaño(self):
        return self.__tamaño
    
    def setMostrar(self):
        return self.__mostrar
    
    
    
    
    
