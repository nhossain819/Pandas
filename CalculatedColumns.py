"""
The following lines:
-Create a 'size' column calculated from the x, y, and z columns.
-Create an 'Expensive' column based on the price column value.
-Create a data frame based on size and whether or not the item is expensive.
-Sort the values of the dataframe by price.
"""

#Create a calculated 'size' column.
df['size'] = round((df.x * df.y * df.z) , 2)

#Create a calculated 'Expensive' column.
df['Expensive'] = df.price.apply(lambda x: 'Yes' if x > 2000 else 'No')

#Create a dataframe based on the 'Expensive' column.
big_expensive = df[(df.size > 25) & (df.Expensive == 'Yes')]

#Sort the dataframe by price.
df.sort_values(by=['price'], inplace=True, ascending=False)
