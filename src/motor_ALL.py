from automata.tm.dtm import DTM
#tm: Turing Machine, dtm: Deterministic Turing Machine  

class MaquinaTuring:
    def __init__(self):
        # Definimos el automta linealmente litado con la librería
        self.all = DTM(
            states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12'},
            input_symbols={'v', 'a', 'n', 'z', '#', '<', '>'},
            tape_symbols={'v', 'a', 'n', 'z', '#', '<', '>', 'X', '_'},
            transitions={
                    'q0': {                     
                        'v': ('q1', 'X', 'R'),
                        'a': ('q4', 'X', 'R'),
                        'n': ('q6', 'X', 'R'),
                        'z': ('q8', 'X', 'R'),
                        '#': ('q10', '#', 'R'),
                        'X': ('q0', 'X', 'R'),
                        '<': ('q0', '<', 'R')
                    },
                    'q1': {                     
                        'v': ('q1', 'v', 'R'),
                        'a': ('q1', 'a', 'R'),
                        'n': ('q1', 'n', 'R'),
                        'z': ('q1', 'z', 'R'),
                        '#': ('q2', '#', 'R')
                    },
                    'q2': {                     
                        'v': ('q3', 'X', 'L'),
                        'X': ('q2', 'X', 'R'),
                        '>': ('q12', '>', 'N')
                    },
                    'q3': {                      
                        'v': ('q3', 'v', 'L'),
                        'a': ('q3', 'a', 'L'),
                        'n': ('q3', 'n', 'L'),
                        'z': ('q3', 'z', 'L'),
                        '#': ('q3', '#', 'L'),
                        'X': ('q3', 'X', 'L'),
                        '<': ('q0', '<', 'R')
                    },
                    'q4': {                     
                        'v': ('q4', 'v', 'R'),
                        'a': ('q4', 'a', 'R'),
                        'n': ('q4', 'n', 'R'),
                        'z': ('q4', 'z', 'R'),
                        '#': ('q5', '#', 'R')
                    },
                    'q5': {                     
                        'a': ('q3', 'X', 'L'),
                        'X': ('q5', 'X', 'R'),
                        '>': ('q12', '>', 'N')
                    },
                    'q6': {                     
                        'v': ('q6', 'v', 'R'),
                        'a': ('q6', 'a', 'R'),
                        'n': ('q6', 'n', 'R'),
                        'z': ('q6', 'z', 'R'),
                        '#': ('q7', '#', 'R')
                    },
                    'q7': {                      
                        'n': ('q3', 'X', 'L'),
                        'X': ('q7', 'X', 'R'),
                        '>': ('q12', '>', 'N')
                    },
                    'q8': {                      
                        'v': ('q8', 'v', 'R'),
                        'a': ('q8', 'a', 'R'),
                        'n': ('q8', 'n', 'R'),
                        'z': ('q8', 'z', 'R'),
                        '#': ('q9', '#', 'R')
                    },
                    'q9': {                      
                        'z': ('q3', 'X', 'L'),
                        'X': ('q9', 'X', 'R'),
                        '>': ('q12', '>', 'N')
                    },
                    'q10': {                     
                        'X': ('q10', 'X', 'R'),
                        '>': ('q11', '>', 'N')
                    }
                        
            },
            initial_state='q0',
            blank_symbol='_',
            final_states={'q11'}
        )

    def evaluar_secuencia(self,secuencia_maestra ,secuencia_actual):
        # Preparamos la cinta para el ALL
        cinta = '<' + secuencia_maestra + '#' + secuencia_actual + '>'
        ultima = None
        try:
            for configuracion in self.all.read_input_stepwise(cinta):
                ultima = configuracion
        except Exception:
            pass   

      
        salidas = {'q11': 'G', 'q12': 'B'}
        return salidas.get(ultima.state, 'P') 