import streamlit as st
import pickle
import numpy as np
import sklearn

# predicting status

def predict_status(coutry,item_type,application,width,product_ref,quantity_tons_log,customer_log,thickness_log,selling_price_log,item_date_day,item_date_month,item_date_year,
                   delivery_date_day,delivery_date_month,delivery_date_year):
    
    # converting the datatype

    item_date_day_i = int(item_date_day)
    item_date_month_i = int(item_date_month)
    item_date_year_i = int(item_date_year)

    delivery_date_day_i = int(delivery_date_day)
    delivery_date_month_i = int(delivery_date_month)
    delivery_date_year_i = int(delivery_date_year)

    with open("S:/Projects/Industrial Copper Modelling/model.pkl",'rb') as f:
        model_class = pickle.load(f)

    user_data = np.array([[coutry,item_type,application,width,product_ref,quantity_tons_log,customer_log,thickness_log,selling_price_log,item_date_day,item_date_month,item_date_year,
                   delivery_date_day,delivery_date_month,delivery_date_year]])
    
    y_pred = model_class.predict(user_data)

    if y_pred == 1:
        return 1
    else:
        return 0
    
def predict_selling_price(coutry,status,item_type,application,width,product_ref,quantity_tons_log,customer_log,thickness_log,item_date_day,item_date_month,item_date_year,
                   delivery_date_day,delivery_date_month,delivery_date_year):
    item_date_day_s = int(item_date_day)
    item_date_month_s = int(item_date_month)
    item_date_year_s = int(item_date_year)

    delivery_date_day_s = int(delivery_date_day)
    delivery_date_month_s = int(delivery_date_month)
    delivery_date_year_s = int(delivery_date_year)

    with open("S:/Projects/Industrial Copper Modelling/model_ran.pkl",'rb') as f_ran:
        model_ran = pickle.load(f_ran)

    user_data = np.array([[coutry,status,item_type,application,width,product_ref,quantity_tons_log,customer_log,thickness_log,item_date_day,item_date_month,item_date_year,
                   delivery_date_day,delivery_date_month,delivery_date_year]])
    y_pred = model_ran.predict(user_data)

    return y_pred

st.set_page_config(layout='wide')
st.title("Industrial Copper Modelling")

tab3,tab1,tab2 = st.tabs(['About','Predict Business Status','Predict Selling Price'])

with tab1:
    st.header("Predict Status (Yes/No)")

    st.write(":red[The Maximum and Minimum values shown near each attribute is just for reference purposes. The user can any value of thier choice.]")

    day_options_d = list(range(1,32))
    day_options_m = list(range(1,13))
    day_options_y = list(range(2020,2022))
    day_options = list(range(2020,2023))

    col1,col2 = st.columns(2)

    with col1:
        country = st.number_input(label="Enter the value for Country to Predict Status (Min : 25, Max : 113)")
        item_type = st.number_input(label="Enter the value for item_type to Predict Status (Min : 0, Max : 6)")
        application = st.number_input(label="Enter the value for application to Predict Status (Min : 2, Max : 87.5)")
        width = st.number_input(label="Enter the value for width to Predict Status (Min : 700, Max : 1980)")
        product_ref = st.number_input(label="Enter the value for product_ref to Predict Status (Min : 611728, Max : 1722207579)")
        quantity_tons_log = st.number_input(label="Enter the value for quantity_tons_log to Predict Status (Min : -0.322334379, Max : 6.924734324)")
        customer_log = st.number_input(label="Enter the value for customer_log to Predict Status (Min : 17.21910566, Max : 17.23015536)")
        thickness_log = st.number_input(label="Enter the value for thickness_log to Predict Status (Min : -1.714798428, Max : 3.281543138)")
    with col2:
        selling_price_log = st.number_input(label="Enter the value for selling_price_log to Predict Status (Min : 5.975037795, Max : 7.390361169)")
        item_date_day = st.selectbox("Select the Item date day to Predict Status (Min : 1, Max : 31)",day_options_d)
        item_date_month = st.selectbox("Select the Item date month to Predict Status (Min : 1, Max : 12)",day_options_m)
        item_date_year = st.selectbox("Select the Item date year to Predict Status (Min : 2020, Max : 2021)",day_options_y)
        delivery_date_day = st.selectbox("Select the Delivery date day to Predict Status (Min : 1, Max : 31)",day_options_d)
        delivery_date_month = st.selectbox("Select the Delivery date month to Predict Status (Min : 1, Max : 12)",day_options_m)
        delivery_date_year = st.selectbox("Select the Delivery date year to Predict Status (Min : 2020, Max : 2022)",day_options)

        st.write("")

    button = st.button(":red[PREDICT THE STATUS]",use_container_width=True)

    if button:
        status = predict_status(country,item_type,application,width,product_ref,quantity_tons_log,customer_log,thickness_log,selling_price_log,item_date_day,item_date_month,item_date_year,
                   delivery_date_day,delivery_date_month,delivery_date_year)
            
        if status == 1:
            st.write (":green[The Business is Won]")

        else:
            st.write(":red[The Business is Lost]")

                
