# persona.py
import random

class Persona:
    def __init__(self, id):
        self.id = id
        self.edad = random.randint(5, 17)

    def subsidio(self):
        if 5 <= self.edad <= 9:
            return 60000
        elif 10 <= self.edad <= 13:
            return 80000
        else:
            return 100000

    def __str__(self):
        return f"Persona {self.id} | Edad: {self.edad}"
