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
        return self.items
    
    def getDesencolar(self):
        return self.desencolar

    def getEsta_vacia(self):
        return self.esta_vacia
    
    def getTamaño(self):
        return self.tamaño
    
    def getMostrar(self):
        return self.mostrar
    
    
    
    def setItem(self):
        return self.items
    
    def setDesencolar(self):
        return self.desencolar
    
    def setEsta_vacia(self):
        return self.esta_vacia
    
    def setTamaño(self):
        return self.tamaño
    
    def setMostrar(self):
        return self.mostrar
    
    
    
    
    
