import tkinter as tk
class VistaJugarSimonDice:
    def __init__(self, master, accionJugarNormal, accionJugarReverso, accionVolver):
        self.master = master
        self.master.geometry("1000x700")

        self.img_fondo = tk.PhotoImage(file="assets/imagenes/fondoJugar.png")

        self.canvas = tk.Canvas(self.master, width=1000, height=700, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")

        btn_jugar = tk.Button(self.master, text="MODO NORMAL", font=("Minecraft", 16, "bold"), bg="#C99559", fg="#3A2212", activebackground="#A87840", activeforeground="#3A2212", relief="raised", bd=4, command=accionJugarNormal)
        btn_jugar.place(relx=0.52, rely=0.60, width=250, height=50, anchor="center")
        
        btn_salir = tk.Button(self.master, text="MODO REVERSO", font=("Minecraft", 16, "bold"), bg="#C99559", fg="#3A2212", activebackground="#A87840", activeforeground="#3A2212", relief="raised", bd=4, command=accionJugarReverso)
        btn_salir.place(relx=0.52, rely=0.70, width=250, height=50, anchor="center")

        btn_salir = tk.Button(self.master, text="VOLVER AL MENÚ", font=("Minecraft", 16, "bold"), bg="#C99559", fg="#3A2212", activebackground="#A87840", activeforeground="#3A2212", relief="raised", bd=4, command=accionVolver)
        btn_salir.place(relx=0.52, rely=0.80, width=250, height=50, anchor="center")

        # ----------------- BOTÓN DE AYUDA -----------------
        self.btn_ayuda = tk.Button(self.master, text="?", font=("Minecraft", 16, "bold"), bg="#C99559", fg="#3A2212", activebackground="#A87840", activeforeground="#FFFFFF", relief="raised", bd=4, command=self.mostrar_modal_ayuda)
        self.btn_ayuda.place(x=930, y=20, width=45, height=45)

    def mostrar_modal_ayuda(self):
        overlay_id = self.canvas.create_rectangle(0, 0, 1000, 700, fill="black", stipple="gray50", outline="")

        # Cartel 
        card = tk.Frame(self.master, bg="#563D2B", bd=6, relief="ridge", padx=25, pady=25)
        card.place(relx=0.5, rely=0.5, anchor="center", width=560, height=355)
        card.lift()

        # Función para limpiar la sombra y el cartel al hacer clic en cerrar
        def cerrar_ayuda():
            self.canvas.delete(overlay_id)
            card.destroy()

        lbl_titulo = tk.Label(card, text="AYUDA CON LOS MODOS", font=("Minecraft", 13, "bold"), bg="#563D2B", fg="#F4E197")
        lbl_titulo.pack(pady=(0, 10))
        
        txt_normal = (
            "★ MODO NORMAL (ALL)\n"
            "\n"
            "   • Ingresá la secuencia en el MISMO ORDEN mostrado.\n"
            "\n"
            "   • Se valida mediante un Autómata Linealmente Limitado que procesa\n"
            "     en cinta la palabra L = {w#w}."
            "\n"
        )
        lbl_normal = tk.Label(card, text=txt_normal, font=("Minecraft", 10), bg="#563D2B", fg="#FFFFFF", justify="left", anchor="w")
        lbl_normal.pack(fill="x", pady=6)

        txt_reverso = (
            "★ MODO REVERSO (AP)\n"   
            "\n"       
            "   • Ingresá la secuencia en ORDEN INVERSO (del último al primero).\n"
            "\n"
            "   • Se valida con un Autómata de Pila (AP) que almacena los colores\n"
            "     y exige desapilarlos en LIFO para L = {w#w^R}."
        )
        lbl_reverso = tk.Label(card, text=txt_reverso, font=("Minecraft", 10), bg="#563D2B", fg="#FFFFFF", justify="left", anchor="w")
        lbl_reverso.pack(fill="x", pady=6)

        btn_cerrar = tk.Button(card, text="¡ENTENDIDO!", font=("Minecraft", 11, "bold"), bg="#C99559", fg="#3A2212", activebackground="#A87840", bd=4, relief="raised", command=cerrar_ayuda)
        btn_cerrar.pack(pady=(20, 0))