from logica import Logica
from ui.app import run_app


def main() -> None:
    """
    Prueba de consola para verificar funcionamiento de la lógica sin interfaz gráfica.

    Pasos:
    1. Se genera una cola simulada con personas.
    2. Se muestra la cola inicial en consola.
    3. Se procesan los subsidios (se atienden todas las personas).
    4. Se muestra el total atendido y el total de dinero entregado.
    """
    logica = Logica()
    cola = logica.generar_cola()

    print("📌 Cola inicial:")
    print("\n".join(cola.mostrar()))

    total_p, total_d = logica.procesar_subsidios()
    print(f"\n✅ Personas atendidas: {total_p}")
    print(f"💰 Dinero total entregado: ${total_d:,.0f}")
    print(f"📌 Cola final: {cola.mostrar()}")



run_app()  # Ejecución de la interfaz gráfica

