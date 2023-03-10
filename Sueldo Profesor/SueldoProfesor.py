from customtkinter import CTk,CTkButton,CTkEntry,CTkLabel

class Calcular_Sueldo:
    def __init__(self) -> None:
        self.root = CTk()
        
        CTkLabel(self.root,text="CALCULAR EL SUELDO DEL PROFESOR",font=("Arial",14,"bold")).grid(row=0,columnspan=2)

        textos = ["Horas","Valor Hora","Sueldo"]

        for i in range(3):
            CTkLabel(self.root,text=textos[i]).grid(row=i+1,column=0,padx=5,pady=5)
            entry = CTkEntry(self.root)
            entry.grid(row=i+1,column=1)

        btnAceptar = CTkButton(self.root,text="Aceptar")
        btnAceptar.grid(row=4,column=0,padx=5,pady=5)
        btnSalir = CTkButton(self.root,text="Salir")
        btnSalir.grid(row=4,column=1,pady=5,padx=5)

        self.root.mainloop()

Calcular_Sueldo()