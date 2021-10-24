#IMPORTS
import csv 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Part 1 
loans_1 = pd.read_csv('Loans - 1.csv')
loans_1 

loans_2 = pd.read_csv("Loans - 2.csv")
loans_2 

merged_data = pd.merge(loans_1, loans_2, on ='ID')
merged_data 

#Part 2

#1 Top 5:
import numpy as np
sorted_df = merged_data.sort_values('balance', ascending = False)
sorted_df 

sorted_df.head(5)
# finds top 5 records 

#Bottom 5 
sorted_df = merged_data.sort_values('balance', ascending = False)
sorted_df 

sorted_df.tail(5)

#finds bottom 5 records 

sorted_df.describe()

#has everything like mean, min, max, std etc 

x = (merged_data['age'], merged_data['balance'])
plt.hist(x, bins = 2)

plt.show()

#Part 3, 1: 
merged_data.describe() 
#avg age is 41.170095 
#avg balance is 1422.657819

data_df = {'bin1':["19 - 35"],
          'bin2':['36 - 50'], 
          'bin3':['51-65'], 
          'bin4':['65+']}
data_df 
df = pd.DataFrame(data_df)

age = ['87','49','39','33','19']
print(df)
#made a bin for these values 
print(merged_data)

merged_data.drop(columns=['poutcome'])
#dropped column

#Part 4 - Scatter 
import matplotlib.pyplot as plt 
plt.scatter(merged_data['age'], merged_data['balance'])
plt.show() 

#5 - Bonus
from scipy import stats 
stats.pearsonr(merged_data['age'], merged_data['balance'])




