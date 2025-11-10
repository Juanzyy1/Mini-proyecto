# pip install PyQt6 y pip install qt-material

# Interfaz gráfica del proyecto "Familias en Acción"
# Diseñada con PyQt6 usando estilo visual moderno (qt_material)


from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QMessageBox, QProgressBar, QFrame, QTableWidget, QTableWidgetItem
)
from qt_material import apply_stylesheet  # Para aplicar tema visual moderno
from logica import generar_cola  # Importamos la lógica que genera la cola
from datetime import datetime  # Para registrar fecha y hora en el guardado



class MainWindow(QWidget):
    """
    Ventana principal del sistema de control de subsidios.
    Permite visualizar una cola de beneficiarios, atenderlos y
    registrar el monto total de subsidios entregados.
    """

    def __init__(self):
        super().__init__()

        # ✅ Configuración inicial de ventana
        self.setWindowTitle("Familias en Acción - Control de Subsidios")
        self.setMinimumSize(700, 600)

        # ✅ Generamos la cola de beneficiarios inicial usando lógica del programa
        self.cola = generar_cola()
        self.totalPersonasInicial = self.cola.tamaño()

        # ✅ Layout principal vertical
        layout = QVBoxLayout()

        # -------- Título de la vista --------
        self.labelTitulo = QLabel("👥 Cola de Beneficiarios")
        self.labelTitulo.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(self.labelTitulo)

        # -------- Tabla de beneficiarios --------
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["Nombre Completo", "Edad", "Número de Documento"])

        # Ajustes visuales en columnas
        self.tabla.setColumnWidth(0, 250)
        self.tabla.setColumnWidth(1, 80)
        self.tabla.setColumnWidth(2, 250)
        layout.addWidget(self.tabla)

        # Cargar los datos iniciales de la cola a la tabla
        self.actualizar_tabla()

        # -------- Botón para atender beneficiarios --------
        self.btnAtender = QPushButton("✅ Atender próximo beneficiario")
        self.btnAtender.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #1e88e5;
                color: white;
            }
        """)
        self.btnAtender.clicked.connect(self.atender_persona)
        layout.addWidget(self.btnAtender)

        # -------- Tarjeta de información del beneficiario siendo atendido --------
        self.infoCard = QLabel("✅ Esperando atención...")
        self.infoCard.setFrameStyle(QFrame.Shape.StyledPanel)
        self.infoCard.setStyleSheet("""
            background: #2e2e2e;
            padding: 12px;
            border-radius: 8px;
            font-size: 15px;
        """)
        layout.addWidget(self.infoCard)

        # -------- Barra de progreso del proceso --------
        self.progress = QProgressBar()
        layout.addWidget(self.progress)

        # -------- Etiquetas de estadísticas --------
        self.resPersonas = QLabel("Personas atendidas: 0")
        self.resDinero = QLabel("Dinero total entregado: $0")
        layout.addWidget(self.resPersonas)
        layout.addWidget(self.resDinero)

        # -------- Botón para guardar en archivo --------
        self.btnGuardar = QPushButton("💾 Guardar registro de beneficiarios atendidos")
        self.btnGuardar.setStyleSheet("""
            QPushButton {
                font-size: 15px;
                padding: 8px;
                border-radius: 6px;
                background-color: #4caf50;
                color: white;
            }
            QPushButton:hover {
                background-color: #66bb6a;
            }
        """)
        self.btnGuardar.clicked.connect(self.guardar_en_txt)
        layout.addWidget(self.btnGuardar)

        self.setLayout(layout)

        # ✅ Variables internas del sistema
        self.atendidos = 0
        self.totalDinero = 0



    def actualizar_tabla(self):
        """
        Llena o refresca la tabla con los datos actuales de la cola.
        """
        self.tabla.setRowCount(self.cola.tamaño())
        for i, persona in enumerate(self.cola.items):
            self.tabla.setItem(i, 0, QTableWidgetItem(f"{persona.get_nombre()} {persona.get_apellido()}"))
            self.tabla.setItem(i, 1, QTableWidgetItem(str(persona.get_edad())))
            self.tabla.setItem(i, 2, QTableWidgetItem(persona.get_documento()))



    def atender_persona(self):
        """
        Atiende al siguiente beneficiario en la cola.
        Calcula y acumula el subsidio e actualiza las estadísticas visuales.
        """
        persona = self.cola.desencolar()

        # Si ya no hay personas → mostramos confirmación
        if not persona:
            QMessageBox.information(self, "✅ Finalizado", "Todos los beneficiarios fueron atendidos ✅")
            self.btnAtender.setEnabled(False)
            return

        # Obtener subsidio según edad del beneficiario
        subsidio = persona.subsidio()
        self.atendidos += 1
        self.totalDinero += subsidio

        # Mostrar la información del beneficiario atendido
        self.infoCard.setText(
            f"🧑 Atendiendo beneficiario:\n"
            f"👤 Nombre: {persona.get_nombre()} {persona.get_apellido()}\n"
            f"🎂 Edad: {persona.get_edad()} años\n"
            f"🪪 Documento: {persona.get_documento()}\n"
            f"💵 Subsidio entregado: ${subsidio:,}"
        )

        # Actualizar estadísticas visuales
        self.resPersonas.setText(f"Personas atendidas: {self.atendidos}")
        self.resDinero.setText(f"Dinero total entregado: ${self.totalDinero:,}")
        self.progress.setValue(int((self.atendidos / self.totalPersonasInicial) * 100))

        # Actualizar tabla sin el beneficiario que fue atendido
        self.actualizar_tabla()



    def guardar_en_txt(self):
        """
        📌 Guarda en archivo el registro del proceso realizado
        Incluye fecha, cantidad de beneficiarios atendidos y dinero total entregado.
        """
        try:
            with open("registro_subsidios.txt", "a", encoding="utf-8") as f:
                f.write("\n--- REGISTRO DE ATENCIÓN ---\n")
                f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Personas atendidas: {self.atendidos}\n")
                f.write(f"Dinero total entregado: ${self.totalDinero:,}\n\n")

            QMessageBox.information(self, "✅ Éxito", "Registro guardado en 'registro_subsidios.txt'")
        except Exception as e:
            QMessageBox.warning(self, "❌ Error", f"No se pudo guardar el archivo.\n{e}")



def run_app():
    """
    ✅ Inicia la aplicación y ejecuta la interfaz
    Incluye aplicación del tema oscuro con qt_material.
    """
    app = QApplication([])
    apply_stylesheet(app, theme='dark_blue.xml')  # Tema moderno
    window = MainWindow()
    window.show()
    app.exec()
