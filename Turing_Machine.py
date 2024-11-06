class Turing_Machine():
    def __init__(self, cinta, inital_state, final_state, transitions):
        self.cinta = list(cinta)
        self.head = 0
        self.state = inital_state
        self.final_state = final_state
        self.transitions = transitions
        self.errror_ocurred = False

    def movements(self):

        if self.head < 0 or self.head >= len(self.cinta):
            print('El cabezal esta fuera de los limites')
            return False
        
        current_symbol = self.cinta[self.head]
        if (self.state, current_symbol) in self.transitions:
            new_symbol, move, new_state = self.transitions[(self.state, current_symbol)]
            self.cinta[self.head] = new_symbol
            self.state = new_state

            if move == 'R':
                self.head += 1
            elif move == 'L':
                self.head -= 1

            if self.head >= len(self.cinta):
                self.cinta.append(' ')

            return True
        
        else:
            self.errror_ocurred = True
            return False
        

    def run(self):
        while self.state != self.final_state:
            if not self.movements():
                break

    def is_valid(self):
        if self.state in self.final_state:
            print("La cinta final es: ", ''.join(self.cinta))
            return ' '.join(self.cinta).strip()
        else: 
            if self.errror_ocurred:
               print("Error de transicion: El estado", self.state, "no tiene una transicion para el simbolo", self.cinta[self.head])
               return False
        return False