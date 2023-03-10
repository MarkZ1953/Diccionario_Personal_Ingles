from customtkinter import CTkFrame, CTkEntry, CTkLabel, CTk, CTkToplevel, CTkButton

# Variable global para mantener el seguimiento del estado de la ventana del formulario
formulario_abierto = False

class Palabras:
    def __init__(self, tab_frases) -> None:
        self.tab_frases = tab_frases
        self.widgets()

    def widgets(self):
        boton = CTkButton(self.tab_frases, text="", command=lambda: self.abrir_formulario())
        boton.grid(row=0, column=0)

    def abrir_formulario(self):
        global formulario_abierto
        if not formulario_abierto:
            self.temp = CTkToplevel()
            self.formulario()
            formulario_abierto = True
        else:
            self.temp.focus()

    def cerrar_formulario(self):
        global formulario_abierto
        formulario_abierto = False
        self.temp.destroy()

    def formulario(self):
        #self.temp = CTkToplevel()

        frame = CTkFrame(self.temp)
        frame.grid(row=0, column=0)

        pingles = CTkEntry(self.temp, placeholder_text="Enlglish Word")
        pingles.grid(row=0, column=0)
        pespanol = CTkEntry(self.temp, placeholder_text="Spanish Translate")
        pespanol.grid(row=1, column=0)

        boton_cerrar = CTkButton(self.temp, text="Cerrar", command=lambda: self.cerrar_formulario())
        boton_cerrar.grid(row=2, column=0)
