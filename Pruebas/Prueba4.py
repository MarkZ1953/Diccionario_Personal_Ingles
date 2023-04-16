from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QCompleter
from PySide6.QtCore import QStringListModel, Qt


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Crear widgets
        self.search_input = QLineEdit()

        # Crear layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.search_input)

        # Establecer layout principal
        self.setLayout(layout)

        # Crear modelo de lista de palabras
        words = ["hola", "mouse", "computador", "a", "abecedario"]
        self.wordListModel = QStringListModel(words)

        # Crear QCompleter
        self.completer = QCompleter(self.wordListModel)
        # self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchContains)  # Establecer filtro para que busque las palabras que contengan el texto ingresado

        # Establecer el QCompleter en el QLineEdit
        self.search_input.setCompleter(self.completer)


app = QApplication([])
main_widget = MainWidget()
main_widget.show()
app.exec_()
