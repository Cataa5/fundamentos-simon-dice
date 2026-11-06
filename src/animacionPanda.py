class AnimacionPanda:
    def __init__(self, master, canvas, panda_id, frames_espera, frames_gano, img_acierto, frames_perdio):
        self.master = master
        self.canvas = canvas
        self.panda_id = panda_id
        
        self.frames_espera = frames_espera
        self.frames_gano = frames_gano
        self.frames_perdio = frames_perdio
        self.img_acierto = img_acierto
        
        self.indice = 0
        self.estado_actual = "ESPERA" 

    def iniciar_espera(self):
        self.estado_actual = "ESPERA"
        self.indice = 0
        self.bucle_espera()

    def bucle_espera(self):
        if self.estado_actual != "ESPERA" or not self.canvas.winfo_exists():
            return
        img = self.frames_espera[self.indice]
        self.canvas.itemconfig(self.panda_id, image=img)
        self.indice = (self.indice + 1) % len(self.frames_espera)       
        self.master.after(1000, self.bucle_espera)

    def iniciar_victoria(self):
        self.estado_actual = "GANO"
        self.indice = 0
        self.bucle_victoria()

    def bucle_victoria(self):
        if self.estado_actual != "GANO" or not self.canvas.winfo_exists():
            return
        img = self.frames_gano[self.indice]
        self.canvas.itemconfig(self.panda_id, image=img)
        self.indice = (self.indice + 1) % len(self.frames_gano)
        self.master.after(300, self.bucle_victoria)

    def bucle_derrota(self):
        if self.estado_actual != "PERDIO" or not self.canvas.winfo_exists():
            return
        img = self.frames_perdio[self.indice]
        self.canvas.itemconfig(self.panda_id, image=img)
        self.indice = (self.indice + 1) % len(self.frames_perdio)
        self.master.after(300, self.bucle_derrota)

    def mostrar_acierto_temporal(self, callback_volver):
        self.estado_actual = "PAUSA"
        self.canvas.itemconfig(self.panda_id, image=self.img_acierto)
        self.master.after(500, callback_volver)

    def mostrar_derrota(self):
        self.estado_actual = "PERDIO"
        self.indice = 0
        self.bucle_derrota()