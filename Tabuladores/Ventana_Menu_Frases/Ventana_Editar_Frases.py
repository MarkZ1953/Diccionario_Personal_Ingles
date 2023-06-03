from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QLineEdit, QPushButton, QCompleter, QTextEdit

from PalabrasDB import PalabrasDB


class VentanaEditarFrases(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Edit Phrase")
        self.setFixedSize(400, 250)
        self.setContentsMargins(10, 10, 10, 10)
        self.setWindowIcon(QIcon(QPixmap("Imagenes/book.png")))

        layout_principal = QGridLayout()

        self.layout_botones = QVBoxLayout()
        layout_principal.addLayout(self.layout_botones, 0, 2, 4, 1)

        layout_principal.addWidget(QLabel("Id Phrase"), 0, 0)
        layout_principal.addWidget(QLabel("English Phrase"), 1, 0)
        layout_principal.addWidget(QLabel("Spanish Translation"), 2, 0)
        layout_principal.addWidget(QLabel("Phrase Description"), 3, 0)

        self.id_word = QLineEdit()
        layout_principal.addWidget(self.id_word, 0, 1)
        self.id_word.textChanged.connect(self.verificar_y_cambiar_textos_id)
        self.id_word.setFixedHeight(30)

        self.p_ingles = QLineEdit()
        layout_principal.addWidget(self.p_ingles, 1, 1)
        self.p_ingles.textChanged.connect(self.verificar_y_cambiar_textos_p_ingles)
        self.p_ingles.setFixedHeight(30)

        self.p_espanol = QLineEdit()
        self.p_espanol.setFixedHeight(30)
        self.p_espanol.textChanged.connect(self.verificar_y_cambiar_textos_p_espanol)
        layout_principal.addWidget(self.p_espanol, 2, 1)

        self.descripcion_p = QTextEdit()
        self.setMinimumSize(100, 120)
        layout_principal.addWidget(self.descripcion_p, 3, 1)

        self.btnGuardar = QPushButton("Save")
        self.btnGuardar.setIcon(QIcon(QPixmap("Imagenes/Disk/disk--pencil.png")))
        self.btnGuardar.setFixedSize(80, 35)
        self.layout_botones.addWidget(self.btnGuardar)

        self.btnNuevo = QPushButton("Clean")
        self.btnNuevo.setIcon(QIcon(QPixmap("Imagenes/Blueprint/blueprint.png")))
        self.btnNuevo.clicked.connect(self.limpiar_cajas)
        self.btnNuevo.setFixedSize(80, 35)
        self.layout_botones.addWidget(self.btnNuevo)

        self.actualizar_completer()

        btnSalir = QPushButton("Exit")
        btnSalir.setIcon(QIcon(QPixmap("Imagenes/cross-circle.png")))
        btnSalir.clicked.connect(lambda: self.close())
        btnSalir.setFixedSize(80, 35)
        self.layout_botones.addWidget(btnSalir)

        self.setLayout(layout_principal)

    def verificar_y_cambiar_textos_p_ingles(self):
        try:
            palabra = PalabrasDB.seleccionarPalabraIngles(self.p_ingles.text())
            self.id_word.setText(str(palabra[0]))
            self.p_espanol.setText(palabra[2])
            self.descripcion_p.setText(palabra[3])
        except TypeError as e:
            pass

    def verificar_y_cambiar_textos_p_espanol(self):
        try:
            palabra = PalabrasDB.seleccionarPalabraEspanol(self.p_espanol.text())
            self.id_word.setText(str(palabra[0]))
            self.p_ingles.setText(palabra[1])
            self.descripcion_p.setText(palabra[3])
        except TypeError as e:
            pass

    def verificar_y_cambiar_textos_id(self):
        try:
            palabra = PalabrasDB.seleccionarIdPalabra(self.id_word.text())
            self.p_espanol.setText(palabra[2])
            self.p_ingles.setText(palabra[1])
            self.descripcion_p.setText(palabra[3])
        except Exception as e:
            pass

    def limpiar_cajas(self):
        self.id_word.setText("")
        self.p_ingles.setText("")
        self.p_espanol.setText("")
        self.descripcion_p.setText("")

    def actualizar_completer(self):

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
