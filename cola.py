# cola.py
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
