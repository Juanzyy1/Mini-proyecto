# main.py
from logica import generar_cola, procesar_subsidios
from ui.app import run_app  # 👈 Importamos la interfaz

def main():
    # Parte en consola (opcional)
    cola = generar_cola()
    print("Cola inicial:")
    print("\n".join(cola.mostrar()))

    total_p, total_d = procesar_subsidios(cola)
    print(f"\nPersonas atendidas: {total_p}")
    print(f"Dinero total entregado: ${total_d:,.0f}")
    print("Cola final:", cola.mostrar())

    # 👇 Ejecutamos la interfaz
run_app()

