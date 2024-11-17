import pandas as pd
import numpy as np

df = pd.DataFrame({"name":['Vyapti','Sejal','Sanjya'], 
                   "colour":["blue",np.nan,np.nan],
                   "born":[pd.Timestamp("13/04/2005"),pd.NaT, pd.NaT]})
print(df.head())

print(df.shape) #3,3
print(df.info)

print(df.dropna()) #it drops all the NaT rows

df1 = pd.DataFrame({"name":['Vyapti','Sejal','Sanjya'], 
                   "colour":["blue",np.nan,np.nan],
                   "age": [np.nan,pd.NaT,np.nan],
                   "born":[pd.Timestamp("13/04/2005"),pd.NaT, pd.NaT]})
print(df1.dropna(how='all',axis=1)) #it drops the nan only if the whole column is nan #axis=1 is for columns

print()

df2 = pd.DataFrame({"name":['Vyapti','Sejal','Vyapti'], 
                   "age": [19,20,21],})
print(df2.drop_duplicates(subset=['name'],keep='first'))
print(df2.drop_duplicates(subset=['name'],keep='last'))
print(df2.drop_duplicates(subset=['name'],keep=False))

print(df2['name'].value_counts(dropna=False))

print(df.notnull()) #wherever there is not null it is True otherwise False
