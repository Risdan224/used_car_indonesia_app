from pathlib import Path
import pickle
import pandas as pd
import numpy as np
import sklearn
import category_encoder as ce
import xgboost


def predict(df):
    # Load the model and scaler from the saved file
    # Load model
    file_name =str(Path(__file__).parents[1] / 'model/indonesia_used_car_colab_v2.pkl')
    model = pickle.load(open(file_name, 'rb'))
    
    pred = model.predict(df)
    return pred
