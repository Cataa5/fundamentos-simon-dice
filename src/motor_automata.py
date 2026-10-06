from automata.fa.dfa import DFA
#fa: Finite Automata, dfa: Deterministic Finite Automata

class AutomataSimonDice:
   
    def __init__(self):
        # Definimos el autómata con la librería
        self.dfa = DFA(
            states={'q0', 'q1', 'q2', 'q_win', 'q_lose'}, # ESTADOS PRUEBA
            input_symbols={'v', 'a', 'n', 'z'}, #ALFABETO: violeta, amarillo, naranja, azul
            transitions={ #transiciones
                'q0': {'v': 'q1', 'a': 'q_lose', 'n': 'q_lose', 'z': 'q_lose'},
                'q1': {'v': 'q_lose', 'a': 'q2', 'n': 'q_lose', 'z': 'q_lose'},
                'q2': {'v': 'q_lose', 'a': 'q_lose', 'n': 'q_win', 'z': 'q_lose'},
                'q_win': {'v': 'q_win', 'a': 'q_win', 'n': 'q_win', 'z': 'q_win'},
                'q_lose': {'v': 'q_lose', 'a': 'q_lose', 'n': 'q_lose', 'z': 'q_lose'}
            },
            initial_state='q0',
            final_states={'q0','q1','q2','q_win','q_lose'}
        )
        
        # ESTADOS/SALIDAS
        self.salidas = {
            'q0': 'I',
            'q1': 'B',
            'q2': 'B',
            'q_win': 'G',
            'q_lose': 'P'
        }

    def evaluar_secuencia(self, secuencia_actual):
        # read_input en qué estado cayó
        estado_alcanzado = self.dfa.read_input(secuencia_actual)
        # retornamos la salida asociada a ese estado
        return self.salidas[estado_alcanzado]


    #states={'q0', 'q1', 'q2','q3','q4','q5','q6','q7', 'q_win', 'q_lose'}, # ESTADO DEL PDF
    #'q2': {'v': 'q_lose', 'a': 'q3', 'n': 'q_lose', 'z': 'q_lose'}, # ESTADOS DEL PDF
    #'q3': {'v': 'q_lose', 'a': 'q4', 'n': 'q_lose', 'z': 'q_lose'},
    #'q4': {'v': 'q5', 'a': 'q_lose', 'n': 'q_lose', 'z': 'q_lose'},
    #'q5': {'v': 'q_lose', 'a': 'q_lose', 'n': 'q_lose', 'z': 'q6'},
    #'q6': {'v': 'q_lose', 'a': 'q_lose', 'n': 'q7', 'z': 'q_lose'},
    #'q7': {'v': 'q_lose', 'a': 'q_win', 'n': 'q_lose', 'z': 'q_lose'},
    #'q_win': {'v': 'q_win', 'a': 'q_win', 'n': 'q_win', 'z': 'q_win'},
    # 'q1': {'v': 'q_lose', 'a': 'q2', 'n': 'q_lose', 'z': 'q_lose'},