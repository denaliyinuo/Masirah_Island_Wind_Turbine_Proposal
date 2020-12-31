import pandas as pd
import matplotlib.pyplot as plt
import math
import statistics


def read_file(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df


path = '/Users/nathanoliver/Desktop/Python/Github/Masirah Island/csv/data_set_2/wind_speed.csv'

df = read_file(path)

print(df.columns)

avg = sum(df['wind_speed']) / len(df)

print(df['wind_speed'])

standard = statistics.stdev((df['wind_speed']))


k = (standard / avg)**(-1.086)

print(standard, avg, k)

c = 5.34

x = []
y = []


for i in range(-10, 10):
    math.exp(i)

for v in range(0, 240):

    v = v / 10
    x.append(v)
    ex = math.exp((-(v / c)**k))
    y.append((k / c) * (v / c)**(k - 1) * ex)

fig, ax = plt.subplots(figsize=(10, 5))

kwargs = dict(alpha=0.5, bins=24, density=True, stacked=True)

ax.hist(df['wind_speed'], **kwargs, color='blue',
        range=[0, 24], edgecolor='black')
ax.set_xticks(range(0, 25), minor=True)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', length=5)
ax.plot(x, y, color='red', alpha=0.5,
        label='Weibull Distribution\n(k = 1.38, c = 5.34)')
ax.set_xlabel('Wind Speed (m/s)')
ax.set_ylabel('Frequency')
ax.set_xlim(0, 24)
ax.legend()
ax.set_title('Masirah Island\nWind Speed Weibull Distribution')

# ax.grid()
plt.show()
