import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


pd.set_option('display.max_columns', 30)


def read_file(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df


path1 = '/Users/nathanoliver/Desktop/Python/Github/Masirah Island/csv/data_daily.csv'
path2 = '/Users/nathanoliver/Desktop/Python/Github/Masirah Island/csv/turbine_power_coefficients.csv'

df1 = read_file(path1)
df2 = read_file(path2)

print(df2.columns)

df1['lower_wind_speed'] = 0
df1['upper_wind_speed'] = 0


turbine_col = ['E33', 'E44', 'E48', 'E53', 'E70', 'E82']
turbine_col_power_lower = []
turbine_col_power_upper = []
turbine_col_power_output = []


for i in range(len(turbine_col)):
    turbine_col_power_lower.append(turbine_col[i] + '_power_lower')
    df1[turbine_col_power_lower[i]] = 0

for i in range(len(turbine_col)):
    turbine_col_power_upper.append(turbine_col[i] + '_power_upper')
    df1[turbine_col_power_upper[i]] = 0

for i in range(len(turbine_col)):
    turbine_col_power_output.append(turbine_col[i] + '_power_output')
    df1[turbine_col_power_output[i]] = 0


for i in range(len(df1)):
    df1.loc[i, 'lower_wind_speed'] = math.floor(df1.loc[i, 'wind_speed'])
    df1.loc[i, 'upper_wind_speed'] = math.ceil(df1.loc[i, 'wind_speed'])


def determine_power_lower(lower_wind_speed):
    for i in range(14):
        if lower_wind_speed == df2.loc[i, 'wind_speed']:
            return i
            break


for i in range(len(df1)):
    wind_speed = df1.loc[i, 'lower_wind_speed']
    lower_wind_speed_index = determine_power_lower(wind_speed)
    upper_wind_speed_index = determine_power_lower(wind_speed) + 1
    for j in range(len(turbine_col)):
        df1.loc[i, turbine_col[j] + '_power_lower'] = df2.loc[lower_wind_speed_index,
                                                              turbine_col[j] + '_power']
        df1.loc[i, turbine_col[j] + '_power_upper'] = df2.loc[upper_wind_speed_index,
                                                              turbine_col[j] + '_power']

        ws = df1.loc[i, 'wind_speed']
        lw = df1.loc[i, 'lower_wind_speed']
        uw = df1.loc[i, 'upper_wind_speed']

        lp = df1.loc[i, turbine_col[j] + '_power_lower']
        up = df1.loc[i, turbine_col[j] + '_power_upper']
        delta_p = up - lp

        df1.loc[i, turbine_col[j] + '_power_output'] = delta_p * (ws - lw) + lp

d = [33.4, 44, 48, 52.9, 71, 82]
A = []

for i in range(len(d)):
    A.append(1 / 4 * math.pi * d[i]**2)


turbine_col_efficiency = []


for i in range(len(turbine_col)):
    turbine_col_efficiency.append(turbine_col[i] + '_efficiency')
    df1[turbine_col_efficiency[i]] = 0

    for j in range(len(df1)):
        df1.iloc[j, 23 + i] = df1.iloc[j, 23 + i - 6] * \
            1000 / (1 / 2 * A[i] * 1.225 * df1.loc[j, 'wind_speed']**3)

# df1.to_csv(
#     '/Users/nathanoliver/Desktop/Python/Github/Masirah Island/csv/wind_site_power_efficiency.csv')
