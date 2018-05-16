from cellular_automaton import Cellular_Automaton

# Simulation flow and configuration


def main():
    n_iterations = 0
    current_iteration = 0
    width = 200
    height = 200
    ca = Cellular_Automaton(height, width)

    while(current_iteration < n_iterations):
        ca.stats()
        ca.step()
        current_iteration += 1


if __name__ == '__main__':
    main()
