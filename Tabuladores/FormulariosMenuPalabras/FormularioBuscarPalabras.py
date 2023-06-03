from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QCompleter, QTextEdit, \
    QHBoxLayout, QGroupBox, QFormLayout

from PalabrasDB import PalabrasDB


class FormularioBuscarPalabras(QWidget):
    def __init__(self):
        super().__init__()

        # Agregamos algunas configuraciones a la Ventana
        self.setWindowTitle("Search Word")
        self.setFixedSize(450, 250)
        self.setContentsMargins(10, 10, 10, 10)
        self.setWindowIcon(QIcon(QPixmap("Imagenes/book.png")))

        # Creamos un Layout Principal
        layoutPrincipal = QHBoxLayout()

        # Creamos un Frame y un Layout para la Informacion de la Palabra
        layoutInfoPalabra = QFormLayout()
        layoutInfoPalabra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frameInfoPalabra = QGroupBox("Word Information")
        frameInfoPalabra.setLayout(layoutInfoPalabra)
        layoutPrincipal.addWidget(frameInfoPalabra)

        # Creamos un Frame y un Layout para las Funciones
        self.layoutFunciones = QVBoxLayout()
        self.layoutFunciones.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frameFunciones = QGroupBox("Functions")
        frameFunciones.setLayout(self.layoutFunciones)
        layoutPrincipal.addWidget(frameFunciones)

        self.txtIdPalabra = QLineEdit()
        self.txtIdPalabra.textChanged.connect(self.verificar_y_cambiar_textos_id)
        self.txtIdPalabra.setFixedHeight(30)
        layoutInfoPalabra.addRow(QLabel("Id Word"), self.txtIdPalabra)

        self.txtPalabraIngles = QLineEdit()
        self.txtPalabraIngles.textChanged.connect(self.verificar_y_cambiar_textos_p_ingles)
        self.txtPalabraIngles.setFixedHeight(30)
        layoutInfoPalabra.addRow(QLabel("English Word"), self.txtPalabraIngles)

        self.txtPalabraEspanol = QLineEdit()
        self.txtPalabraEspanol.setFixedHeight(30)
        self.txtPalabraEspanol.textChanged.connect(self.verificar_y_cambiar_textos_p_espanol)
        layoutInfoPalabra.addRow(QLabel("Spanish Translation"), self.txtPalabraEspanol)

        self.txtDescripcionPalabra = QTextEdit()
        self.setMinimumSize(100, 120)
        layoutInfoPalabra.addRow(QLabel("Word Description"), self.txtDescripcionPalabra)

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

        self.btnNuevo = QPushButton()
        self.btnNuevo.setToolTip("Clean the boxes")
        self.btnNuevo.setIcon(QIcon(QPixmap("Imagenes/Blueprint/blueprint.png")))
        self.btnNuevo.clicked.connect(self.limpiarCajasFormularioBuscarPalabras)
        self.btnNuevo.setFixedSize(40, 40)
        self.layoutFunciones.addWidget(self.btnNuevo)

        btnSalir = QPushButton()
        btnSalir.setFixedSize(40, 40)
        btnSalir.setToolTip("Close the window")
        btnSalir.setIcon(QIcon(QPixmap("Imagenes/cross-circle.png")))
        btnSalir.clicked.connect(lambda: self.close())
        self.layoutFunciones.addWidget(btnSalir)

        self.setLayout(layoutPrincipal)

    def verificar_y_cambiar_textos_p_ingles(self):
        try:
            palabra = PalabrasDB.seleccionarPalabraIngles(self.txtPalabraIngles.text())
            self.txtIdPalabra.setText(str(palabra[0]))
            self.txtPalabraEspanol.setText(palabra[2])
            self.txtDescripcionPalabra.setText(palabra[3])
        except TypeError as e:
            pass

    def verificar_y_cambiar_textos_p_espanol(self):
        try:
            palabra = PalabrasDB.seleccionarPalabraEspanol(self.txtPalabraEspanol.text())
            self.txtIdPalabra.setText(str(palabra[0]))
            self.txtPalabraIngles.setText(palabra[1])
            self.txtDescripcionPalabra.setText(palabra[3])
        except TypeError as e:
            pass

    def verificar_y_cambiar_textos_id(self):
        try:
            palabra = PalabrasDB.seleccionarIdPalabra(self.txtIdPalabra.text())
            self.txtPalabraEspanol.setText(palabra[2])
            self.txtPalabraIngles.setText(palabra[1])
            self.txtDescripcionPalabra.setText(palabra[3])
        except Exception as e:
            pass

    def limpiarCajasFormularioBuscarPalabras(self):
        self.txtIdPalabra.setText("")
        self.txtPalabraIngles.setText("")
        self.txtPalabraEspanol.setText("")
        self.txtDescripcionPalabra.setText("")
