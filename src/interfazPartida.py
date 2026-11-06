import tkinter as tk
from animacionPanda import AnimacionPanda
from efectos import GestorConfeti
from secuenciaLuces import GestorLuces

class VistaSimonDice:
    def __init__(self, master, accion_boton, accion_reiniciar, accion_volver_menu):
        self.master = master
        self.accion_boton = accion_boton 
        self.accion_reiniciar = accion_reiniciar
        self.accion_volver_menu = accion_volver_menu
        
        self.master.geometry("1000x700")

        self.elementos_cartel = []
        
        # ------------- Cargar Imágenes -------------------
        self.img_fondo = tk.PhotoImage(file="assets/imagenes/fondo.png")
        self.img_acierto = tk.PhotoImage(file="assets/imagenes/acerto.png")
        self.img_derrota = tk.PhotoImage(file="assets/imagenes/perdiste.png")
        self.img_ganada = tk.PhotoImage(file="assets/imagenes/ganaste.png")
        self.frames_espera = [tk.PhotoImage(file="assets/imagenes/base.png"), tk.PhotoImage(file="assets/imagenes/espera1.png"), tk.PhotoImage(file="assets/imagenes/espera2.png"), tk.PhotoImage(file="assets/imagenes/espera3.png"), tk.PhotoImage(file="assets/imagenes/bostezo1.png"), tk.PhotoImage(file="assets/imagenes/bostezo2.png")]
        self.frames_gano = [tk.PhotoImage(file="assets/imagenes/gano1.png"), tk.PhotoImage(file="assets/imagenes/gano2.png"), tk.PhotoImage(file="assets/imagenes/gano3.png"), tk.PhotoImage(file="assets/imagenes/gano4.png"), tk.PhotoImage(file="assets/imagenes/gano5.png"), tk.PhotoImage(file="assets/imagenes/gano6.png"), tk.PhotoImage(file="assets/imagenes/gano7.png"), tk.PhotoImage(file="assets/imagenes/gano8.png")]
        self.frames_perdio = [tk.PhotoImage(file="assets/imagenes/perdio1.png"), tk.PhotoImage(file="assets/imagenes/perdio2.png"), tk.PhotoImage(file="assets/imagenes/perdio1.png"), tk.PhotoImage(file="assets/imagenes/perdio3.png")]
        
        # ----------- Canvas y Capas ---------------
        self.canvas = tk.Canvas(self.master, width=1000, height=700, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")
        
        self.panda_id = self.canvas.create_image(400, 300, image=self.frames_espera[0])
        
        # -------------- Filtro rojo y carteles -----------------
        self.filtro_rojo = self.canvas.create_rectangle(0, 0, 1000, 700, outline="#8B0000", width=30, fill="red", stipple="gray50", state="hidden")
        self.cartel_derrota_id = self.canvas.create_image(500, 350, image=self.img_derrota, state="hidden")
        self.cartel_ganada_id = self.canvas.create_image(500, 350, image=self.img_ganada, state="hidden")
        
        # ------------- Panel y Botones -----------------
        self.panel_madera = tk.Frame(self.master, bg="#563D2B", bd=6, relief="ridge", padx=10, pady=10)
        self.panel_madera.place(relx=0.5, rely=0.85, anchor="center")
        
        btn_violeta = tk.Button(self.panel_madera, bg="#5B2C6F", width=6, height=3, command=lambda: self.accion_boton('v'))
        btn_amarillo = tk.Button(self.panel_madera, bg="#F1C40F", width=6, height=3, command=lambda: self.accion_boton('a'))
        btn_naranja = tk.Button(self.panel_madera, bg="#E67E22", width=6, height=3, command=lambda: self.accion_boton('n'))
        btn_azul = tk.Button(self.panel_madera, bg="#193A7B", width=6, height=3, command=lambda: self.accion_boton('z'))
        
        btn_violeta.pack(side="left", padx=5)
        btn_amarillo.pack(side="left", padx=5)
        btn_naranja.pack(side="left", padx=5)
        btn_azul.pack(side="left", padx=5)
        
        self.botones = [btn_violeta, btn_amarillo, btn_naranja, btn_azul]
        self.botones_map = {'v': btn_violeta, 'a': btn_amarillo, 'n': btn_naranja, 'z': btn_azul}
        self.colores_base = {'v': '#5B2C6F', 'a': '#F1C40F', 'n': '#E67E22', 'z': '#193A7B'}
        self.colores_luz = {'v': "#BC86D2", 'a': "#F4E197", 'n': "#F9CEA9", 'z': "#87C2E9"}
        
        # ----------- INICIALIZAR GESTORES EXTERNOS -----------
        self.animacion = AnimacionPanda(self.master, self.canvas, self.panda_id, self.frames_espera, self.frames_gano, self.img_acierto, self.frames_perdio)
        self.efectos = GestorConfeti(self.master, self.canvas)
        self.luces = GestorLuces(self.master, self.botones_map, self.colores_base, self.colores_luz, self.cambiar_estado_botones)
        
        self.animacion.iniciar_espera()

    def cambiar_estado_botones(self, estado):
        for btn in self.botones:
            btn.config(state=estado)

    # --------------- MÉTODOS PARA EL CONTROLADOR ----------------
    def mostrar_acierto(self):
        self.animacion.mostrar_acierto_temporal(self.volver_a_espera)

    def volver_a_espera(self):
        if self.animacion.estado_actual == "GANO" or self.canvas.itemcget(self.filtro_rojo, "state") == "normal":
            return
            
        self.animacion.iniciar_espera()

    def mostrar_derrota(self):
        self.cambiar_estado_botones(tk.DISABLED)
        self.animacion.mostrar_derrota()
        self.panel_madera.place_forget()
        self.canvas.itemconfig(self.filtro_rojo, state="normal")
        self.canvas.itemconfig(self.cartel_derrota_id, state="normal")
        self.master.after(1000, self.mostrar_menu_final)

    def mostrar_victoria(self):
        self.cambiar_estado_botones(tk.DISABLED) 
        self.animacion.iniciar_victoria()
        self.panel_madera.place_forget()
        self.canvas.itemconfig(self.cartel_ganada_id, state="normal")
        self.efectos.lanzar_confeti() 
        self.master.after(1000, self.mostrar_menu_final)

    def reiniciar_interfaz(self):
        self.efectos.limpiar_confeti() 
        self.canvas.itemconfig(self.filtro_rojo, state="hidden")
        self.canvas.itemconfig(self.cartel_derrota_id, state="hidden")
        self.canvas.itemconfig(self.cartel_ganada_id, state="hidden")
        self.panel_madera.place(relx=0.5, rely=0.85, anchor="center")
        self.cambiar_estado_botones(tk.NORMAL)
        self.animacion.iniciar_espera()

    def reproducir_secuencia(self, secuencia_objetivo):
        self.luces.reproducir_secuencia(secuencia_objetivo) 

    # --------------- MENÚ FINAL ----------------
    def mostrar_menu_final(self):
        self.btn_jugar_de_nuevo = tk.Button(
            self.master, text="VOLVER A JUGAR", font=("Minecraft", 16, "bold"), 
            bg="#C99559", fg="#3A2212", activebackground="#A87840", activeforeground="#464646", 
            relief="raised", bd=4, command=self.reiniciar_partida
        )
        self.btn_jugar_de_nuevo.place(relx=0.5, rely=0.55, width=280, height=50, anchor="center")

        self.btn_volver_inicio = tk.Button(
            self.master, text="VOLVER AL INICIO", font=("Minecraft", 16, "bold"), 
            bg="#C99559", fg="#3A2212", activebackground="#A87840", activeforeground="#464646", 
            relief="raised", bd=4, command=self.volver_al_menu
        )
        self.btn_volver_inicio.place(relx=0.5, rely=0.66, width=280, height=50, anchor="center")

    def reiniciar_partida(self):
        self.btn_jugar_de_nuevo.destroy()
        self.btn_volver_inicio.destroy()
        self.accion_reiniciar()

    def volver_al_menu(self):
        self.accion_volver_menu()