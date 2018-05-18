import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_r = ctrl.Antecedent(np.arange(0, 8.1, 0.1), 'R_0')
x_p = ctrl.Antecedent(np.arange(0, 1.001, 0.001), 'P_nl')
x_l = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'L')

x_r['very low'] = fuzz.trapmf(x_r.universe, [0, 0, 0.1, 1.9])
x_r['low'] = fuzz.trapmf(x_r.universe, [0.1, 1.9, 2.1, 3.9])
x_r['median'] = fuzz.trapmf(x_r.universe, [2.1, 3.9, 4.1, 5.9])
x_r['high'] = fuzz.trapmf(x_r.universe, [4.1, 5.9, 6.1, 7.9])
x_r['very high'] = fuzz.trapmf(x_r.universe, [6.1, 7.9, 8, 8])

x_p['very low'] = fuzz.trapmf(x_p.universe, [0, 0, 0.025, 0.225])
x_p['low'] = fuzz.trapmf(x_p.universe, [0.025, 0.225, 0.275, 0.475])
x_p['median'] = fuzz.trapmf(x_p.universe, [0.275, 0.475, 0.525, 0.725])
x_p['high'] = fuzz.trapmf(x_p.universe, [0.525, 0.725, 0.775, 0.975])
x_p['very high'] = fuzz.trapmf(x_p.universe, [0.775, 0.975, 1, 1])

x_l['small'] = fuzz.trapmf(x_l.universe, [0, 0, 0.05, 0.45])
x_l['median'] = fuzz.trapmf(x_l.universe, [0.05, 0.45, 0.55, 0.95])
x_l['big'] = fuzz.trapmf(x_l.universe, [0.55, 0.95, 1, 1])

rules = []
rules.append(ctrl.Rule(x_r['very low'] & x_p['very low'], x_l['small']))
rules.append(ctrl.Rule(x_r['very low'] & x_p['low'], x_l['small']))
rules.append(ctrl.Rule(x_r['very low'] & x_p['median'], x_l['small']))
rules.append(ctrl.Rule(x_r['very low'] & x_p['high'], x_l['median']))
rules.append(ctrl.Rule(x_r['very low'] & x_p['very high'], x_l['median']))

rules.append(ctrl.Rule(x_r['low'] & x_p['very low'], x_l['small']))
rules.append(ctrl.Rule(x_r['low'] & x_p['low'], x_l['small']))
rules.append(ctrl.Rule(x_r['low'] & x_p['median'], x_l['median']))
rules.append(ctrl.Rule(x_r['low'] & x_p['high'], x_l['median']))
rules.append(ctrl.Rule(x_r['low'] & x_p['very high'], x_l['big']))

rules.append(ctrl.Rule(x_r['median'] & x_p['very low'], x_l['small']))
rules.append(ctrl.Rule(x_r['median'] & x_p['low'], x_l['small']))
rules.append(ctrl.Rule(x_r['median'] & x_p['median'], x_l['median']))
rules.append(ctrl.Rule(x_r['median'] & x_p['high'], x_l['big']))
rules.append(ctrl.Rule(x_r['median'] & x_p['very high'], x_l['big']))

rules.append(ctrl.Rule(x_r['high'] & x_p['very low'], x_l['small']))
rules.append(ctrl.Rule(x_r['high'] & x_p['low'], x_l['median']))
rules.append(ctrl.Rule(x_r['high'] & x_p['median'], x_l['median']))
rules.append(ctrl.Rule(x_r['high'] & x_p['high'], x_l['big']))
rules.append(ctrl.Rule(x_r['high'] & x_p['very high'], x_l['big']))

rules.append(ctrl.Rule(x_r['very high'] & x_p['very low'], x_l['median']))
rules.append(ctrl.Rule(x_r['very high'] & x_p['low'], x_l['median']))
rules.append(ctrl.Rule(x_r['very high'] & x_p['median'], x_l['big']))
rules.append(ctrl.Rule(x_r['very high'] & x_p['high'], x_l['big']))
rules.append(ctrl.Rule(x_r['very high'] & x_p['very high'], x_l['big']))

displacement_ctrl = ctrl.ControlSystem(rules)
sim = ctrl.ControlSystemSimulation(displacement_ctrl)


def eval_fuzz(r0, pnl):
    sim.input['R_0'] = r0
    sim.input['P_nl'] = pnl
    sim.compute()
    return sim.output['L']


# Fuzzy output plot
# x, y = np.meshgrid(np.linspace(0, 8, 20), np.linspace(0, 1, 20))
# z = np.zeros_like(x)

# for i in range(20):
#     for j in range(20):
#         sim.input['R_0'] = x[i, j]
#         sim.input['P_nl'] = y[i, j]
#         sim.compute()
#         z[i, j] = sim.output['L']

# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(111, projection='3d')

# surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis',
#                        linewidth=0.4, antialiased=True)

# cset = ax.contourf(x, y, z, zdir='z', offset=0.1, cmap='viridis', alpha=0.5)
# cset = ax.contourf(x, y, z, zdir='x', offset=9, cmap='viridis', alpha=0.5)
# cset = ax.contourf(x, y, z, zdir='y', offset=1.1, cmap='viridis', alpha=0.5)

# ax.view_init(30, 200)
# plt.show()
