from customtkinter import CTk,CTkEntry,CTkFrame,CTkTabview
from Utiles.Centrar_Ventana_Geometry import centerwindows

class Layout:
    def __init__(self) -> None:
        self.root = CTk()
        self.root.title("Diccionario - Ingles")
        centerwindows(self.root,360,360)
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.root.config(border=20)
        self.tabs()
        self.principal()

        self.root.mainloop()
    
    def tabs(self):
        self.tab_principal = CTkTabview(self.root)
        self.tab_principal.grid(row=0,column=0,sticky="news")

        tab1 = self.tab_principal.add("Words")
        tab2 = self.tab_principal.add("Phrases")
        tab3 = self.tab_principal.add("Topics")
        tab4 = self.tab_principal.add("Settings")
    
    def principal(self):
        frame = CTkFrame(self.tab_principal)
        frame.grid(row=0,column=0,sticky="news")

    def xd(self):
        pass

Layout()