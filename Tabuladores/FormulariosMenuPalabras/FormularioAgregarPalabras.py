from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QLineEdit, QPushButton, QCompleter, QTextEdit

from PalabrasDB import PalabrasDB


class FormularioAgregarPalabras(QWidget):
    def __init__(self):
        super().__init__()

        # Agregamos algunas configuraciones a la Ventana
        self.setWindowTitle("Add Word")
        self.setFixedSize(450, 250)
        self.setContentsMargins(10, 10, 10, 10)
        self.setWindowIcon(QIcon(QPixmap("Imagenes/book.png")))

        # Creamos un Layout Principal
        layoutPrincipal = QGridLayout()

        self.layoutFunciones = QVBoxLayout()
        layoutPrincipal.addLayout(self.layoutFunciones, 0, 2, 3, 1)

        layoutPrincipal.addWidget(QLabel("English Word"), 0, 0)
        layoutPrincipal.addWidget(QLabel("Spanish Translation"), 1, 0)
        layoutPrincipal.addWidget(QLabel("Word Description"), 2, 0)

        self.txtPalabraIngles = QLineEdit()
        self.txtPalabraIngles.textChanged.connect(self.llenarInformacionPalabraIngles)
        self.txtPalabraIngles.setFixedHeight(30)
        layoutPrincipal.addWidget(self.txtPalabraIngles, 0, 1)

        self.txtPalabraEspanol = QLineEdit()
        self.txtPalabraEspanol.setFixedHeight(30)
        self.txtPalabraEspanol.textChanged.connect(self.llenarInformacionPalabraEspanol)
        layoutPrincipal.addWidget(self.txtPalabraEspanol, 1, 1)

        self.txtDescripcionPalabra = QTextEdit()
        self.setMinimumSize(100, 120)
        layoutPrincipal.addWidget(self.txtDescripcionPalabra, 2, 1)

        self.btnGuardar = QPushButton("Add")
        self.btnGuardar.setIcon(QIcon(QPixmap("Imagenes/Disk/disk--plus.png")))
        self.btnGuardar.setFixedSize(80, 35)
        self.layoutFunciones.addWidget(self.btnGuardar)

        self.btnNuevo = QPushButton("New")
        self.btnNuevo.setIcon(QIcon(QPixmap("Imagenes/Blueprint/blueprint.png")))
        self.btnNuevo.clicked.connect(self.limpiarCajasFormularioAgregarPalabras)
        self.btnNuevo.setFixedSize(80, 35)
        self.layoutFunciones.addWidget(self.btnNuevo)

        palabrasEspanol = PalabrasDB.seleccionar_una_columna("p_espanol")
        palabrasIngles = PalabrasDB.seleccionar_una_columna("p_ingles")

        completerPalabrasEspanol = QCompleter(palabrasEspanol)
        completerPalabrasEspanol.setCaseSensitivity(Qt.CaseInsensitive)
        completerPalabrasEspanol.setFilterMode(Qt.MatchContains)

        completerPalabrasIngles = QCompleter(palabrasIngles)
        completerPalabrasIngles.setCaseSensitivity(Qt.CaseInsensitive)
        completerPalabrasIngles.setFilterMode(Qt.MatchContains)

        self.txtPalabraEspanol.setCompleter(completerPalabrasEspanol)
        self.txtPalabraIngles.setCompleter(completerPalabrasIngles)

        btnSalir = QPushButton("Exit")
        btnSalir.setIcon(QIcon(QPixmap("Imagenes/cross-circle.png")))
        btnSalir.clicked.connect(lambda: self.close())
        btnSalir.setFixedSize(80, 35)
        self.layoutFunciones.addWidget(btnSalir)

        self.setLayout(layoutPrincipal)

    def llenarInformacionPalabraIngles(self, palabraIngles):
        try:
            palabra = PalabrasDB.seleccionarPalabraIngles(palabraIngles)
            self.txtPalabraEspanol.setText(palabra[2])
        except TypeError as e:
            pass

    def llenarInformacionPalabraEspanol(self, palabraEspanol):
        try:
            palabra = PalabrasDB.seleccionarPalabraEspanol(palabraEspanol)
            self.txtPalabraIngles.setText(palabra[1])
            self.txtDescripcionPalabra.setText(palabra[3])
            self.setWindowTitle("")
            self.setWindowTitle(f"Add Word | Id: {palabra[0]}")
        except TypeError as e:
            pass

    def limpiarCajasFormularioAgregarPalabras(self):
        self.txtPalabraIngles.setText("")
        self.txtPalabraEspanol.setText("")
        self.txtDescripcionPalabra.setText("")
