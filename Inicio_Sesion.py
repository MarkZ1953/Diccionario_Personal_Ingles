from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry, CTkFrame


class Iniciar_Sesion:
    def __init__(self) -> None:
        self.root = CTk()
        self.root.title("Login")
        self.root.config(border=20)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.widgets()
        self.root.mainloop()


    def widgets(self):
        frame = CTkFrame(self.root)
        frame.grid(row=0, column=0, sticky="news")

        frame.columnconfigure(0, weight=1)

        CTkLabel(frame, text="Login", font=("Arial", 25)).grid(row=0, column=0, pady=40)

        self.usuario = CTkEntry(frame, placeholder_text="User", width=180)
        self.usuario.grid(row=1, column=0)

        self.contrasena = CTkEntry(frame, placeholder_text="Password", show="*", width=180)
        self.contrasena.grid(row=2, column=0, pady=15)

        bton = CTkButton(frame, text="Accept", cursor="hand2")
        bton.grid(row=3, column=0, pady=30)


if __name__ == '__main__':
    Iniciar_Sesion()
