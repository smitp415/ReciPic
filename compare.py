import pandas as pd
from os import listdir
from models import PredictRawVeggies
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
classifier = PredictRawVeggies()
classifier.create_model()
files = [f for f in listdir('img')]
imageresults = classifier.collapseDict(classifier.call_predict(files, 'img'))

print(compare(imageresults, df))





#bestRecipes = [[df.iloc[i]['title'], df.iloc[i]['numIngredients']] for i in range(0,df.shape[0]) if df.iloc[i]['score'] == df.iloc[i]['score']]
#works

#export_csv = df.to_csv("example.csv", index = None, header=True)