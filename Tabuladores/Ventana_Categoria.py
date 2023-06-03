from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel


class VentanaCategorias(QWidget):
    def __init__(self):
        super().__init__()

        # Agregamos algunas configuraciones a la Ventana
        self.setWindowTitle("Categories")
        self.resize(200, 100)

        # Creamos un Layout Principal
        layoutPrincipal = QHBoxLayout()

        layoutBotones = QVBoxLayout()
        layoutForm = QGridLayout()

        layoutForm.addWidget(QLabel("Id Categoria"), 0, 0)

        # Creamos y agregamos los botones al layout de botones
        btnAgregar = QPushButton("Add")
        layoutBotones.addWidget(btnAgregar)

        btnEditar = QPushButton("Edit")
        layoutBotones.addWidget(btnEditar)

        btnEliminar = QPushButton("Delete")
        layoutBotones.addWidget(btnEliminar)

        btnCerrar = QPushButton("Close")
        layoutBotones.addWidget(btnCerrar)

        # Agregamos los layouts al layout principal
        layoutPrincipal.addLayout(layoutForm)
        layoutPrincipal.addLayout(layoutBotones)

        self.setLayout(layoutPrincipal)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaCategorias()
    ventana.show()
    app.exec()
