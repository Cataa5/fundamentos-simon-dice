import tkinter as tk

class GestorLuces:
    def __init__(self, master, botones_map, colores_base, colores_luz, callback_estado_botones):
        self.master = master
        self.botones_map = botones_map
        self.colores_base = colores_base
        self.colores_luz = colores_luz
        self.cambiar_estado = callback_estado_botones

    def reproducir_secuencia(self, secuencia, indice=0):
        if indice == 0:
            self.cambiar_estado(tk.DISABLED)

        # Si se mostraron todas las luces, recién ahí desbloqueamos
        if indice >= len(secuencia):
            self.cambiar_estado(tk.NORMAL)
            return

        letra = secuencia[indice]
        boton = self.botones_map[letra]

        if boton.winfo_exists():
            # Encender luz
            boton.config(bg=self.colores_luz[letra])

            # Apagar después de 400ms y pasar al siguiente
            self.master.after(400, lambda: self.apagar_y_continuar(letra, secuencia, indice))
            
    def apagar_y_continuar(self, letra, secuencia, indice):
        boton = self.botones_map[letra]
        if boton.winfo_exists():
            boton.config(bg=self.colores_base[letra])
        self.master.after(200, lambda: self.reproducir_secuencia(secuencia, indice + 1))