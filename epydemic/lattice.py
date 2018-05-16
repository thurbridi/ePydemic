import numpy as np

np.set_printoptions(threshold=np.nan)


class Lattice():
    def __init__(self, height=200, width=200):
        self.height = height
        self.width = width
        self.grid = np.ones((height, width), np.int8)

    def __getitem__(self, index):
        x, y = index
        return self.grid[x % self.width, y % self.height]

    def __setitem__(self, index, value):
        if (type(index) is (np.ndarray or list)):
            aux = np.reshape(self.grid, (self.height * self.width, 1))

            for i in index:
                aux[i] = value
            aux = np.reshape(aux, (self.height, self.width))
            self.grid = aux

        else:
            x, y = index
            self.grid[x % self.width, y % self.height] = value

    def __str__(self):
        return self.grid.__str__()
