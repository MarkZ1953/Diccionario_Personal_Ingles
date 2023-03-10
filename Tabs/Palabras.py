from customtkinter import CTkFrame, CTkEntry, CTkLabel, CTk, CTkToplevel, CTkButton
from Utiles.Centrar_Ventana_Geometry import centerwindows
from tkinter.ttk import Treeview

formulario_abierto = False

class Palabras:
    def __init__(self, tab_frases) -> None:
        self.tab_frases = tab_frases
        self.widgets()

    def widgets(self):
        boton = CTkButton(self.tab_frases, text="Add", command=lambda: self.abrir_formulario())
        boton.grid(row=0, column=0)

    def abrir_formulario(self):
        global formulario_abierto
        if not formulario_abierto:
            self.temp = CTkToplevel()
            self.temp.config(border=10)
            centerwindows(self.temp,260,200)
            self.temp.rowconfigure(0,weight=1)
            self.temp.columnconfigure(0,weight=1)
            self.formulario()
            formulario_abierto = True
        else:
            self.temp.focus()

    def cerrar_formulario(self):
        global formulario_abierto
        formulario_abierto = False
        self.temp.destroy()

    def formulario(self):
        frame = CTkFrame(self.temp)
        frame.grid(row=0, column=0,sticky="news")
        frame.columnconfigure(0,weight=1)
        pingles = CTkEntry(frame, placeholder_text="Enlglish Word")
        pingles.grid(row=0, column=0,pady=10,padx=10,sticky="we")
        pespanol = CTkEntry(frame, placeholder_text="Spanish Translate")
        pespanol.grid(row=1, column=0,pady=5,padx=10,sticky="we")
        boton_cerrar = CTkButton(frame, text="Cerrar", command=lambda: self.cerrar_formulario())
        boton_cerrar.grid(row=2, column=0,pady=5)
