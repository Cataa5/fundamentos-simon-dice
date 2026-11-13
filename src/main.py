import tkinter as tk
from motor_ALL import MaquinaTuring
from motor_AP import AutomataPila
from interfazJugar import VistaJugarSimonDice
from interfazInicio import VistaInicioSimonDice
from interfazPartida import VistaSimonDice

class ControladorSimonDice:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Simón Dice - Autómatas")
        self.motor_all = MaquinaTuring()
        self.motor_ap = AutomataPila()

        self.secuencia_actual = ""
        self.estado_juego = "ESPERANDO"
        self.modo_juego = "NORMAL"
        self.secuencia_maestra = "vvnaz" # Secuencia PRUEBA
        
        self.mostrar_menu()

    def transicion_pestaneo(self, callback_cambio_vista):
        """Crea un frame negro sobre toda la pantalla simulando un parpadeo rápido."""
        overlay = tk.Frame(self.ventana, bg="black")
        overlay.place(x=0, y=0, relwidth=1, relheight=1)
        overlay.lift()  # Se asegura de quedar sobre todo

        def ejecutar_cambio():
            # Limpiamos todos los widgets de la ventana excepto el overlay de transición
            for widget in self.ventana.winfo_children():
                if widget != overlay:
                    widget.destroy()

            # Cambio de pantalla 
            callback_cambio_vista()
            
            # Overlay arriba brevemente en la nueva vista y lo destruimos
            overlay.lift()
            self.ventana.after(140, overlay.destroy)

        # Espera 100ms con la pantalla en negro (ojo cerrado) antes de cargar la vista
        self.ventana.after(100, ejecutar_cambio)
    
    def mostrar_menu(self):
        def _cambiar():                
            # Instanciamos el menú 
            self.vista_menu = VistaInicioSimonDice(self.ventana, self.mostrar_jugar, self.ventana.quit)

        self.transicion_pestaneo(_cambiar)

    def mostrar_jugar(self):
        def _cambiar():
            self.vista_menu = VistaJugarSimonDice(self.ventana, self.iniciar_partida, self.iniciar_partida_reverso, self.mostrar_menu)

        self.transicion_pestaneo(_cambiar)

    
    def iniciar_partida(self):
        self.modo_juego = "NORMAL"
        def _cambiar():                
            # Instanciamos la vista de la partida
            self.vista = VistaSimonDice(self.ventana, self.procesar_color, self.reiniciar_juego, self.mostrar_menu, modo="NORMAL")
            
            self.secuencia_actual = ""
            self.estado_juego = "ESPERANDO"
            
            self.ventana.after(500, lambda: self.vista.reproducir_secuencia(self.secuencia_maestra))

        self.transicion_pestaneo(_cambiar)

    def iniciar_partida_reverso(self):
        self.modo_juego = "REVERSO"
        def _cambiar():
            # Instanciamos la vista de la partida
            self.vista = VistaSimonDice(self.ventana, self.procesar_color, self.reiniciar_juego, self.mostrar_menu, modo="REVERSO")
            self.secuencia_actual = ""
            self.estado_juego = "ESPERANDO"
            self.ventana.after(500, lambda: self.vista.reproducir_secuencia(self.secuencia_maestra))

        self.transicion_pestaneo(_cambiar)

    
    def procesar_color(self, color):
        if self.estado_juego in ["G", "P"]:
            self.reiniciar_juego()
            return

        self.secuencia_actual += color

        if self.modo_juego == "NORMAL":
            resultado = self.motor_all.evaluar_secuencia(self.secuencia_maestra, self.secuencia_actual)
        else:
            resultado = self.motor_ap.evaluar_secuencia(self.secuencia_maestra, self.secuencia_actual)

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