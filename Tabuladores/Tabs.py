from PySide6.QtWidgets import QTabWidget

from Tabuladores.TabFrases import TabFrases
from Tabuladores.TabPalabras import TabPalabras


class Tabs(QTabWidget):
    def __init__(self):
        super().__init__()

        # Creamos el tab de palabras
        tabPalabras = TabPalabras()
        self.addTab(tabPalabras, "Words")

        # Creamos el tab de frases
        tabFrases = TabFrases()
        self.addTab(tabFrases, "Phrases")
