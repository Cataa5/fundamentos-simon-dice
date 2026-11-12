from automata.pda.dpda import DPDA
#pda: Pushdown Automaton, dpda: Deterministic Pushdown Automaton 

class AutomataPila:
    def __init__(self):
        colores = {'v': 'V', 'a': 'A', 'n': 'N', 'z': 'Z'}
        simbolos_pila = {'V', 'A', 'N', 'Z', '#'}
        
        transitions = {
            'q0': {},
            'q1': {},
            'q2': {}
        }
        
        # Estado q0: Apila la secuencia mostrada
        for c_in, c_stack in colores.items():
            transitions['q0'][c_in] = {}
            for s in simbolos_pila:
                transitions['q0'][c_in][s] = ('q0', (c_stack, s))
        
        # Transición del separador '#' en q0 hacia q1
        transitions['q0']['#'] = {}
        for s in simbolos_pila:
            transitions['q0']['#'][s] = ('q1', (s,))
            
        # Estado q1: Desapila en orden LIFO
        for c_in, c_stack in colores.items():
            transitions['q1'][c_in] = {
                c_stack: ('q1', '')
            }
            
        # Transición épsilon/lambda ('') en q1: al quedar fondo '#', pasa a q2
        transitions['q1'][''] = {
            '#': ('q2', ('#',))
        }

        self.ap = DPDA(
            states={'q0', 'q1', 'q2'},
            input_symbols={'v', 'a', 'n', 'z', '#'},
            stack_symbols=simbolos_pila,
            transitions=transitions,
            initial_state='q0',
            initial_stack_symbol='#',
            final_states={'q1', 'q2'},
            acceptance_mode='final_state'
        )

    def evaluar_secuencia(self, secuencia_maestra, secuencia_actual):
        cinta = secuencia_maestra + '#' + secuencia_actual
        ultima_config = None
        try:
            for configuracion in self.ap.read_input_stepwise(cinta):
                ultima_config = configuracion
        except Exception:
            return 'P'

        if len(ultima_config.stack) == 1:   # pila vacía (solo queda '#') -> aceptó de verdad
            return 'G'
        return 'B'