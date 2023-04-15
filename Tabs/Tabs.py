from PySide6.QtWidgets import QTabWidget, QWidget


class Tabs(QTabWidget):
    def __init__(self):
        super().__init__()

        tab_palabras = QWidget()

        self.addTab(tab_palabras, "Words")
