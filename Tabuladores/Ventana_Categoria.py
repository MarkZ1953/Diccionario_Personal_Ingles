from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel


class VentanaCategorias(QWidget):
    def __init__(self):
        super().__init__()

        # Agregamos algunas configuraciones a la Ventana
        self.setWindowTitle("Categories")
        self.resize(200, 100)

        # Creamos un Layout Principal
        layoutPrincipal = QHBoxLayout()

        layout_botones = QVBoxLayout()
        layout_form = QGridLayout()

        layout_form.addWidget(QLabel("Id Categoria"), 0, 0)

        # Creamos y agregamos los botones al layout de botones
        btnAgregar = QPushButton("Add")
        layout_botones.addWidget(btnAgregar)

        btnEditar = QPushButton("Edit")
        layout_botones.addWidget(btnEditar)

        btnEliminar = QPushButton("Delete")
        layout_botones.addWidget(btnEliminar)

        btnCerrar = QPushButton("Close")
        layout_botones.addWidget(btnCerrar)

        # Agregamos los layouts al layout principal
        layoutPrincipal.addLayout(layout_form)
        layoutPrincipal.addLayout(layout_botones)

        self.setLayout(layoutPrincipal)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaCategorias()
    ventana.show()
    app.exec()
