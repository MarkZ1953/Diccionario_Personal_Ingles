from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QLineEdit, QPushButton, QCompleter, QTextEdit, \
    QComboBox

from FrasesDB import FrasesDB


class VentanaAgregarFrases(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Phrase")
        self.setFixedSize(500, 250)
        self.setContentsMargins(10, 10, 10, 10)
        self.setWindowIcon(QIcon(QPixmap("Imagenes/book.png")))

        layout_principal = QGridLayout()

        self.layout_botones = QVBoxLayout()
        layout_principal.addLayout(self.layout_botones, 0, 2, 4, 1)

        layout_principal.addWidget(QLabel("English Phrase"), 0, 0)
        layout_principal.addWidget(QLabel("Spanish Translation"), 1, 0)
        layout_principal.addWidget(QLabel("Phrase Description"), 2, 0)
        layout_principal.addWidget(QLabel("Category"), 3, 0)

        self.f_ingles = QLineEdit()
        layout_principal.addWidget(self.f_ingles, 0, 1)
        self.f_ingles.textChanged.connect(self.verificar_y_cambiar_textos_p_ingles)
        self.f_ingles.setFixedHeight(30)

        self.f_espanol = QLineEdit()
        self.f_espanol.setFixedHeight(30)
        self.f_espanol.textChanged.connect(self.verificar_y_cambiar_textos_p_espanol)
        layout_principal.addWidget(self.f_espanol, 1, 1)

        self.descripcion_f = QTextEdit()
        self.setMinimumSize(100, 120)
        layout_principal.addWidget(self.descripcion_f, 2, 1)

        self.categoria_f = QComboBox()
        self.categoria_f.addItems(FrasesDB.seleccionar_categorias_frases())
        self.categoria_f.setFixedHeight(30)
        layout_principal.addWidget(self.categoria_f, 3, 1)

        self.btnGuardar = QPushButton("Save")
        self.btnGuardar.setIcon(QIcon(QPixmap("Imagenes/Disk/disk--plus.png")))
        self.btnGuardar.setFixedSize(80, 35)
        self.layout_botones.addWidget(self.btnGuardar)

        self.btnNuevo = QPushButton("New")
        self.btnNuevo.setIcon(QIcon(QPixmap("Imagenes/Blueprint/blueprint.png")))
        self.btnNuevo.clicked.connect(self.limpiar_cajas)
        self.btnNuevo.setFixedSize(80, 35)
        self.layout_botones.addWidget(self.btnNuevo)

        palabras_espanol = FrasesDB.seleccionar_todas_las_frases_espanol()
        palabras_ingles = FrasesDB.seleccionar_todas_las_frases_ingles()

        resultados_espanol = QCompleter(palabras_espanol)
        resultados_espanol.setCaseSensitivity(Qt.CaseInsensitive)
        resultados_espanol.setFilterMode(Qt.MatchContains)

        resultados_ingles = QCompleter(palabras_ingles)
        resultados_ingles.setCaseSensitivity(Qt.CaseInsensitive)
        resultados_ingles.setFilterMode(Qt.MatchContains)

        self.f_espanol.setCompleter(resultados_espanol)
        self.f_ingles.setCompleter(resultados_ingles)

        btnSalir = QPushButton("Exit")
        btnSalir.setIcon(QIcon(QPixmap("Imagenes/cross-circle.png")))
        btnSalir.clicked.connect(lambda: self.close())
        btnSalir.setFixedSize(80, 35)
        self.layout_botones.addWidget(btnSalir)

        self.setLayout(layout_principal)

    def verificar_y_cambiar_textos_p_ingles(self):
        try:
            pass
            # palabra = PalabrasDB.seleccionar_registro_p_ingles(self.f_ingles.text())
            # self.f_espanol.setText(palabra[2])
        except TypeError as e:
            pass

    def verificar_y_cambiar_textos_p_espanol(self):
        try:
            pass
            # palabra = FrasesDB.seleccionar_todas_las_frases(self.f_espanol.text())
            # self.f_ingles.setText(palabra[1])
            # self.descripcion_f.setText(palabra[3])
        except TypeError as e:
            pass

    def limpiar_cajas(self):
        self.f_ingles.setText("")
        self.f_espanol.setText("")
        self.descripcion_f.setText("")
