from PySide6.QtWidgets import QMainWindow, QApplication

from Tabuladores.Tabs import Tabs


class DiccionarioIngles(QMainWindow):
    def __init__(self):
        super().__init__()

        # Agregamos algunas configuraciones a la Ventana
        self.setWindowTitle("English Dictionary")
        self.resize(1000, 800)

        # Creamos los Tabs
        tabs = Tabs()

        self.setCentralWidget(tabs)


if __name__ == '__main__':
    app = QApplication([])
    ventana = DiccionarioIngles()
    ventana.show()
    app.exec()
