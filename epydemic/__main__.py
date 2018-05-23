import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QAction, qApp, QFormLayout, QVBoxLayout,
    QHBoxLayout, QTabWidget, QWidget, QSizePolicy
)
from PyQt5 import uic

import matplotlib.pyplot as plt
from .cellular_automaton import CellularAutomaton
import numpy as np
import threading


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('./epydemic/forms/ePydemic.ui', self)

        self.button_simulate.clicked.connect(self.worker)

        self.show()

    def worker(self):
        thread = threading.Thread(target=self.start_simulation, daemon=True)
        self.button_simulate.setEnabled(False)
        thread.start()

    def start_simulation(self):
        current_iteration = 0
        n_iterations = int(self.form_n_iterations.text())

        height = int(self.form_height.text())
        width = int(self.form_width.text())
        p_cure = float(self.form_p_cure.text())
        p_death_disease = float(self.form_p_death_disease.text())
        p_death_other = float(self.form_p_death_other.text())
        beta = float(self.form_beta.text())
        d_max = 200

        ca = CellularAutomaton(
            height=height,
            width=width,
            p_cure=p_cure,
            p_death_disease=p_death_disease,
            p_death_other=p_death_other,
            beta=beta,
            d_max=200
        )

        data_i = np.empty(n_iterations+1)
        data_s = np.empty(n_iterations+1)
        data_r = np.empty(n_iterations+1)

        while(current_iteration <= n_iterations):
            self.statusBar().showMessage(
                f"STATUS: RUNNING | t={current_iteration}")

            i_count, s_count, r_count = ca.stats()
            data_i[current_iteration] = i_count
            data_s[current_iteration] = s_count
            data_r[current_iteration] = r_count

            ca.step()
            current_iteration += 1

        self.statusBar().showMessage(
            f"STATUS: RUN COMPLETE | t={current_iteration-1}")
        self.plot_stats(data_i, data_s, data_r, n_iterations, width * height)
        self.button_simulate.setEnabled(True)

    def plot_stats(self, data_i, data_s, data_r, n_iterations, n_individuals):
        t = range(0, len(data_i))

        plt.ticklabel_format(style='sci', scilimits=(0, 3), useMathText=True)
        plt.title('Number of individuals')
        plt.plot(t, data_i, 'k--', label='Infected')
        plt.plot(t, data_r, 'k:', label='Recovered')
        plt.plot(t, data_s, 'k', label='Susceptible')
        plt.legend(loc='upper right')
        plt.ylabel('Individuals')
        plt.xlabel('Time')
        plt.xlim(0, n_iterations)
        plt.ylim(0, n_individuals)

        plt.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
