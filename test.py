from models import PredictRawVeggies

tester = PredictRawVeggies()

tester.create_model()

res = tester.call_predict(['artichoke_1.jpg', 'bellpeppers_1.jpg', 'asparagus_23.jpg', 'springonion_1.jpg', 'avocado_1.jpg'], 'img')
print(res)