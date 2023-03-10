from customtkinter import CTk,CTkButton,CTkEntry,CTkCheckBox,CTkLabel

class Configuraciones:
    """
    La clase configuraciones estara a cargo de mostrar los widgets, donde se le dara la disponibilidad al usuario
    para poder editar la aplicacion al gusto.
    """
    def __init__(self,tab4) -> None:
        self.tab_configuraciones = tab4 #Recibe el tab creado del Modulo principal "Interfaz"
    