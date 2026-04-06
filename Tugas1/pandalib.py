import pandas as pd

#read data from csv file
data = pd.read_csv('tips.csv')

#showing 10 first rows of data
print(data.head(10))