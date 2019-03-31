import pandas as pd
#vegelist = ['green onion', 'tomatoes']

#TL only dataframe w/ # of ingredients, and also 
#best = # of ingredients - # matches    >= 0
def compare(imageresults, df):
	alltraininglabels =['avocado', 'beet', 'bell pepper', 'broccoli', 'brussel sprout', 'cabbage', 'carrot', 'carrot', 'cauliflower',
				 'corn', 'cucumber', 'green bean', 'green onion/scallion', 'mushroom', 'okra', 'onion', 'pea', 
				 'potato', 'potato', 'pumpkin', 'spinach', 'sweet potato/yam', 'tomato']

	existinglabels = []
	for label in alltraininglabels:
		if imageresults[label] == 1:#if exists
			existinglabels.append(label)

	#take rowwise sum of columns in existing labels and place as column "available ingredients"
	df['sharedIngredients'] = df[existinglabels].sum(axis=1) 
	# score = most shared ingredients, highest ratio of available/total as tie breaker
	df['score'] = df['sharedIngredients'] + (df['sharedIngredients']/df['numIngredients'])
	maxid = df['score'].idxmax()
	# print(df.iloc[maxid][:])
	# print(df.iloc[maxid]['title'])
	return df.iloc[maxid]['title']

df = pd.read_csv("recipeData.csv")
imageresults = {   'avocado': 0,
				   'beet': 1,
				   'bell pepper': 1,
				   'broccoli': 1,
				   'brussel sprout': 1,
				   'cabbage': 1,
				   'carrot': 0,
				   'cauliflower': 0,
				   'corn': 0,
				   'cucumber': 0,
				   'green bean': 0,
				   'green onion/scallion': 1,
				   'mushroom': 1,
				   'okra': 0,
				   'onion': 1,
				   'pea': 0,
				   'potato': 0,
				   'pumpkin': 0,
				   'spinach': 0,
				   'sweet potato/yam': 0,
				   'tomato': 1
				}

compare(imageresults, df)





#bestRecipes = [[df.iloc[i]['title'], df.iloc[i]['numIngredients']] for i in range(0,df.shape[0]) if df.iloc[i]['score'] == df.iloc[i]['score']]
#works

#export_csv = df.to_csv("example.csv", index = None, header=True)


