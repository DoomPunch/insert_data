import pandas as pd
import numpy as np
from get_path import get_config_path

#  reference range mean加减1*std, 红线用mean加减2.5*std

filename = get_config_path('item_stats.csv')
df = pd.read_csv(filename)
# print(df['mean'])

a = list(np.array(df))

x = {}
zz = []
for i in a:
    if str(i[0]) == 'nan':
        i[0] = 'NA'
    x[i[0]] = {}
    x[i[0]]['mean'] = i[1]
    x[i[0]]['std'] = i[2]
    x[i[0]]['reference_range'] = [i[1]-i[2], i[1]+i[2]]
    x[i[0]]['red_flag'] = [i[1]-(2.5*i[2]), i[1]+(2.5*i[2])]
    print('{' + str(i[0]) + ': ' + str(x[i[0]]) + '}')
    # zz.append(str(i[0]))

print(zz)
