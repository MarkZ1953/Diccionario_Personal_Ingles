from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QFont, QTextCharFormat, QIcon, QPixmap
from PySide6.QtWidgets import QFrame, QTableWidget, QVBoxLayout, QHeaderView, QHBoxLayout, QPushButton, \
    QTableWidgetItem, QWidget, QLineEdit, QGridLayout, QLabel, QMessageBox, QErrorMessage, QTextEdit, QCompleter

from PalabrasDB import PalabrasDB
from Tabuladores.FormulariosMenuPalabras.FormularioAgregarPalabras import FormularioAgregarPalabras
from Tabuladores.FormulariosMenuPalabras.FormularioBuscarPalabras import FormularioBuscarPalabras
from Tabuladores.FormulariosMenuPalabras.FormularioEditarPalabras import VentanaEditarPalabras
from Tabuladores.FormulariosMenuPalabras.FormularioEliminarPalabras import VentanaEliminarPalabras


class TabPalabras(QFrame):
    def __init__(self):
        super().__init__()

        # Creamos un layout principal
        layout_principal = QVBoxLayout()

        # Creamos el menu de opciones y agregamos al layout_principal
        self.layout_menu = MenuOpcionesPalabras()
        layout_principal.addLayout(self.layout_menu)
        self.layout_menu.ventana_agregar.btnGuardar.clicked.connect(self.agregar_palabra)

        self.layout_menu.ventana_editar.btnGuardar.clicked.connect(self.editar_palabra)

        self.layout_menu.ventana_eliminar.btnGuardar.clicked.connect(self.eliminar_palabra)

        # Llamamos a la clase para crear y agregar la tabla a el layout_principal
        self.tabla_palabras = TablaPalabras()
        layout_principal.addWidget(self.tabla_palabras)

        self.setLayout(layout_principal)

    def agregar_palabra(self):
        try:
            palabra_espanol = self.layout_menu.ventana_agregar.txtPalabraEspanol.text().strip()
            palabra_ingles = self.layout_menu.ventana_agregar.txtPalabraIngles.text().strip()
            descripcion = self.layout_menu.ventana_agregar.txtDescripcionPalabra.toPlainText().strip()

            if palabra_espanol.isalpha() and palabra_ingles.isalpha():
                datos = [
                    palabra_ingles,
                    palabra_espanol,
                    descripcion
                ]

                PalabrasDB().agregarPalabra(palabra_ingles=datos[0], palabra_espanol=datos[1], descripcion=datos[2])

            else:
                QMessageBox.critical(self, "Error", "Could not insert data, please restart or try again",
                                     QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Close)
        except Exception as e:
            pass
        finally:
            self.tabla_palabras.setRowCount(0)
            self.tabla_palabras.actualizar_tabla()

    def editar_palabra(self):
        try:
            id_palabra = self.layout_menu.ventana_editar.id_word.text()
            palabra_espanol = self.layout_menu.ventana_editar.p_espanol.text().strip()
            palabra_ingles = self.layout_menu.ventana_editar.p_ingles.text().strip()
            descripcion = self.layout_menu.ventana_editar.descripcion_p.toPlainText().strip()

            # Orden: (Palabra espanol, palabra ingles, descripcion palabra, id_palabra)
            PalabrasDB.actualizarPalabra(palabra_espanol=palabra_espanol, palabra_ingles=palabra_ingles,
                                         descripcion_palabra=descripcion, id_palabra=id_palabra)
        except Exception as e:
            pass
        finally:
            self.tabla_palabras.setRowCount(0)
            self.tabla_palabras.actualizar_tabla()
            self.layout_menu.ventana_editar.actualizar_completer()

    def eliminar_palabra(self):
        try:
            id_palabra = self.layout_menu.ventana_eliminar.id_word.text()
            PalabrasDB.eliminarPalabra(id_palabra=id_palabra)
        except Exception as e:
            pass
        finally:
            self.tabla_palabras.setRowCount(0)
            self.tabla_palabras.actualizar_tabla()
            self.layout_menu.ventana_eliminar.actualizar_completer()


class MenuOpcionesPalabras(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.ventana_agregar = FormularioAgregarPalabras()
        self.ventana_eliminar = VentanaEliminarPalabras()
        self.ventana_editar = VentanaEditarPalabras()
        self.ventana_buscar = FormularioBuscarPalabras()

        self.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.btnAgregar = QPushButton(text="Add Word", icon=QIcon(QPixmap("Imagenes/Blueprint/blueprint--plus.png")))
        self.btnAgregar.setFixedSize(120, 40)
        self.btnAgregar.pressed.connect(self.abrir_ventana_agregar)
        self.addWidget(self.btnAgregar)

        self.btnEliminar = QPushButton(text="Delete Word", icon=QIcon(QPixmap("Imagenes/Blueprint/blueprint--minus.png")))
        self.btnEliminar.setFixedSize(120, 40)
        self.btnEliminar.pressed.connect(self.abrir_ventana_eliminar)
        self.addWidget(self.btnEliminar)

        self.btnEditar = QPushButton(text="Edit Word", icon=QIcon(QPixmap("Imagenes/Blueprint/blueprint--pencil.png")))
        self.btnEditar.pressed.connect(self.abrir_ventana_editar)
        self.btnEditar.setFixedSize(120, 40)
        self.addWidget(self.btnEditar)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setFrameShadow(QFrame.Shadow.Plain)
        separator.setFixedSize(5, 40)
        self.addWidget(separator)

        btnBuscar = QPushButton(text="Search Word", icon=QIcon(QPixmap("Imagenes/blue-document-search-result.png")))
        btnBuscar.setFixedSize(120, 40)
        btnBuscar.clicked.connect(self.abrir_ventana_buscar)
        self.addWidget(btnBuscar)

    def abrir_ventana_editar(self):
        if not self.ventana_editar.isVisible():
            self.ventana_editar.show()

    def abrir_ventana_eliminar(self):
        if not self.ventana_eliminar.isVisible():
            self.ventana_eliminar.show()

    def abrir_ventana_buscar(self):
        if not self.ventana_buscar.isVisible():
            self.ventana_buscar.show()

    def abrir_ventana_agregar(self):
        if not self.ventana_agregar.isVisible():
            self.ventana_agregar.show()
        else:
            self.ventana_agregar.show()


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
        datos = PalabrasDB().seleccionarTodasLasPalabras()

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
