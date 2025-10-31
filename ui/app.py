from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLabel, QListWidget, QMessageBox
)
from logica import generar_cola, procesar_subsidios

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Familias en Acción - Control de Subsidios")
        self.setMinimumSize(500, 450)

        self.cola = generar_cola()

        layout = QVBoxLayout()

        self.labelTitulo = QLabel("Cola Inicial de Beneficiarios")
        layout.addWidget(self.labelTitulo)

        self.listaCola = QListWidget()
        self.listaCola.addItems(self.cola.mostrar())
        layout.addWidget(self.listaCola)

        self.btnProcesar = QPushButton("Procesar Subsidios")
        self.btnProcesar.clicked.connect(self.procesar_subsidios)
        layout.addWidget(self.btnProcesar)

        self.resPersonas = QLabel("Personas atendidas: 0")
        self.resDinero = QLabel("Dinero entregado: 0")
        layout.addWidget(self.resPersonas)
        layout.addWidget(self.resDinero)

        self.setLayout(layout)

    def procesar_subsidios(self):
        total_personas, total_dinero = procesar_subsidios(self.cola)

        self.resPersonas.setText(f"Personas atendidas: {total_personas}")
        self.resDinero.setText(f"Dinero entregado: ${total_dinero:,}")

        self.listaCola.clear()
        self.listaCola.addItems(self.cola.mostrar())

        QMessageBox.information(self, "Proceso Finalizado", "Subsidios entregados correctamente ✅")


def run_app():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
