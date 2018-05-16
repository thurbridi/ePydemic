from .lattice import Lattice
import numpy as np
import math as m

INFECTED = 0
SUSCEPTIBLE = 1
RECOVERED = 2


class CellularAutomaton:
    def __init__(self, height=200, width=200, p_cure=0.6, p_death_disease=0.3,
                 p_death_other=0.1, beta=3.5, d_max=200):
        self.height = height
        self.width = width
        self.total_people = height * width

        self.p_cure = p_cure
        self.p_death_disease = p_death_disease
        self.p_death_other = p_death_other
        self.beta = beta  # beta
        self.d_max = d_max

        self.lattice = self.init_lattice(height, width)

    # Step forward 1 time unit
    def step(self):
        aux = Lattice(self.height, self.width)

        for i in range(0, self.height):
            for j in range(0, self.width):
                aux[i, j] = self.apply_ruleset(i, j)

        self.lattice.grid = aux.grid[:, :]

    # Return statistics from the current state
    def stats(self):
        i_count = 0
        r_count = 0
        s_count = 0

        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.lattice[i, j] == INFECTED:
                    i_count += 1
                if self.lattice[i, j] == RECOVERED:
                    r_count += 1
                if self.lattice[i, j] == SUSCEPTIBLE:
                    s_count += 1

        return i_count, s_count, r_count

    # Apply the ruleset on a cell and returns the result
    def apply_ruleset(self, i, j):
        i_count, s_count, r_count = self.count_neighbors(i, j)
        outcome = self.lattice[i, j]

        # Local infection
        Pi = (self.beta * i_count) / 8
        Prand_s = np.random.rand()
        if self.lattice[i, j] == SUSCEPTIBLE and Prand_s <= Pi:
            outcome = INFECTED

        # Non-local infection

        # Recovery
        Prand_ic = np.random.rand()
        if self.lattice[i, j] == INFECTED and Prand_ic <= self.p_cure:
            outcome = RECOVERED

        # Death by disease
        Prand_im = np.random.rand()
        if self.lattice[i, j] == INFECTED and Prand_im <= self.p_death_disease:
            outcome = SUSCEPTIBLE

        # Death by other
        p1 = np.random.rand()
        if p1 <= self.p_death_other:
            outcome = SUSCEPTIBLE

        return outcome

    def count_neighbors(self, i, j):
        i_count = 0
        s_count = 0
        r_count = 0

        for y in range(i-1, i+2):
            for x in range(j-1, j+2):
                if (x == j and y == i):
                    continue
                if self.lattice[x, y] == INFECTED:
                    i_count += 1
                if self.lattice[x, y] == SUSCEPTIBLE:
                    s_count += 1
                if self.lattice[x, y] == RECOVERED:
                    r_count += 1

        return i_count, s_count, r_count

    # Creates inital lattice with random infected
    def init_lattice(self, height, width):
        lattice = Lattice(height, width)
        pa = np.random.permutation(self.total_people)
        I0 = m.floor(0.005 * self.total_people)
        lattice[pa[:I0]] = 0

        return lattice

    def __str__(self):
        return self.lattice.__str__()
