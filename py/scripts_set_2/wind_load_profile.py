import pandas as pd
import matplotlib.pyplot as plt


def read_file(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df


path = '/Users/nathanoliver/Desktop/Python/Github/Masirah Island/csv/data_daily.csv'

df = read_file(path)

print(df.columns)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 5))

ax1.plot(df['day'], df['load'], color='blue', label='Load (kW)')
ax2.plot(df['day'], df['wind_speed'], color='red', label='Wind Speed (m/s)')

ax1.set_xlim(1, 365)
ax2.set_xlim(1, 365)

ax1.set_ylim(0, 8000)
ax2.set_ylim(0, 13)

ax1.set_title('Masirah Island\nLoad and Wind Speed Profiles')
ax2.set_xlabel('Day')
ax1.set_ylabel('Average Daily\nLoad (kW)')
ax2.set_ylabel('Average Daily\nWind Speed (m/s)')

ax1.legend()
ax2.legend()

plt.show()
