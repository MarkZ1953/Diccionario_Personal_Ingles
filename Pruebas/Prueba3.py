from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Ventana")
        self.setGeometry(100, 100, 800, 600)

        # Crear el QStackedWidget
        self.stacked_widget = QStackedWidget()

        # Crear las páginas (widgets) a mostrar en el QStackedWidget
        page1 = QWidget()
        layout1 = QVBoxLayout()
        label1 = QLabel("Página 1")
        button1 = QPushButton("Ir a Página 2")
        button1.clicked.connect(self.show_page2)
        layout1.addWidget(label1)
        layout1.addWidget(button1)
        page1.setLayout(layout1)

        page2 = QWidget()
        layout2 = QVBoxLayout()
        label2 = QLabel("Página 2")
        button2 = QPushButton("Ir a Página 1")
        button2.clicked.connect(self.show_page1)
        layout2.addWidget(label2)
        layout2.addWidget(button2)
        page2.setLayout(layout2)

        # Agregar las páginas al QStackedWidget
        self.stacked_widget.addWidget(page1)
        self.stacked_widget.addWidget(page2)

        # Establecer el QStackedWidget como widget central de la ventana
        self.setCentralWidget(self.stacked_widget)

    def show_page1(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_page2(self):
        self.stacked_widget.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
