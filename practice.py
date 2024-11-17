#a DatFrame which contains only integers with 3 rows and 2 columns

import pandas as pd

data = pd.read_excel('practice.xlsx', sheet_name='Sheet1')
print(data)

print()

data0 = pd.read_excel('practice.xlsx', sheet_name='Sheet2')
print(data0)

print()

data.iloc[0,2] = 2000
print(data)

#data.to_excel('practice.xlsx', sheet_name='Sheet1') #makes changes in the excel sheet

#data2 = data.copy()
#data.to_excel(writer, sheet_name='Sheet1')
#data2.to_excel(writer,sheet_name='Sheet1.0')

print()

print(data.describe())

print()

numeric_data = data0.select_dtypes(include='number') #select only numeric data
print(numeric_data.describe())

print("\nMean:")
print(numeric_data.mean())
print()

print("\nCorrelation:")
print(numeric_data.corr())
print()

print("\nCount:")
print(numeric_data.count())
print()

print("\nMax:")
print(numeric_data.max())
print()

print("\nMin:")
print(numeric_data.min())
print()

print("\nMedian:")
print(numeric_data.median())
print()

print("\nStandard Deviation:")
print(numeric_data.std())