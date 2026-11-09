import tkinter as tk
from motor_ALL import MaquinaTuring
from interfazInicio import VistaInicioSimonDice
from interfazPartida import VistaSimonDice

class ControladorSimonDice:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Simón Dice - Autómatas")
        self.motor = MaquinaTuring()
        self.secuencia_actual = ""
        self.estado_juego = "ESPERANDO"
        self.secuencia_maestra = "zznaa" # Secuencia PRUEBA 
        
        self.mostrar_menu()

    def mostrar_menu(self):
        # Limpiamos la ventana completa por las dudas
        for widget in self.ventana.winfo_children():
            widget.destroy()
            
        # Instanciamos el menú pasándole las funciones para los botones
        self.vista_menu = VistaInicioSimonDice(self.ventana, self.iniciar_partida, self.ventana.quit)

    def iniciar_partida(self):
        # Limpiamos los widgets del menú de inicio
        for widget in self.ventana.winfo_children():
            widget.destroy()
            
        # Instanciamos la vista de la partida
        self.vista = VistaSimonDice(self.ventana, self.procesar_color, self.reiniciar_juego, self.mostrar_menu)
        
        self.secuencia_actual = ""
        self.estado_juego = "ESPERANDO"
        
        self.ventana.after(300, lambda: self.vista.reproducir_secuencia(self.secuencia_maestra))

    def procesar_color(self, color):
        if self.estado_juego in ["G", "P"]:
            self.reiniciar_juego()
            return

        self.secuencia_actual += color
        resultado = self.motor.evaluar_secuencia(self.secuencia_maestra, self.secuencia_actual)
        self.estado_juego = resultado
        
        if resultado == "P":
            self.vista.mostrar_derrota()
        elif resultado == "G":
            self.vista.mostrar_victoria()
        elif resultado == "B":
            self.vista.mostrar_acierto()

    def reiniciar_juego(self):
        self.secuencia_actual = ""
        self.estado_juego = "ESPERANDO"
        self.vista.reiniciar_interfaz()
        
        self.ventana.after(500, lambda: self.vista.reproducir_secuencia(self.secuencia_maestra))

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = ControladorSimonDice()
    app.iniciar()