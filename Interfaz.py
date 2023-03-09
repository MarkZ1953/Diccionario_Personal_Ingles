from customtkinter import CTk,CTkEntry,CTkFrame,CTkTabview,CTkButton,CTkLabel
from Utiles.Centrar_Ventana_Geometry import centerwindows
import json

class Layout:

    #colores
    
    _DARK = "#302c2c"

    def __init__(self) -> None:
        self.root = CTk()
        self.root.title("Diccionario - Ingles")
        centerwindows(self.root,360,360)
        self.root.columnconfigure(0,weight=1)
        self.root._set_appearance_mode("white") # system, dark, light


        self.root.rowconfigure(0,weight=0)
        self.root.rowconfigure(1,weight=1)

        self.root.config(border=20)

        self.xd()

        #self.tabs()
        #self.principal()

        self.root.mainloop()
    
    def tabs(self):
        self.tab_principal = CTkTabview(self.root)
        self.tab_principal.grid(row=1,column=0,sticky="news")

        self.tab1 = self.tab_principal.add("Words")
        tab2 = self.tab_principal.add("Phrases")
        tab3 = self.tab_principal.add("Topics")
        tab4 = self.tab_principal.add("Settings")
    
    def principal(self):
        entry = CTkEntry(self.tab1)
        entry.grid(row=0,column=0)

        frame = CTkFrame(self.root,height=400)
        frame.grid(row=0,column=0,sticky="new")
        frame.columnconfigure(0,weight=1)

        self.titulo = CTkLabel(frame,text="Welcome Back",font=("Arial",40),height=80)
        self.titulo.grid(row=0,column=0,sticky="ns")

    def xd(self):
        with json.load("Configuraciones.json") as archivo:
            print(archivo.read())


Layout()

# def configuracion_fuente_widgets(self):
#         with open("Recursos/Configuraciones.json") as archivo:
#             configuraciones = json.load(archivo)
#             return configuraciones["font"]

#     def listar_fuentes(self):
#         with open("Recursos/Tipografias.txt") as tipografias:
#             return tipografias.read()

#     def guardar_cambios(self):
#         if messagebox.askyesno("Advertencia","¿Esta seguro de guardar los cambios?"):
#             try:
#                 with open("Recursos/Configuraciones.json","r") as archivo:
#                     datos = json.load(archivo)
#                 datos["font"] = self.combo.get()
#                 datos["font-size"] = self.spinbox.get()
#                 with open("Recursos/Configuraciones.json","w") as archivo:
#                     json.dump(datos,archivo)
#             except:
#                 messagebox.showerror("Error","Algo ha salido mal, intente de nuevo o reinicie el programa.")