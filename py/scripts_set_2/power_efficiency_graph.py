import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


pd.set_option('display.max_columns', 30)


def read_file(path):
  data = pd.read_csv(path)
  df = pd.DataFrame(data)
  return df


path = '/Users/nathanoliver/Desktop/Python/Github/Masirah Island/csv/data_set_2/wind_site_power_efficiency.csv'


df = read_file(path)


print(df.columns)

power_col = ['E33_power_output', 'E44_power_output',
             'E48_power_output', 'E53_power_output', 'E70_power_output',
             'E82_power_output']
eff_col = ['E33_efficiency', 'E44_efficiency',
           'E48_efficiency', 'E53_efficiency', 'E70_efficiency', 'E82_efficiency']


print(df.sum(axis='index') / len(df))

# eff = [0.358052,
#        0.370269,
#        0.393586,
#        0.378945,
#        0.345958,
#        0.351483]

eff = [0.305461,
       0.352550,
       0.379906,
       0.357742,
       0.315994,
       0.317587]

ann_cost = [341116.6667 * .67,
            350862.8571 * .67,
            409340 * .67,
            614010 * .67,
            852791.6667 * .67,
            1057461.667 * .67]

# power = [57.188268,
#          104.398368,
#          124.271234,
#          144.041908,
#          269.229874,
#          346.331948]

power = [64.965598,
         132.152088,
         146.077424,
         162.061159,
         342.959486,
         396.804204]

energy = []
coe = []

for i in range(len(power)):
  energy.append(power[i] * 8760 / 1e6)
  coe.append(ann_cost[i] / (energy[i] * 1e6))


tur = ['E33', 'E44', 'E48', 'E53', 'E70', 'E82']

print('Turbine  COE     Energy (GWh)')
for i in range(len(power)):

  print(tur[i],    coe[i],  energy[i])

# colors = ['#c4e6c3', '#96d2a4', '#6dbc90',
#           '#4da284', '#36877a', '#266b6e']

colors = ['#e15759', '#f28e2b', '#edc948',
          '#59a14f', '#76b7b2', '#4e79a7', '#b07aa1']


fig, axes = plt.subplots(2, 2, sharex=True, figsize=(20, 8))

ax1, ax2, ax3, ax4 = axes.flatten()


ax1.bar(tur, energy, color=colors)
ax1.set_title('Yearly Energy Production on Masirah Island')
# ax2.set_xlabel('Enercon Turbine Model')
ax1.set_ylabel('Energy Production\n(GWh/yr)')

ax2.bar(tur, eff, color=colors)
ax2.set_title('Turbine Efficiencies on Masirah Island')
# ax3.set_xlabel('Enercon Turbine Model')
ax2.set_ylabel('Efficiency (%)')

ax3.bar(tur, ann_cost, color=colors)
ax3.set_title('Annualized Cost')
ax3.set_xlabel('Enercon Turbine Model')
ax3.set_ylabel('Annualized Cost\n($/yr)')


ax4.bar(tur, coe, color=colors)
ax4.set_title('Turbine COE')
ax4.set_xlabel('Enercon Turbine Model')
ax4.set_ylabel('COE ($)')

title = 'Enercon Candidate Turbine Perforamce on Masirah Island'

fig.suptitle(title, fontsize=20)

# fig.tight_layout()
plt.show()


# print(df.sum(axis='index'))

# print(4.535900e+04 * 365)

print('energy', energy)


E48_new_energy = 1.08861600984e6
E48_old_energy = 1899594

E48_new_eff = .393586
E48_old_eff = .377

new_ratio = E48_new_eff / E48_new_energy
old_ratio = E48_old_eff / E48_old_energy

# print(new_ratio, old_ratio)
# print(1 / (new_ratio / old_ratio))
