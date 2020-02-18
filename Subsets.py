"""
The following lines:
-Creates a subsets of data based on row value.
"""
#Create a subset of data with the best cut of diamond.
best_cut = df[df.cut == 'Ideal']

#Produce a subset of data with null clarity values.
missing_clarity = df[df['clarity'].isnull()]

#A subset of data with carat values between 0.25 and 0.30.
carat_between25and30 = df[(df.carat > 0.25) & (df.carat <= 0.3)]
