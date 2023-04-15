from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, \
    QTextEdit, QStackedWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicación de Páginas")
        self.setGeometry(100, 100, 800, 600)

        # Crear el widget central y el layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Crear el combo box para seleccionar la página
        self.page_combo_box = QComboBox()
        self.page_combo_box.currentIndexChanged.connect(self.change_page)
        self.layout.addWidget(self.page_combo_box)

        # Crear el stacked widget para las páginas
        self.page_stacked_widget = QStackedWidget()
        self.layout.addWidget(self.page_stacked_widget)

        # Agregar la primera página
        self.add_page()

        # Agregar el botón para agregar una nueva página
        add_page_button_layout = QHBoxLayout()
        self.layout.addLayout(add_page_button_layout)
        add_page_button = QPushButton("Agregar Página")
        add_page_button.clicked.connect(self.add_page)
        add_page_button_layout.addWidget(add_page_button)

    def add_page(self):
        # Crear un nuevo widget para la página
        new_page_widget = QWidget()
        new_page_layout = QVBoxLayout()
        new_page_widget.setLayout(new_page_layout)

        # Agregar un text edit para ingresar texto
        text_edit = QTextEdit()
        new_page_layout.addWidget(text_edit)

        # Agregar la página al stacked widget y al combo box
        page_index = self.page_stacked_widget.addWidget(new_page_widget)
        self.page_combo_box.addItem(f"Página {page_index + 1}")

        # Seleccionar la nueva página
        self.page_combo_box.setCurrentIndex(page_index)

    def change_page(self, index):
        # Cambiar la página actual del stacked widget
        self.page_stacked_widget.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
