from customtkinter import CTk,CTkButton

class Ejemplo:
    def __init__(self) -> None:
        self.root = CTk()
        CTkButton(self.root,text="Cerrar",command=lambda:self.cerrar()).grid(row=0,column=0)
        self.root.mainloop()

    def cerrar(self):
        self.root.destroy()

Ejemplo()