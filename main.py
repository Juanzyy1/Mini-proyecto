# main.py
from logica import Logica
from ui.app import run_app  #Importamos la interfaz

def main():
    # Parte en consola (opcional)
    logica = Logica()
    cola = logica.generar_cola()
    print("Cola inicial:")
    print("\n".join(cola.mostrar()))

    total_p, total_d = logica.procesar_subsidios(cola)
    print(f"\nPersonas atendidas: {total_p}")
    print(f"Dinero total entregado: ${total_d:,.0f}")
    print("Cola final:", cola.mostrar())


def guardar_en_txt(self):
    """Guarda el historial actual de beneficiarios atendidos"""
    try:
        with open("beneficiarios.txt", "a", encoding="utf-8") as f:
            f.write(f"\n--- Resumen de sesión ---\n")
            f.write(f"Personas atendidas: {self.atendidos}\n")
            f.write(f"Dinero total entregado: ${self.totalDinero:,}\n")
            f.write(f"--------------------------\n")

        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(self, "✅ Guardado", "El historial fue guardado correctamente en 'beneficiarios.txt'")
    except Exception as e:
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.warning(self, "❌ Error", f"No se pudo guardar el archivo:\n{e}")



#Ejecutamos la interfaz
run_app()

