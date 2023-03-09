from customtkinter import CTk,CTkEntry,CTkFrame
from Utiles.Centrar_Ventana_Geometry import centerwindows

class Layout:
    def __init__(self) -> None:
        self.root = CTk()
        self.root.title("Diccionario - Ingles")
        centerwindows(self.root,360,360)
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.root.config(border=20)
        self.principal()

        self.root.mainloop()
    
    def principal(self):
        frame = CTkFrame(self.root)
        frame.grid(row=0,column=0,sticky="news")

    def xd(self):
        pass

Layout()