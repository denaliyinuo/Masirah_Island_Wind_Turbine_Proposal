import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


pd.set_option('display.max_columns', 30)


def read_file(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df


path = '/Users/nathanoliver/Desktop/Python/Github/Masirah Island/csv/wind_site_power_efficiency.csv'

df = read_file(path)

print(df.columns)

print(max(df['E44_power_output']))

plt.plot(df['day'], df['E44_power_output'])
plt.show()
