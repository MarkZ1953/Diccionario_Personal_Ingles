from customtkinter import CTk,CTkLabel,CTkButton,CTkEntry,CTkFrame
from Utiles.Centrar_Ventana_Geometry import centerwindows
from Conexion import Conexion
from Interfaz import Layout
from tkinter import messagebox

class Iniciar_Sesion:
    def __init__(self) -> None:
        self.root = CTk()
        self.root.title("Login")
        
        centerwindows(self.root,360,360)
        self.root.config(border=20)
        self.root.rowconfigure(0,weight=1)
        self.root.columnconfigure(0,weight=1)
        self.root.resizable(False,False)
        self.conexion = Conexion.obtenerConexion()
        self.widgets()
        self.root.mainloop()
    
    def __del__(self):
        self.conexion.close()
    
    def widgets(self):
        frame = CTkFrame(self.root)
        frame.grid(row=0,column=0,sticky="news")

        frame.columnconfigure(0,weight=1)

        CTkLabel(frame,text="Login",font=("Arial",25)).grid(row=0,column=0,pady=40)

        self.usuario = CTkEntry(frame,placeholder_text="User",width=180)
        self.usuario.grid(row=1,column=0)

        self.contrasena = CTkEntry(frame,placeholder_text="Password",show="*",width=180)
        self.contrasena.grid(row=2,column=0,pady=15)

        bton = CTkButton(frame,text="Accept",cursor="hand2",command=lambda:self.verificar())
        bton.grid(row=3,column=0,pady=30)

        self.usuario.bind("<Return>",self.evento)
        self.contrasena.bind("<Return>",self.evento)

    def evento(self,e):
        self.verificar()

    def verificar(self):
        try:
            with self.conexion.cursor() as cursor:
                sql = "SELECT COUNT(*) FROM usuarios WHERE usuario = %s AND contrasena = %s"
                cursor.execute(sql,(self.usuario.get().strip(),self.contrasena.get().strip()))
                registros = cursor.fetchall()

            if registros[0][0] == 1:
                self.conexion.close()
                Layout(self.root)
            else:
                messagebox.showerror("Error","The username or Password is incorrect")
        except Exception as e:
            print(f"Error {e}")

Iniciar_Sesion()