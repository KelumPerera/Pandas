# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:27:54 2017

@author: Kelum Perera
"""

import pandas as pd

# Data import from CSV file

df = pd.read_csv('/Data/MonthlySales.csv')

df

# Data import from JSON file

import json
from pandas.io.json import json_normalize

with open('/data/monthlySalesbyCategoryMultiple.json') as json_data:
    d = json.load(json_data)

df = json_normalize(d['contents'], 'monthlySales', ['category', 'region'])

df

# Data import from parquet file
# pip install pyarrow

import pyarrow.parquet as pq

table = pq.read_table('/data/MonthlyProductSales.parquet')
table.to_pandas()


# Data import from excel file
# pip install xlrd

from pandas import ExcelWriter
from pandas import ExcelFile

# load the excel sheet into the Pandas Dataframe structure
df = pd.read_excel("/data/excel_data.xlsx", sheetname='Sheet1',skiprows=2 )

# Calculations using columns

# print each row of the item column
for i in df.index:
    print(df['Item'][i])

# compute a new column as the product of two other columns (ie. Price * Qty)

df['Price*Qty'] =  np.nan

for i in df.index:
    df['Price*Qty'][i] = df['Price'][i] * df['Qty'][i]

# load the Pandas Dataframe into a excel worksheet structure
writer = ExcelWriter('/data/excel_saveddata.xlsx')
df.to_excel(writer,'Sheet1',index=True)
writer.save()
