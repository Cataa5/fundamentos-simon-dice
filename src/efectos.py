import random

class GestorConfeti:
    def __init__(self, master, canvas):
        self.master = master
        self.canvas = canvas
        self.lista_confeti = []

    def lanzar_confeti(self):
        colores = ["#FF5733", "#33FF57", "#3357FF", "#F1C40F", "#9B59B6", "#E67E22", "#FFFFFF"]
        self.limpiar_confeti()
        for _ in range(150):
            x = random.randint(0, 1000)
            y = random.randint(-600, -50)
            ancho = random.randint(6, 14)
            alto = random.randint(6, 14)
            color = random.choice(colores)
            
            if random.choice([True, False]):
                fig_id = self.canvas.create_rectangle(x, y, x+ancho, y+alto, fill=color, outline="")
            else:
                fig_id = self.canvas.create_oval(x, y, x+ancho, y+alto, fill=color, outline="")
                
            self.lista_confeti.append({"id": fig_id, "vel": random.randint(4, 12)})
        self.animar_confeti()

    def animar_confeti(self):
        if not self.lista_confeti or not self.canvas.winfo_exists():
            return
        for particula in self.lista_confeti:
            self.canvas.move(particula["id"], 0, particula["vel"])
        self.master.after(30, self.animar_confeti)

    def limpiar_confeti(self):
        for particula in self.lista_confeti:
            self.canvas.delete(particula["id"])
        self.lista_confeti.clear()