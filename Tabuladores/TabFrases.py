import re

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QTextCharFormat, QBrush, QColor, QFont
from PySide6.QtWidgets import QFrame, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QMessageBox, QPushButton, QHeaderView, \
    QTableWidget

from FrasesDB import FrasesDB
from Tabuladores.Ventana_Menu_Frases.Ventana_Agregar_Frases import VentanaAgregarFrases
from Tabuladores.Ventana_Menu_Frases.Ventana_Buscar_Frases import VentanaBuscarFrases
from Tabuladores.Ventana_Menu_Frases.Ventana_Editar_Frases import VentanaEditarFrases
from Tabuladores.Ventana_Menu_Frases.Ventana_Eliminar_Frases import VentanaEliminarFrases


class TabFrases(QFrame):
    def __init__(self) -> None:
        super().__init__()
        # Creamos un layout principal
        layout_principal = QVBoxLayout()

        # Creamos el menu de opciones y agregamos al layout_principal
        self.layout_menu = MenuOpcionesFrases()
        layout_principal.addLayout(self.layout_menu)
        self.layout_menu.ventana_agregar.btnGuardar.clicked.connect(self.agregar_palabra)

        self.layout_menu.ventana_editar.btnGuardar.clicked.connect(self.editar_palabra)

        self.layout_menu.ventana_eliminar.btnGuardar.clicked.connect(self.eliminar_palabra)

        # Llamamos a la clase para crear y agregar la tabla a el layout_principal
        self.tabla_palabras = TablaFrases()
        layout_principal.addWidget(self.tabla_palabras)

        self.setLayout(layout_principal)

    def agregar_palabra(self):
        print("entro")
        try:
            frase_espanol = self.layout_menu.ventana_agregar.f_espanol.text().strip()
            frase_ingles = self.layout_menu.ventana_agregar.f_ingles.text().strip()
            print(frase_ingles, frase_espanol)
            categoria = self.layout_menu.ventana_agregar.categoria_f.currentText()
            descripcion = self.layout_menu.ventana_agregar.descripcion_f.toPlainText().strip()

            print(frase_ingles.isalpha())
            print(frase_espanol.isalpha())

            # if re.match(r'^[\p{L}\s]+$', frase_ingles, re.UNICODE) and re.match(r'^[\p{L}\s]+$', frase_espanol, re.UNICODE):

            datos = [
                frase_ingles,
                frase_espanol,
                categoria,
                descripcion
            ]

            print(datos)

            FrasesDB.insertar_frase(frase_ingles=datos[0],
                                    frase_espanol=datos[1],
                                    categoria=datos[2],
                                    descripcion_frase=datos[3])

            # else:
            #     QMessageBox.critical(self, "Error", "Could not insert data, please restart or try again",
            #                          QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Close)
        except Exception as e:
            print(e)
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
            # FrasesDB.actualizar_registro(palabra_espanol=palabra_espanol,
            #                                palabra_ingles=palabra_ingles,
            #                                descripcion_palabra=descripcion,
            #                                id_palabra=id_palabra)
        except Exception as e:
            pass
        finally:
            self.tabla_palabras.setRowCount(0)
            self.tabla_palabras.actualizar_tabla()
            self.layout_menu.ventana_editar.actualizar_completer()

    def eliminar_palabra(self):
        try:
            id_palabra = self.layout_menu.ventana_eliminar.id_word.text()
            # PalabrasDB.eliminar_palabra(id_palabra=id_palabra)
        except Exception as e:
            pass
        finally:
            self.tabla_palabras.setRowCount(0)
            self.tabla_palabras.actualizar_tabla()
            self.layout_menu.ventana_eliminar.actualizar_completer()


class MenuOpcionesFrases(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.ventana_agregar = VentanaAgregarFrases()
        self.ventana_eliminar = VentanaEliminarFrases()
        self.ventana_editar = VentanaEditarFrases()
        self.ventana_buscar = VentanaBuscarFrases()

        self.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.btnAgregar = QPushButton(text="Add Phrase",
                                      icon=QIcon(QPixmap("Imagenes/Blueprint/blueprint--plus.png")))
        self.btnAgregar.setFixedSize(120, 40)
        self.btnAgregar.pressed.connect(self.abrir_ventana_agregar)
        self.addWidget(self.btnAgregar)

        self.btnEliminar = QPushButton(text="Delete Phrase",
                                       icon=QIcon(QPixmap("Imagenes/Blueprint/blueprint--minus.png")))
        self.btnEliminar.setFixedSize(120, 40)
        self.btnEliminar.pressed.connect(self.abrir_ventana_eliminar)
        self.addWidget(self.btnEliminar)

        self.btnEditar = QPushButton(text="Edit Phrase",
                                     icon=QIcon(QPixmap("Imagenes/Blueprint/blueprint--pencil.png")))
        self.btnEditar.pressed.connect(self.abrir_ventana_editar)
        self.btnEditar.setFixedSize(120, 40)
        self.addWidget(self.btnEditar)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setFrameShadow(QFrame.Shadow.Plain)
        separator.setFixedSize(5, 40)
        self.addWidget(separator)

        btnBuscar = QPushButton(text="Search Phrase", icon=QIcon(QPixmap("Imagenes/blue-document-search-result.png")))
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

class TablaFrases(QTableWidget):
    def __init__(self):
        super().__init__()

        cabezeras = ["ID", "English Phrase", "Spanish Translation", "Category", "Description"]
        self.setColumnCount(len(cabezeras))
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Darle nombres a las cabeceras de la tabla
        self.setHorizontalHeaderLabels(cabezeras)

        self.actualizar_tabla()

    def actualizar_tabla(self):
        datos = FrasesDB.seleccionar_todas_las_frases()

        format = QTextCharFormat()
        format.setFontUnderline(True)

        for fila, (id_frase, frase_ingles, frase_espanol, categoria, descripcion_frase) in enumerate(datos):
            self.insertRow(fila)
            self.setItem(fila, 0, QTableWidgetItem(str(id_frase)))
            self.item(fila, 0).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 0).setForeground(QBrush(QColor("blue")))
            self.item(fila, 0).setFont(QFont("Arial", 10, QFont.Bold))
            self.item(fila, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 1, QTableWidgetItem(frase_ingles))
            self.item(fila, 1).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 2, QTableWidgetItem(frase_espanol))
            self.item(fila, 2).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 3, QTableWidgetItem(categoria))
            self.item(fila, 3).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 4, QTableWidgetItem(descripcion_frase))
            self.item(fila, 4).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 4).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
