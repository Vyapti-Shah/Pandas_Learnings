import pandas as pd

#to explain copy 

data = pd.read_excel('practice2.xlsx', sheet_name='Sheet1')
print(data)

data2 = data.copy()

with pd.ExcelWriter('practice2.xlsx') as writer:
    data.to_excel(writer, sheet_name='Sheet1', index=False)
    data2.to_excel(writer,sheet_name='Sheet1.0', index=False)