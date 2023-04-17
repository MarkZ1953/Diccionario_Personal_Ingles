from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QLineEdit, QPushButton, QCompleter, QTextEdit

from PalabrasDB import PalabrasDB


class VentanaAgregarPalabras(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Word")
        self.setFixedSize(400, 200)
        self.setContentsMargins(10, 10, 10, 10)
        self.setWindowIcon(QIcon(QPixmap("Imagenes/book.png")))

        layout_principal = QGridLayout()

        self.layout_botones = QVBoxLayout()
        layout_principal.addLayout(self.layout_botones, 0, 2, 3, 1)

        layout_principal.addWidget(QLabel("English Word"), 0, 0)
        layout_principal.addWidget(QLabel("Spanish Translation"), 1, 0)
        layout_principal.addWidget(QLabel("Word Description"), 2, 0)

        self.p_ingles = QLineEdit()
        layout_principal.addWidget(self.p_ingles, 0, 1)
        self.p_ingles.textChanged.connect(self.verificar_y_cambiar_textos_p_ingles)
        self.p_ingles.setFixedHeight(30)

        self.p_espanol = QLineEdit()
        self.p_espanol.setFixedHeight(30)
        self.p_espanol.textChanged.connect(self.verificar_y_cambiar_textos_p_espanol)
        layout_principal.addWidget(self.p_espanol, 1, 1)

        self.descripcion_p = QTextEdit()
        self.setMinimumSize(100, 120)
        layout_principal.addWidget(self.descripcion_p, 2, 1)

        self.btnGuardar = QPushButton("Save")
        self.btnGuardar.setIcon(QIcon(QPixmap("Imagenes/Disk/disk--plus.png")))
        self.btnGuardar.setFixedSize(80, 35)
        self.layout_botones.addWidget(self.btnGuardar)

        self.btnNuevo = QPushButton("New")
        self.btnNuevo.setIcon(QIcon(QPixmap("Imagenes/Blueprint/blueprint.png")))
        self.btnNuevo.clicked.connect(self.limpiar_cajas)
        self.btnNuevo.setFixedSize(80, 35)
        self.layout_botones.addWidget(self.btnNuevo)

        palabras_espanol = PalabrasDB.seleccionar_una_columna("p_espanol")
        palabras_ingles = PalabrasDB.seleccionar_una_columna("p_ingles")

        resultados_espanol = QCompleter(palabras_espanol)
        resultados_espanol.setCaseSensitivity(Qt.CaseInsensitive)
        resultados_espanol.setFilterMode(Qt.MatchContains)

        resultados_ingles = QCompleter(palabras_ingles)
        resultados_ingles.setCaseSensitivity(Qt.CaseInsensitive)
        resultados_ingles.setFilterMode(Qt.MatchContains)

        self.p_espanol.setCompleter(resultados_espanol)
        self.p_ingles.setCompleter(resultados_ingles)

        btnSalir = QPushButton("Exit")
        btnSalir.setIcon(QIcon(QPixmap("Imagenes/cross-circle.png")))
        btnSalir.clicked.connect(lambda: self.close())
        btnSalir.setFixedSize(80, 35)
        self.layout_botones.addWidget(btnSalir)

        self.setLayout(layout_principal)

    def verificar_y_cambiar_textos_p_ingles(self):
        try:
            palabra = PalabrasDB.seleccionar_registro_p_ingles(self.p_ingles.text())
            self.p_espanol.setText(palabra[2])
        except TypeError as e:
            pass

    def verificar_y_cambiar_textos_p_espanol(self):
        try:
            palabra = PalabrasDB.seleccionar_registro_p_espanol(self.p_espanol.text())
            self.p_ingles.setText(palabra[1])
            self.descripcion_p.setText(palabra[3])
            self.setWindowTitle("")
            self.setWindowTitle(f"Add Word | Id: {palabra[0]}")
        except TypeError as e:
            pass

    def limpiar_cajas(self):
        self.p_ingles.setText("")
        self.p_espanol.setText("")
        self.descripcion_p.setText("")
