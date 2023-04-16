from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QFont, QTextCharFormat, QIcon, QPixmap
from PySide6.QtWidgets import QFrame, QTableWidget, QVBoxLayout, QHeaderView, QHBoxLayout, QPushButton, \
    QTableWidgetItem, QWidget, QLineEdit, QGridLayout, QLabel, QMessageBox, QErrorMessage, QTextEdit

from PalabrasDB import PalabrasDB


class TabPalabras(QFrame):
    def __init__(self):
        super().__init__()

        # Creamos un layout principal
        layout_principal = QVBoxLayout()

        # Creamos el menu de opciones y agregamos al layout_principal
        self.layout_menu = MenuOpcionesPalabras()
        layout_principal.addLayout(self.layout_menu)
        self.layout_menu.ventana_agregar.btnGuardar.clicked.connect(self.agregar_palabra)

        # Llamamos a la clase para crear y agregar la tabla a el layout_principal
        self.tabla_palabras = TablaPalabras()
        layout_principal.addWidget(self.tabla_palabras)

        self.setLayout(layout_principal)

    def agregar_palabra(self):
        try:
            palabra_espanol = self.layout_menu.ventana_agregar.p_espanol.text().strip()
            palabra_ingles = self.layout_menu.ventana_agregar.p_ingles.text().strip()
            descripcion = self.layout_menu.ventana_agregar.descripcion_p.toPlainText().strip()

            if palabra_espanol.isalpha() and palabra_ingles.isalpha():
                datos = [
                    palabra_ingles,
                    palabra_espanol,
                    descripcion
                ]

                PalabrasDB().insertar_palabra(palabra_ingles=datos[0],
                                              palabra_espanol=datos[1],
                                              descripcion=datos[2])

            else:
                QMessageBox.critical(self, "Error", "Could not insert data, please restart or try again",
                                     QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Close)
        except Exception as e:
            pass
        finally:
            self.tabla_palabras.setRowCount(0)
            self.tabla_palabras.actualizar_tabla()


class MenuOpcionesPalabras(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.ventana_agregar = VentanaAgregarPalabra()
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)

        btnAgregar = QPushButton(text="Add Word", icon=QIcon(QPixmap("Imagenes/Blueprint/blueprint--plus.png")))
        btnAgregar.setFixedSize(120, 40)
        btnAgregar.pressed.connect(self.abrir_ventana_agregar)
        self.addWidget(btnAgregar)

        btnEliminar = QPushButton(text="Delete Word", icon=QIcon(QPixmap("Imagenes/Blueprint/blueprint--minus.png")))
        btnEliminar.setFixedSize(120, 40)
        self.addWidget(btnEliminar)

        btnEditar = QPushButton(text="Edit Word", icon=QIcon(QPixmap("Imagenes/Blueprint/blueprint--pencil.png")))
        btnEditar.setFixedSize(120, 40)
        self.addWidget(btnEditar)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setFrameShadow(QFrame.Shadow.Plain)
        separator.setFixedSize(5, 40)
        self.addWidget(separator)

        btnBuscar = QPushButton(text="Search Word", icon=QIcon(QPixmap("Imagenes/blue-document-search-result.png")))
        btnBuscar.setFixedSize(120, 40)
        btnBuscar.clicked.connect(self.buscar)
        self.addWidget(btnBuscar)

    def buscar(self):
        pass

    def abrir_ventana_agregar(self):
        if self.ventana_agregar.isVisible():
            self.ventana_agregar.show()
        else:
            self.ventana_agregar.show()


class VentanaAgregarPalabra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Word")
        self.setFixedSize(400, 180)
        self.setContentsMargins(10, 10, 10, 10)
        self.setWindowIcon(QIcon(QPixmap("Imagenes/book.png")))

        layout_principal = QGridLayout()

        layout_botones = QVBoxLayout()
        layout_principal.addLayout(layout_botones, 0, 2, 3, 1)

        layout_principal.addWidget(QLabel("English Word"), 0, 0)
        layout_principal.addWidget(QLabel("Spanish Translation"), 1, 0)
        layout_principal.addWidget(QLabel("Word Description"), 2, 0)

        self.p_ingles = QLineEdit()
        layout_principal.addWidget(self.p_ingles, 0, 1)
        self.p_ingles.setFixedHeight(30)

        self.p_espanol = QLineEdit()
        self.p_espanol.setFixedHeight(30)
        layout_principal.addWidget(self.p_espanol, 1, 1)

        self.descripcion_p = QTextEdit()
        self.setMinimumSize(100, 120)
        layout_principal.addWidget(self.descripcion_p, 2, 1)

        self.btnGuardar = QPushButton("Save")
        self.btnGuardar.setIcon(QIcon(QPixmap("Imagenes/disk.png")))
        self.btnGuardar.setFixedSize(80, 35)
        layout_botones.addWidget(self.btnGuardar)

        btnNuevo = QPushButton("New")
        btnNuevo.setIcon(QIcon(QPixmap("Imagenes/Blueprint/blueprint.png")))
        btnNuevo.clicked.connect(self.limpiar_cajas)
        btnNuevo.setFixedSize(80, 35)
        layout_botones.addWidget(btnNuevo)

        btnSalir = QPushButton("Exit")
        btnSalir.setIcon(QIcon(QPixmap("Imagenes/cross-circle.png")))
        btnSalir.clicked.connect(lambda: self.close())
        btnSalir.setFixedSize(80, 35)
        layout_botones.addWidget(btnSalir)

        self.setLayout(layout_principal)

    def limpiar_cajas(self):
        self.p_ingles.setText("")
        self.p_espanol.setText("")
        self.descripcion_p.setText("")


class TablaPalabras(QTableWidget):
    def __init__(self):
        super().__init__()

        cabezeras = ["ID", "English Word", "Spanish Translation", "Description"]
        self.setColumnCount(len(cabezeras))
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Darle nombres a las cabeceras de la tabla
        self.setHorizontalHeaderLabels(cabezeras)

        self.actualizar_tabla()

    def actualizar_tabla(self):
        datos = PalabrasDB().seleccionar_todas_las_palabras()

        format = QTextCharFormat()
        format.setFontUnderline(True)

        for fila, (id_palabra, palabra_ingles, palabra_espanol, descripcion) in enumerate(datos):
            self.insertRow(fila)
            self.setItem(fila, 0, QTableWidgetItem(str(id_palabra)))
            self.item(fila, 0).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 0).setForeground(QBrush(QColor("blue")))
            self.item(fila, 0).setFont(QFont("Arial", 10, QFont.Bold))
            self.item(fila, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 1, QTableWidgetItem(palabra_ingles))
            self.item(fila, 1).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 2, QTableWidgetItem(palabra_espanol))
            self.item(fila, 2).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 3, QTableWidgetItem(descripcion))
            self.item(fila, 3).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
