import pandas as pd

dict1 = {
    "name":['vyapti','shah','sanjay','sejal'],
    "marks":[92,34,24,67],
    "city":['borivali','ahmedabad','vasai','goregaon']
}
df = pd.DataFrame(dict1)
print(df) #to form a table

print()

df.to_csv('intro.csv') #to create an exel file
df.to_csv('intro_index_false.csv',index=False) #to create an exel file without showing the index numbers

print(df.head(2)) #for bigger data sets we have to show only some of the data so the upper part of data is head

print()

print(df.tail(2)) #lower part of data is tail

print()

print(df.describe()) #calculates mean,std,etc.

print()

vyaps = pd.read_csv('intro_read.csv')
print(vyaps)

print()

print(vyaps['speed'])

print()

vyaps['speed'][0] = 50 #to change the value of a cell
print(vyaps)

vyaps.to_csv('intro_read_updated.csv') #creates the updated value of speed (ie 50)

print()

vyaps.index = ['first', 'second', 'third', 'fourth'] #replaces the index from 0,1,2,3 to first,second,third,fourth
print(vyaps)