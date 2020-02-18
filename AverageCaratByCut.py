"""
The following lines:
-Show how to find the average carat of each cut style.
    -This concept is coded in three different ways using three different methods: 
        -groupby
        -for loop
        -creating data subsets.
"""


#Average carat of each cut style using a groupby.
carat_cut = df[['carat' , 'cut']]
mean_carat_by_cut_type = carat_cut.groupby(['cut']).mean()



#Average carat of each cut style using a for loop.
list_of_all_cuts = list(pd.unique(df.cut))

for cut_type in list_of_all_cuts:
    cut_subset = df[df.cut == cut_type]
    cut_subset_meancarat = cut_subset.carat.mean()
    print('Mean Carat of ' + str(cut_type) + ' Cut ' + str(round(cut_subset_meancarat , 5)))



#Average carat of each cut style using data subsets.
all_cuts = pd.unique(df.cut)

idealcut = df[df.cut == 'Ideal']
premiumcut = df[df.cut == 'Premium']
goodcut = df[df.cut == 'Good']
verygoodcut = df[df.cut == 'Very Good']
faircut = df[df.cut == 'Fair']

idealcut_meancarat = idealcut.carat.mean()
premiumcut_meancarat = premiumcut.carat.mean()
goodcut_meancarat = goodcut.carat.mean()
verygoodcut_meancarat = verygoodcut.carat.mean()
faircut_meancarat = faircut.carat.mean()
