import pandas as pd
import matplotlib.pyplot as plt


def read_file(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df


path1 = '/Users/nathanoliver/Desktop/Python/Github/Masirah Island/csv/load_data_hourly.csv'
path2 = '/Users/nathanoliver/Desktop/Python/Github/Masirah Island/csv/wind_data_hourly.csv'

df1 = read_file(path1)
df2 = read_file(path2)

index = range(1, 366)
columns = ['day', 'load', 'wind_speed']

df = pd.DataFrame(index=index, columns=columns)

hr = 0

for day in range(1, 366):
    print(day)
    df.iloc[day - 1, 0] = day
    df.iloc[day - 1, 1] = df1.iloc[1 + 24 * (day - 1), 0]
    df.iloc[day - 1, 2] = df2.iloc[1 + 24 * (day - 1), 0]

df.to_csv(
    '/Users/nathanoliver/Desktop/Python/Github/Masirah Island/csv/data_daily.csv')
