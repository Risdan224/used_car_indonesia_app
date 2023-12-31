from pathlib import Path
import pandas as pd
import streamlit as st
import predict

def get_user_input(df):
    car_maker = st.selectbox("Manufacturer:", used_car.vehicle_make.unique())
    car_type = st.selectbox("Model/Type:", used_car[used_car.vehicle_make == car_maker].vehicle_model.unique())
    car_body_type = st.selectbox("Body Type:", used_car[used_car.vehicle_model == car_type].vehicle_body_type.unique())
    car_gear_type = st.selectbox("Gear Type:", used_car.vehicle_transmission.unique())
    car_year = st.number_input("Year of Production:", value=2000, step=1)
    car_mileage = st.number_input("Mileage:", value=10000, step=1)

    user_data = pd.DataFrame({
        'vehicle_model':[car_type],
        'vehicle_make':[car_maker],
        'vehicle_transmission':[car_gear_type],
        'vehicle_body_type':[car_body_type],
        'vehicle_year':[car_year],
        'vehicle_mileage':[car_mileage]
    })

    return user_data

if __name__=="__main__":
    
    used_car = pd.read_csv(str(Path(__file__).parents[1] /'data/used_car_for_model.csv'))

    st.set_page_config(page_title="Used-Car Price Prediction in Indonesia", page_icon=None, layout="centered")
    
    # Displaying text
    st.markdown("<h1 style='text-align: center; color: black;'>USED-CAR PRICE PREDICTION IN INDONESIA</h1>", unsafe_allow_html=True)

    # Displaying an image
    st.image(str(Path(__file__).parents[1] /'img/mobilbekas.png'), width=700)

    st.write("""  
            This application predicts a used-car price based on the manufacturer, model, body-type, gear-type, year and mileage. The prediction is calculated using the XGBoost machine learning model. The model has a CV score of 13% (MAPE) and test scores of 14% (MAPE) and 87.56% (R2). Therefore, when using prediction results, consider these CV and test values. To get your prediction, please input your car features below here:
             """)
    
    user_data = get_user_input(used_car)

    # display predictions
    if st.button("Predict Price"):
        used_car_price = round(predict.predict(user_data)[0], 2)  # get prediction
        formatted_X = "{:.0f}".format(used_car_price)
        st.write(f"**Estimated car price : Rp. {formatted_X}**")
        st.write("This price calculated using machine learning model, can be used to estimate used-car price for selling or buying.")

    st.write("Created by: Risdan")
