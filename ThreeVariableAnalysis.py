"""
The following lines:
-Create a dataframe based on color and size.
-Calculate the average size by color.
-Create a dataframe based on color and price.
-Calculate the total revenue of each color.
-Sort the dataframe by price.
-Remove rows of index 7 and 10 from the dataframe.
"""
#Create a dataframe based on color and size.
color_size = df[['color' , 'size']]

#Calculate the average size by color.
mean_size_by_color = color_size.groupby(['color']).mean()

#Create a dataframe based on color and price.
color_price = df[['color' , 'price']]

#Calculate the total revenue of each color.
sum_price_by_color = color_price.groupby(['color']).sum()

#Calculate the total revenue of each color.
sum_price_by_color.sort_values(by=['price'], inplace=True, ascending=False)

#Remove rows of index 7 and 10 from the dataframe.
drop_test_rows_5_15 = rows_5_15.drop(df.index[[7,10]])
