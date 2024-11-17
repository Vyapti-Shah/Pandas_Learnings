import pandas as pd
import numpy as np

ser = pd.Series(np.random.rand(34))
print(ser)
print(type(ser))

print()

newdf = pd.DataFrame(np.random.rand(334,5), index=np.arange(334))
print(newdf)
print(type(newdf))
print(newdf.describe())
print(newdf.dtypes) 
print(newdf.head())

print()
newdf[0][0] = 'vyapti'
print(newdf.dtypes)
print(newdf.head())
print(newdf.index)
print(newdf.columns)
print(newdf.to_numpy())

print()

newdf[0][0] = 0.2
print(newdf.head())
print(newdf.to_numpy())

print()

print(newdf.T) #we get the transpose (ie 5,334)

print()

print(newdf.sort_index(axis=0,ascending=False)) #rows ko ulta sort krdega
print(newdf.sort_index(axis=1,ascending=False)) #columns ko ulta sort krdega

print()

print(newdf[0])
print(type(newdf[0])) #series

print()

newdf2 = newdf #it changes the value
newdf2[0][0] = 9876
print(newdf) #this shows that newdf2 is the view of newdf which means newdf is in the same memory location but 
             #newdf2 is pointing towards newdf so whenever newdf2 is changed newdf will also change


newdf3 = newdf.copy() #it does not change the value 
newdf3[0][0] = 2345
print(newdf) 

newdf4 = newdf[:] #it changes the value
newdf4[0][0] = 0000
print(newdf) 

#loc function = used to change the values #uses columns name only (ie "ABCDE") we cannot use index values to denote it (ie 0,1,2,3,4)
newdf.loc[0] = 654 #it locks the value
print(newdf.head(2))

print()

newdf.columns = list("ABCDE")
print(newdf.head(2))
newdf.loc[0,"A"] = 700
print(newdf.head(2))
newdf.loc[0,0] = 650 #for any column not stated in newdf it will form a new column and put remaining values as NaN
print(newdf.head(2))

a = newdf.drop(['A','C'],axis=1) #axis=1 mein A column hatgya (ie A dropped) #it does'nt change the data set
print(a.head(2))

print()

print(newdf.loc[[1,2],['C','D']])
print(newdf.loc[:,['C','D']])
print(newdf.loc[[1,2],:])

print(newdf.loc[(newdf['A']<0.3) & (newdf['C']>0.1)]) #states all the values which are less than 0.3 and greater than 0.1

print(newdf.iloc[0,2]) #gives the value of the cell #uses index values to denote even if the columns are denoted by "ABCDE"

print(newdf.iloc[[1,5],[0,3]])

newdf.drop(['D','E'],axis=1,inplace=True) #inplace changes the data set by removing D and E permanently
print(newdf.head(2))

print(newdf.reset_index()) #makes a new column of index and resets it
# print(newdf.reset_index(drop=True,inplace=True)) #removes the extra column of index

newdf.loc[:,['B']] = None
print(newdf.head(3))
print(newdf['B'].isnull())

newdf.loc[:,['B']] = 50
print(newdf.head(3))