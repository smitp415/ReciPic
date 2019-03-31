''' Predict vegitables code here '''
#imports
import keras
from keras.models import Model
from keras import applications, optimizers
from keras.applications.vgg19 import preprocess_input
from keras.preprocessing import image
from keras.layers import Dense, Flatten, Dropout
from keras.callbacks import ModelCheckpoint
import numpy as np
import pandas as pd
from keras import backend as K
from keras.models import model_from_json

labelTranslate = {
    'Avocado' : 'avocado',
    'Beet' : 'beet',
    'Broccoli' :'broccoli',
    'Brussels Sprouts' : 'brussels sprouts',
    'Cabbage' : 'cabbage',
    'Carrots' : 'carrots',
    'Cauliflower' : 'cauliflower',
    'Corn' : 'corn',
    'Cucumber' : 'cucumber',
    'Green Beans' : 'green beans',
    'Green Tomato' : 'tomato',
    'Green pepper' : 'bell pepper',
    'Mushroom' : 'mushroom',
    'Okra' : 'okra',
    'Orange Onion' : 'onion',
    'Orange pepper' : 'bell pepper',
    'Peas' : 'pea',
    'Potato' : 'potato',
    'Pumpkin' : 'pumpkin',
    'Red Onion' : 'onion',
    'Red pepper' : 'bell pepper',
    'Spinach' : 'spinach',
    'Spring Onion' : 'green onion/scallion',
    'Sweet potato' : 'sweet potato/yam',
    'Tomato' : 'tomato',
    'White Onion' : 'onion'
}

class PredictRawVeggies:

    ###########################################################################
    def __init__(self):
        #Load the model
        self.img_width = 224
        self.img_height = 224

        #get the labels
        df_labels = pd.read_csv("labels.csv")
        df_labels = df_labels.sort_values(by=['Index'])
        self.labels= list(df_labels['Label'])
        self.num_labels = len(self.labels)
        K.clear_session()
        self.create_model()

        self.model_final._make_predict_function()


    ############################################################################
    def create_model(self):

        json_file = open("vgg19_4_arch.json", 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.model_final = model_from_json(loaded_model_json)
        self.model_final.load_weights("vgg19_4_50.h5")

    ######################################################################
    def call_predict(self, images, folder):

        predictions = {}
        #predict
        for image_name in images:
            image_path = folder+ "/" + image_name
            print(f"imagepath: {image_path}")
            test_image = keras.preprocessing.image.load_img(image_path, target_size=(224,224), grayscale=False)
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            test_image = preprocess_input(test_image)
            # print(test_image)
            predict = self.model_final.predict(test_image)
            # print(predict)
            zip_pred= zip(predict[0], self.labels)
            # if the prediction is high then only senf the value
            match_found = False
            newDict = {}
            for pred_value, pred in zip_pred:
                newDict[labelTranslate[pred]] = 1 if (pred_value > .95) else 0
            predictions[image_name] = newDict
        return predictions

    ######################################################################
    def collapseDict(self, predictions):
        newDict = {}
        for img in predictions:
            for veg in predictions[img]:
                if veg not in newDict:
                    newDict[veg] = predictions[img][veg]
                elif predictions[img][veg] == 1:
                    newDict[veg] = 1
        return newDict