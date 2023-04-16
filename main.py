from PySide6.QtWidgets import QMainWindow, QApplication

from Tabuladores.Tabs import Tabs


class DiccionarioIngles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("English Dictionary")
        self.resize(800, 600)

        tabs = Tabs()

        self.setCentralWidget(tabs)


if __name__ == '__main__':
    app = QApplication([])
    ventana = DiccionarioIngles()
    ventana.show()
    app.exec()
