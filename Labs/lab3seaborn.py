#IMPORTS 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

#python dataset 
sns.get_dataset_names()
iris = sns.load_dataset('iris')
iris 

#boxplot 
sns.boxplot(iris.sepal_length, iris.sepal_width, iris.petal_length)
#this boxplot shows no correlation between the four elements 

#countplot 
sns.countplot(iris.petal_length)
#this countplot that the longer the petal length on a flower, the less petals there are on the flower

#distplot 
sns.distplot(iris.petal_width)
#distplot shows 

#scatterplot 
sns.scatterplot(iris.petal_length, iris.petal_width, hue = iris.sepal_length)
#scatterplot shows a positive correlation between the petal length/width - the longer the petal length, the wider it is 

#heatmap
sns.heatmap(iris.corr())
#heatmap shows that as length/width increase,the boxes get lighter

#point plot
sns.pointplot(x = 'sepal_length', y = 'sepal_width', data = iris)
#point plot shows no correlation between sepal length/width as the points are all over the place

#violin plot 
sns.violinplot(iris.sepal_length, iris.petal_width)
#violin plot shows a positive correlaton between sepal length/width, as the length increase, the width also increases 

sns.get_dataset_names()
flights = sns.load_dataset('flights')
flights.head()

sns.boxplot(flights.year, flights.month, flights.passengers)
#boxplot shows the number of passengers who flew in 1950, in ascending order

#distplot 
sns.distplot(flights.year)
#displot shows that the peak travel years were from about 1951 - 1958 

sns.scatterplot(flights.year, flights.passengers, hue = flights.month)
#positive correlation; peak flying months are may - september, the number of passengers continually increase every
#two years 

sns.heatmap(flights.corr())
#most passengers and peak travel years shown in top left and bottom right 
#least amount of passengers and years for travel depicted on the bottom left and top right 

sns.violinplot(flights.year, flights.passengers)
#violin plot shows that the number of passengers flying increased every year from 1949 - 1960
#also shows a larger range of passengers flyinf as the years went on 
#for example in 1949, the number passengers was around 100-150
#in 1960, the number of passengers ranged frolm about 250-700 

df = flights[['year', 'month', 'passengers']]
sns.pairplot(df, hue = 'month')
#top left - the number of passengers increased steadily each year, peaked around 1960, and decreased steadily in october
#top right - peak flying months are may-deptember - number of passengers flying increased each year 
#bottom left - again shows may-sept as peak flying months, number of passengers increased drastically from 1950-1960
#bottom right - majority of passengers flew in october, around 250 passengers flew between the months of oct-feb


