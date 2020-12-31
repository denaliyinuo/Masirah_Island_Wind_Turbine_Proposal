import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_file(path):
  data = pd.read_csv(path)
  df = pd.DataFrame(data)
  return df


path = '/Users/nathanoliver/Desktop/Python/Github/Masirah Island/csv/data_set_2/turbine_power_coefficients.csv'

df = read_file(path)

print(df.columns)

col1 = ['E33_power', 'E44_power', 'E48_power', 'E53_power', 'E70_power',
        'E82_power']
col2 = ['E33_efficiency', 'E44_efficiency', 'E48_efficiency',
        'E53_efficiency', 'E70_efficiency', 'E82_efficiency']

col3 = ['E33', 'E44', 'E48', 'E53', 'E70', 'E82']

# colors = ['#c4e6c3', '#96d2a4', '#6dbc90',
#           '#4da284', '#36877a', '#266b6e', '#1d4f60']

colors = ['#e15759', '#f28e2b', '#edc948',
          '#59a14f', '#76b7b2', '#4e79a7', '#b07aa1']

fig, ax1 = plt.subplots(1, 1, sharex=True, figsize=(10, 5))

for i in range(len(col1)):
  ax1.plot(df['wind_speed'], df[col1[i]],
           label=col3[i], marker='o', color=colors[i])
  ax1.legend()
  ax1.set_xlim(-1, 26)
  ax1.set_ylim(-50, 2500)

# for i in range(len(col2)):
#   ax2.plot(df['wind_speed'], df[col2[i]], label=col3[i],
#            marker='o', color=colors[i])
#   ax2.legend()

ax1.set_title('Enercon Candidate Wind Turbine\nPower Curves')
ax1.set_xlabel('Wind Speed (m/s)')
ax1.set_ylabel('Power (kW)')

plt.show()


# # plot with power curve and efficiency curve

# fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True)

# for i in range(len(col1)):
#   ax1.plot(df['wind_speed'], df[col1[i]],
#            label=col3[i], marker='o', color=colors[i])
#   ax1.legend()
#   ax1.set_xlim(-1, 26)
#   ax1.set_ylim(-50, 2500)

# for i in range(len(col2)):
#   ax2.plot(df['wind_speed'], df[col2[i]], label=col3[i],
#            marker='o', color=colors[i])
#   ax2.legend()

# plt.show()
