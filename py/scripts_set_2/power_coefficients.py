import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

turbines = np.array([[[0, 0, 0, 5, 13.7, 30, 55, 92, 138, 196, 250, 292.8, 320, 335, 335, 335, 335, 335, 335, 335, 335, 335, 335, 335, 335],
                      [0, 0, 1.4, 8, 24.5, 53, 96, 156, 238, 340, 466, 600, 710,
                          790, 850, 880, 905, 910, 910, 910, 910, 910, 910, 910, 910],
                      [0, 0, 2, 12, 32, 66, 120, 191, 284, 405, 555, 671, 750, 790,
                          810, 810, 810, 810, 810, 810, 810, 810, 810, 810, 810],
                      [0, 0, 2, 14, 38, 77, 141, 228, 336, 480, 645, 744, 780, 810,
                          810, 810, 810, 810, 810, 810, 810, 810, 810, 810, 810],
                      [0, 0, 2, 18, 56, 127, 240, 400, 626, 892, 1223, 1590, 1900, 2080,
                          2230, 2300, 2310, 2310, 2310, 2310, 2310, 2310, 2310, 2310, 2310],
                      [0, 0, 3, 25, 82, 174, 321, 532, 815, 1180, 1612, 1890, 2000, 2050, 2050, 2050, 2050, 2050, 2050, 2050, 2050, 2050, 2050, 2050, 2050]],

                     [[0, 0, 0, .35, .4, .45, .47, .5, .5, .5, .47, .41, .35, .28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, .19, .32, .41, .46, .48, .49, .5, .5, .5, .48, .44, .39,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, .23, .4, .45, .48, .5, .5, .5, .5, .5, .45, .39, .32,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, .19, .39, .44, .46, .48, .49, .49, .49, .48, .42, .34, .27,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, .1, .27, .36, .42, .46, .48, .5, .5, .5, .49, .45, .39,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, .12, .29, .4, .43, .46, .48, .49, .5, .5, .44, .36, .29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]])


print(turbines[0, 1, 2])

x, y, z = np.shape(turbines)

print(np.shape(turbines))

turbine = ['E33', 'E44', 'E48', 'E53', 'E70', 'E82']

title = ['power', 'efficiency']

columns = []

for i in title:
    for j in turbine:
        columns.append(j + '_' + i)

print(columns)

df = pd.DataFrame(index=range(z), columns=columns)

print(x, y, z)

for j in range(y):
    for k in range(z):
        print('turbine:', j)
        print('level:', k)
        df.iloc[k, j] = turbines[0, j, k]

for j in range(y):
    for k in range(z):
        print('turbine:', j)
        print('level:', k)
        df.iloc[k, j + 6] = turbines[1, j, k]

print(df.columns)


plt.show()

# df.to_csv('/Users/nathanoliver/Desktop/Python/Github/Masirah Island/csv/turbine_power_coefficients.csv')
