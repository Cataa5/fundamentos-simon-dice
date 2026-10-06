import tkinter as tk

class GestorLuces:
    def __init__(self, master, botones_map, colores_base, colores_luz, callback_estado_botones):
        self.master = master
        self.botones_map = botones_map
        self.colores_base = colores_base
        self.colores_luz = colores_luz
        self.cambiar_estado = callback_estado_botones

    def reproducir_secuencia(self, secuencia_objetivo, indice=0):
        self.cambiar_estado(tk.DISABLED)
        
        if indice < len(secuencia_objetivo):
            letra = secuencia_objetivo[indice]
            boton = self.botones_map[letra]
            boton.config(bg=self.colores_luz[letra])
            self.master.after(400, lambda: self.apagar_boton(letra, secuencia_objetivo, indice))
        else:
            self.cambiar_estado(tk.NORMAL)
            
    def apagar_boton(self, letra, secuencia_objetivo, indice):
        boton = self.botones_map[letra]
        boton.config(bg=self.colores_base[letra])
        self.master.after(200, lambda: self.reproducir_secuencia(secuencia_objetivo, indice + 1))