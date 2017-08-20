# -*- coding: utf-8 -*-
"""
Created on Fri May 05 21:25:51 2017

@author: Kelum Perera
"""

import pandas as pd

    
# Take a 2D array as input to your DataFrame 
import numpy as np
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(pd.DataFrame(my_2darray))

# Take a dictionary as input to your DataFrame 
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
print(pd.DataFrame(my_dict))

# Take a DataFrame as input to your DataFrame 
my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
print(pd.DataFrame(my_df))

# Take a Series as input to your DataFrame
my_series = pd.Series({"United Kingdom":"London", "India":"New Delhi", "United States":"Washington", "Belgium":"Brussels"})
print(pd.DataFrame(my_series))


# DATE TIME FORMATING

# Create a dataframe through a dictionary
table = pd.DataFrame(data = {'DateTime':['01-01-17 16:30','01-01-17 16:31','02-01-17 08:45','02-01-17 08:45','02-01-17 10:40','02-01-17 16:40','02-01-17 16:41','02-01-17 16:42','03-01-17 08:45','03-01-17 08:45','03-01-17 10:48'],
                             'Amount':[1000,2000,1000,1000,50000,4000,5000,9000,4000,5000,20000],
                             'Ref':['Deduct','Deduct','Add','Add','Add','Transfer','Transfer','Deduct','Add','Add','Deduct'],
                             'DrCode':[1500,1400,9000,9000,9000,1600,1700,2000,9000,9000,4000],
                             'CrCode':[9000,9000,1500,1400,3000,2000,2000,9000,1600,1700,9000],})

# List the Columns
list(table.columns.values)

# check the type of an object, of each columns, of particular column
type(table)
table.dtypes
table['DateTime'].dtype

# convert the DateTime field from an object to a datetime - Method 1
table['DateTime1']= pd.to_datetime(table['DateTime'])
table['DateTime1'].dtype

# convert the DateTime field from an object to a datetime - Method 2
table['DateTime2'] = table['DateTime'].astype('datetime64[ns]')
table['DateTime2'].dtype

# convert the DateTime field from an object to a datetime - Method 3
import datetime as dt
table['DateTime3'] = table['DateTime'].apply(lambda x: 
                                    dt.datetime.strptime(x,'%d-%m-%y %H:%M'))

  # or
import datetime as dt
table['DateTime1'] = table['DateTime'].apply(lambda x: 
                                    dt.datetime.strptime(x,'%d-%m-%Y %H:%M:%S'))
    

# Delete column- Method 1
del table['DateTime2']

# Delete column- Method 2
table = table.drop('DateTime2', 1)  # where 1 is the axis number (0 for rows and 1 for columns.)
table.drop('DateTime2',axis=1,inplace=True) # To delete the column without having to reassign df you can do
table.drop(table.columns[[6,7]], axis=1) #  to drop by column number instead of by column label

# Nearest 5th minute
def round_to_5min(t):
    delta = datetime.timedelta(minutes=t.minute%5, 
                               seconds=t.second, 
                               microseconds=t.microsecond)
    t -= delta
    if delta > datetime.timedelta(minutes=2.5):
        t += datetime.timedelta(minutes=5)
    return t

table['ns5MinDateTime'] = table.DateTime1.map(round_to_5min)

# Nearest 10th minute
def round_to_10min(t):
    delta = datetime.timedelta(minutes=t.minute%10, 
                               seconds=t.second, 
                               microseconds=t.microsecond)
    t -= delta
    if delta > datetime.timedelta(minutes=5):
        t += datetime.timedelta(minutes=10)
    return t

table['ns10MinDateTime'] = table.DateTime1.map(round_to_10min)




