import pandas as pd
#vegelist = ['green onion', 'tomatoes']

#TL only dataframe w/ # of ingredients, and also 
#best = # of ingredients - # matches    >= 0
def compare(df, vegelist):
	return

df = pd.read_csv("vegetables.csv")
#trainedlabels = [""]



traininglabels =['avocado', 'beet', 'bell pepper', 'broccoli', 'brussel sprout', 'cabbage', 'carrot', 'carrot', 'cauliflower',
				 'corn', 'cucumber', 'eggplant', 'green bean', 'green onion/scallion', 'mushroom', 'okra', 'onion', 'pea', 
				 'potato', 'potato', 'pumpkin', 'spinach', 'sweet potato/yam', 'tomato']
#droplist = [i for i in df.columns if df.loc['total', i] not in trainedlabels]
#df = df[]
df = df.drop(droplist, axis=1)
print(df.shape)

