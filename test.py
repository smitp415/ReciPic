import pprint
from os import listdir
from models import PredictRawVeggies

tester = PredictRawVeggies()

tester.create_model()

files = [f for f in listdir('img')]
res = tester.call_predict(files, 'img')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(res)