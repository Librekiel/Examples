import pandas as pd
import numpy as np

ind = True
try:
    file = pd.read_csv('input.txt', sep=' ', header = None)
except:
    print(10000)
    ind = False

if ind:
    file['Timedate'] = (file[0] + ' ' + file[1]).apply(pd.Timestamp)
    table = file[['Timedate', 2]]
    table.columns = ['Timedate', 'Spent']
    table = table.sort_values('Timedate')
    
    avg_spent = np.sum(table['Spent'])/(1+(table['Timedate'].tail(1) - pd.Timestamp('2021-01-01 00:00:00')).iloc[0].total_seconds()/60)
    predicted_spent = avg_spent*(1+(pd.Timestamp('2021-02-01 00:00:00') - table['Timedate'].tail(1)).iloc[0].total_seconds()/60)
    left = round(10000 - np.sum(table['Spent']) - predicted_spent,2)
    
    print(left)
