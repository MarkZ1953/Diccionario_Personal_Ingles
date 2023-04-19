from PySide6.QtWidgets import QTabWidget, QWidget, QFrame

from Tabuladores.TabFrases import TabFrases
from Tabuladores.TabPalabras import TabPalabras



class Tabs(QTabWidget):
    def __init__(self):
        super().__init__()

        # Creamos el tab de palabras
        tab_palabras = TabPalabras()
        self.addTab(tab_palabras, "Words")

        # Creamos el tab de palabras
        tab_frases = TabFrases()
        self.addTab(tab_frases, "Phrases")

