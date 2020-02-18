"""
The following lines of code:
-Import pandas.
-Create a data frame based on a csv.
-Print the first 5 rows of the dataframe.
-Print basic information about the dataframe.
"""
#Import pandas
import pandas as pd

#Create a dataframe
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

#Print the first 5 rows.
print(df.head(5))

#Print information about the data frame.
print(df.info())
