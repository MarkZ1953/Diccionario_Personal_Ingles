from customtkinter import CTkFrame, CTkEntry, CTkLabel, CTkToplevel, CTkButton, CTk
from Utiles.Centrar_Ventana_Geometry import centerwindows
from tkinter.ttk import Treeview
from Conexion import Conexion

#Se declara una varible la cual el proposito de ella sera mantener el control 
#de la cantidad de formularios que se puedan abrir al momento de querer agregar una nueva palabra.
formulario_abierto = False

class Palabras:
    """
    Clase encargada de simular un tab que es abierto desde el modulo principal,
    en la clase se crean funciones y metodos de control para abrir y cerrar formularios, agregar 
    nueva palabras y definiciones a la base de datos y ver informacion en las tablas.
    """
    def __init__(self, tab_frases) -> None:
        self.tab_frases = tab_frases
        self.conexion = Conexion.obtenerConexion()
        self.widgets()

    def seleccionar_datos(self):
        with self.conexion.cursor() as cursor:
            sql = "SELECT * FROM diccionario"
            cursor.execute(sql)
            registros = cursor.fetchall()
            return registros
    
    def insertar_datos(self):
        with self.conexion.cursor() as cursor:
            sql = "INSERT INTO diccionario(p_ingles, p_espanol, nota) VALUES(%s, %s, %s)"

            pingles = self.pingles.get()
            pespanol = self.pespanol.get()
            notas = self.notas.get()

            datos = (pingles,pespanol,notas)
            cursor.execute(sql,(datos))
            #self.actualizar_tabla()
        
        self.conexion.commit()

    def widgets(self):

        heads = ["Id_Word","English Words","Spanish Translations","Notes"]
        
        self.tabla = Treeview(self.tab_frases,columns=("#1","#2","#3"))
        self.tabla.grid(row=0,column=0,sticky="ns")

        for i in range(4):
            self.tabla.column(f"#{i}",anchor="center")
            self.tabla.heading(f"#{i}",anchor="center",text=heads[i])
        
        registros = self.seleccionar_datos()

        for registro in registros:
            self.tabla.insert("","end",text=registro[0],values=(registro[1],registro[2],registro[3]))

        btnSalir = CTkButton(self.tab_frases, text="Add", command=lambda: self.abrir_formulario())
        btnSalir.grid(row=1, column=0)
    
    def actualizar_tabla(self):
        self.tabla.delete(self.tabla.get_children())
        registros = self.seleccionar_datos()
        for registro in registros:
            self.tabla.insert("","end",text=registro[0],values=(registro[1],registro[2],registro[3]))

    def abrir_formulario(self):
        global formulario_abierto
        if not formulario_abierto:
            self.temp = CTk()
            self.temp.config(border=20)
            centerwindows(self.temp,320,220)
            self.temp.rowconfigure(0,weight=1)
            self.temp.columnconfigure(0,weight=1)
            self.formulario()
            formulario_abierto = True
            self.temp.mainloop()
        else:
            self.temp.focus()

    def cerrar_formulario(self):
        """
        - Se ejecuta esta funcion cuando el boton de cerrar del formulario es presionado.
        - Cambia el valor de True a False de la variable que hace que no se pueda abrir mas de una vez el formulario.
        - Por ultimo se destruye el formulario.
        """
        global formulario_abierto
        formulario_abierto = False
        self.temp.destroy()

    def formulario(self):
        #Frame que contiene los widgets de las cajas de texto y los botones para cerrar y abrir el formulario.
        frame = CTkFrame(self.temp)
        frame.grid(row=0, column=0,sticky="news")
        frame.columnconfigure(0,weight=1)

        self.pingles = CTkEntry(frame, placeholder_text="Enlglish Word")
        self.pingles.grid(row=0, column=0,pady=10,padx=10,sticky="we")

        self.pespanol = CTkEntry(frame, placeholder_text="Spanish Translate")
        self.pespanol.grid(row=1, column=0,pady=5,padx=10,sticky="we")

        self.notas = CTkEntry(frame, placeholder_text="Notes")
        self.notas.grid(row=2, column=0,pady=5,padx=10,sticky="we")

        boton_abrir = CTkButton(frame, text="Save", command=lambda: self.insertar_datos())
        boton_abrir.grid(row=3, column=0,pady=5)

        boton_cerrar = CTkButton(frame, text="Close", command=lambda: self.cerrar_formulario())
        boton_cerrar.grid(row=3, column=1,pady=5)