with tab2:
    st.header("Predicting the Selling Price")

    st.write(":red[The Maximum and Minimum values shown near each attribute is just for reference purposes. The user can any value of thier choice.]")

    col1,col2 = st.columns(2)

    with col1:
        country = st.number_input(label="Enter the value for Country to Predict Selling Price (Min : 25, Max : 113)")
        status = st.number_input(label="Enter the value for Status to Predict Selling Price (Min : 0, Max : 8) ")
        item_type = st.number_input(label="Enter the value for item_type to Predict Selling Price (Min : 0, Max : 6)")
        application = st.number_input(label="Enter the value for application to Predict Selling Price (Min : 2, Max : 87.5)")
        width = st.number_input(label="Enter the value for width to Predict Selling Price (Min : 700, Max : 1980)")
        product_ref = st.number_input(label="Enter the value for product_ref to Predict Selling Price (Min : 611728, Max : 1722207579)")
        quantity_tons_log = st.number_input(label="Enter the value for quantity_tons_log to Predict Selling Price (Min : -0.322334379, Max : 6.924734324)")

    with col2:

        customer_log = st.number_input(label="Enter the value for customer_log to Predict Selling Price (Min : 17.21910566, Max : 17.23015536)")
        thickness_log = st.number_input(label="Enter the value for thickness_log to Predict Selling Price (Min : -1.714798428, Max : 3.281543138)")
        item_date_day = st.selectbox("Select the Item date day to Predict Selling Price (Min : 1, Max : 31)",day_options_d)
        item_date_month = st.selectbox("Select the Item date month to Predict Selling Price (Min : 1, Max : 12)",day_options_m)
        item_date_year = st.selectbox("Select the Item date year to Predict Selling Price (Min : 2020, Max : 2021)",day_options_y)
        delivery_date_day = st.selectbox("Select the Delivery date day to Predict Selling Price (Min : 1, Max : 31)",day_options_d)
        delivery_date_month = st.selectbox("Select the Delivery date month to Predict Selling Price (Min : 1, Max : 12)",day_options_m)
        delivery_date_year = st.selectbox("Select the Delivery date year to Predict Selling Price (Min : 2020, Max : 2022)",day_options)

    st.write("")

    button = st.button(":red[PREDICT THE SELLING PRICE]",use_container_width=True)

if button:
    selling_price = predict_selling_price(country,status,item_type,application,width,product_ref,quantity_tons_log,
                                        customer_log,thickness_log,item_date_day,item_date_month,item_date_year,
                                        delivery_date_day,delivery_date_month,delivery_date_year)

    st.write("The Selling Price is:",selling_price)


with tab3:
    st.header("Copper Industry")
    st.write("The **copper industry** plays a crucial role in global infrastructure, technology, and energy sectors. Copper is widely used in electrical wiring, construction, and renewable energy systems due to its excellent conductivity and durability.")  
    st.subheader("Dynamic Pricing in the Copper Industry")
    st.write("Copper prices fluctuate based on several factors, including supply chain disruptions, demand from industries like electric vehicles and renewable energy, and geopolitical influences. The **global supply chain** faces challenges such as declining ore grades, water scarcity in mining regions, and political instability in major copper-producing countries like Chile and Zambia.")  
    st.write("On the **demand side**, copper consumption is rising due to the transition to green energy, with electric vehicles requiring **four times more copper** than traditional cars. Additionally, AI-driven data centers and solar energy infrastructure are increasing copper demand.")  
    st.write("Copper prices have historically been linked to crude oil and China's economic growth, but recent trends show a divergence, with copper prices surging despite China's slowing economy. Tariffs and recession risks also impact pricing, making the market highly volatile.")  

    st.subheader("Two Objectives")
    st.write("We have been given a Copper Industry's Dataset where we must predict the following:")
    st.write("1. The Business Status (Yes/No)") 
    st.write("2. The Selling Price")

    st.subheader("Predicting the Business Status:")
    st.write("* We are using Extra Trees Classification Model to predict the business status")
    st.write("* We have 15 inputs to predict the status such as country, item_type etc. All of them are in numerical data type")
    st.write("* In order to predict the status the user must fill in the 15 data columns. Minimum and Maximum values are represented for reference purposes")
    st.write("* Click on the Predict status button to get the respective value")
    st.write("* The output would either be a Yes or No. Yes indicating a succesfull business No indicating a lost business")

    st.subheader("Predicting the Selling Price:")
    st.write("* We are using Random Forest Regression Model to predict the selling price")
    st.write("* We have 15 inputs to predict the selling price such as country, item_type etc. All of them are in numerical data type")
    st.write("* In order to predict the selling price the user must fill in the 15 data columns. Minimum and Maximum values are represented for reference purposes")
    st.write("* Click on the Predict selling price button to get the respective value")












