from .cellular_automaton import CellularAutomaton
import matplotlib.pyplot as plt
import numpy as np
import csv

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

    data_i = np.empty(n_iterations+1)
    data_s = np.empty(n_iterations+1)
    data_r = np.empty(n_iterations+1)

    ca = CellularAutomaton(height, width, p_cure,
                           p_death_disease, p_death_other, beta)

    while(current_iteration <= n_iterations):
        print('t =', current_iteration)
        i_count, s_count, r_count = ca.stats()
        data_i[current_iteration] = i_count
        data_s[current_iteration] = s_count
        data_r[current_iteration] = r_count
        ca.step()
        current_iteration += 1

    plot_stats(data_i, data_s, data_r, n_iterations, width * height)

    csv_path = './epydemic/data/melotti_cenario1_sdelocamento.csv'
    with open(csv_path, newline='\n') as csvfile:
        matlab_data = csv.reader(csvfile)
        matlab_data_i = np.empty(n_iterations+1)
        matlab_data_s = np.empty(n_iterations+1)
        matlab_data_r = np.empty(n_iterations+1)
        for row in matlab_data:
            iteration, i_count, s_count, r_count = row
            matlab_data_i[int(iteration)] = int(i_count)
            matlab_data_s[int(iteration)] = int(s_count)
            matlab_data_r[int(iteration)] = int(r_count)

    res_i = data_i - matlab_data_i
    res_s = data_s - matlab_data_s
    res_r = data_r - matlab_data_r

    plot_stats(res_i, res_s, res_r, n_iterations, width * height)


def plot_stats(data_i, data_s, data_r, n_iterations, n_individuals):
    t = range(0, len(data_i))
    plt.plot(t, data_i, 'k--', label='Infected')
    plt.plot(t, data_r, 'k:', label='Recovered')
    plt.plot(t, data_s, 'k', label='Susceptible')
    plt.legend(loc='upper right')
    plt.ylabel('Individuals')
    plt.xlabel('Time')
    plt.xlim(0, n_iterations)
    plt.ylim(0, n_individuals)
    plt.show()


if __name__ == '__main__':
    main()
