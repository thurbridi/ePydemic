from lattice import Lattice
import numpy as np
import math as m

cell_state = {
    'infected':    0,
    'susceptible': 1,
    'recovered':   2
}


class Cellular_Automaton:
    def __init__(self, height=200, width=200):
        self.total_people = height * width

        self.p_cure = 0.6
        self.p_death_disease = 0.3
        self.p_death_other = 0.1
        self.infectiousness = 3.5  # beta

        self.lattice = self.init_lattice(height, width)

    # Step forward 1 time unit
    def step(self):
        ...

    # Return statistics from the current state
    def stats(self):
        ...

    # Apply the ruleset on a cell
    def apply_ruleset(self, x, y):
        ...

    # Creates inital lattice with random infected
    def init_lattice(self, height, width):
        lattice = Lattice(height, width)
        pa = np.random.permutation(self.total_people)
        I0 = m.floor(0.005 * self.total_people)
        lattice[pa[:I0]] = 0

        return lattice
