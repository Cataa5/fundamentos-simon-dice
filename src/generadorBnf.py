import random

class BnfGeneradorSecuencias:
    def __init__(self):

        self.colores_terminales = ['v','a', 'n', 'z']

    def generar_secuencia(self, longitud: int = 5) -> str:
        if longitud <= 0:
            return ""

        secuencia_lista = []
        for _ in range(longitud):
            color_elegido = random.choice(self.colores_terminales)
            secuencia_lista.append(color_elegido)

        return "".join(secuencia_lista)

    def generar_secuencia_con_separador(self, longitud: int = 5) -> str:
        colores = [random.choice(self.colores_terminales) for _ in range(longitud)]
        return ",".join(colores)