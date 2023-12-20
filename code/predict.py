from pathlib import Path
import pickle

def predict(df):
    # Load the model and scaler from the saved file
    # Load model
    file_name =str(Path(__file__).parents[1] / 'model/indonesia_used_car_colab_v1.pkl')
    model = pickle.load(open(file_name, 'rb'))
    
    pred = model.predict(df)
    return pred