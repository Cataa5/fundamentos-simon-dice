class BnfSecuenciaParser:
    def __init__(self, entrada: str):
        self.entrada = entrada.strip()
        self.cursor = 0

    def validar(self) -> bool:
        
        if not self.entrada:
            return False
        self.cursor = 0
        resultado = self._parse_secuencia()
        return resultado and self.cursor == len(self.entrada)

    def _parse_secuencia(self) -> bool:
        # aca deberiamos modificar si tenemos mas reglas sobre las secuencias
        if not self._parse_color():
            return False
        
        while self.cursor < len(self.entrada):
            if not self._parse_color():
                return False
        return True

    def _parse_color(self) -> bool:
        # <Color> ::= "v" | "a" | "n" | "z"
        if self.cursor >= len(self.entrada):
            return False
        
        simbolo = self.entrada[self.entrada_cursor_seguro() if hasattr(self, 'entrada_cursor_seguro') else self.cursor] 
        simbolo = self.entrada[self.cursor]
        if simbolo in {'v', 'a', 'n', 'z'}:
            self.cursor += 1
            return True
        return False