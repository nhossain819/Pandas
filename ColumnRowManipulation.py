"""
The following lines:
-Selects rows by index
-Selects specific rows and columns
-Finds the numbers of rows and columns
"""
#Select rows 50 to 75.
rows_50_to_75 = df.iloc[50:76]

#Select specific rows and columns.
carat_cut = df[['carat' , 'cut']]
carat_cut_rows_5_10_15 = carat_cut.iloc[[5, 10, 15]]

#Find the number of columns and rows.
number_of_columns = len(df.axes[1])
number_of_rows = len(df.axes[0])
