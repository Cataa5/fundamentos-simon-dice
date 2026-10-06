import tkinter as tk
import random

class VistaInicioSimonDice:
    def __init__(self, master, accion_jugar, accion_salir):
        self.master = master
        self.master.geometry("1000x700")

        self.img_fondo = tk.PhotoImage(file="assets/imagenes/fondoInicio2.png")
        self.canvas = tk.Canvas(self.master, width=1000, height=700, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")

        self.frames_panda = [tk.PhotoImage(file=f"assets/imagenes/espera{i}.png") for i in range(1, 4)]
        self.frame_actual = 0
        
        self.panda_id = self.canvas.create_image(180, 555, image=self.frames_panda[0], anchor="center")

        self.panda_direccion = 1
        self.panda_pasos = 0
        
        self.animar_panda()
        
        palabra = "SECUENCIA DE LUCES"
        self.letras_id = []
        x_inicial = 370 

        for letra in palabra:
            id_texto = self.canvas.create_text(x_inicial, 260, text=letra, font=("Minecraft", 14, "bold"), fill="#F4E8C1")
            self.letras_id.append(id_texto)
            x_inicial += 18 
            
        btn_jugar = tk.Button(self.master, text="JUGAR", font=("Minecraft", 16, "bold"), bg="#C99559", fg="#464646", activebackground="#A87840", activeforeground="#464646", relief="raised", bd=4, command=accion_jugar)
        btn_jugar.place(relx=0.52, rely=0.60, width=250, height=50, anchor="center")

        btn_salir = tk.Button(self.master, text="SALIR", font=("Minecraft", 16, "bold"), bg="#C99559", fg="#464646", activebackground="#A87840", activeforeground="#464646", relief="raised", bd=4, command=accion_salir)
        btn_salir.place(relx=0.52, rely=0.70, width=250, height=50, anchor="center")

        self.animar_luces()

    def animar_panda(self):
        # Si el canvas fue destruido al cambiar de pantalla, cortamos el bucle
        if not self.canvas.winfo_exists():
            return
        
        if self.panda_pasos >= 8:
            self.panda_direccion *= -1
            self.panda_pasos = 0
            
        self.canvas.move(self.panda_id, 0, self.panda_direccion)
        self.panda_pasos += 1
        
        self.frame_actual = (self.frame_actual + 1) % len(self.frames_panda)
        self.canvas.itemconfig(self.panda_id, image=self.frames_panda[self.frame_actual])
        
        self.master.after(2000, self.animar_panda)

    def animar_luces(self):
        if not self.canvas.winfo_exists():
            return
        
        colores = ["#8A2BE2", "#FFD700", "#FFA500", "#1E90FF"] 
        color_base = "#544F48"
        
        for id_letra in self.letras_id:
            self.canvas.itemconfig(id_letra, fill=color_base)
            
        letras_random = random.sample(self.letras_id, 1)
        
        for id_letra in letras_random:
            color_azar = random.choice(colores)
            self.canvas.itemconfig(id_letra, fill=color_azar)
            
        self.master.after(800, self.animar_luces)