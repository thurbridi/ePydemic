from .cellular_automaton import CellularAutomaton
import matplotlib.pyplot as plt

# Simulation flow and configuration


def main():
    n_iterations = 100
    current_iteration = 0

    width = 200
    height = 200
    p_cure = 0.6
    p_death_disease = 0.3
    p_death_other = 0.1
    beta = 3.5  # beta

    data_i = []
    data_s = []
    data_r = []

    ca = CellularAutomaton(height, width, p_cure,
                           p_death_disease, p_death_other, beta)

    while(current_iteration < n_iterations):
        print('t =', current_iteration)
        i_count, s_count, r_count = ca.stats()
        data_i.append(i_count)
        data_s.append(s_count)
        data_r.append(r_count)
        ca.step()
        current_iteration += 1

    plot_stats(data_i, data_s, data_r, n_iterations, width * height)


def plot_stats(data_i, data_s, data_r, n_iterations, n_individuals):
    t = range(0, len(data_i))
    plt.plot(t, data_i, 'k--', label='Infected')
    plt.plot(t, data_r, 'k:', label='Recovered')
    plt.plot(t, data_s, 'k', label='Susceptible')
    plt.legend(loc='upper right')
    plt.ylabel('Individuals')
    plt.xlabel('Time')
    plt.axes([0, n_iterations, 0, n_individuals])
    plt.show()


if __name__ == '__main__':
    main()
