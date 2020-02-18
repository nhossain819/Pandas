"""
The following lines:
-Create a dataframe from the first 5 rows.
-Export the dataframe as a CSV.
-Import the exported CSV.
"""
#Create a dataframe from the first 5 rows.
rows5 = df.iloc[:5]

#Export the dataframe as a CSV.
rows5.to_csv('/Users/Nayeem/Desktop/WORKING/rows5.csv', sep=',', index=False)

#Import the exported CSV.
df2 = pd.read_csv('/Users/Nayeem/Desktop/WORKING/rows5.csv')
