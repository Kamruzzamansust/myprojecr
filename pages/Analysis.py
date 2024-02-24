import pandas as pd 
import streamlit as st 
import requests
import seaborn as sns 
import matplotlib.pyplot as plt

from src.loding_data import load_data,get_data_from_fastapi


st.set_page_config(layout ='wide')
df=load_data('Data\data.csv')




FASTAPI_URL = "http://127.0.0.1:8000/"

# def make_request(gender):
#     url = f"{FASTAPI_URL}/analysis/{gender}"
#     response = requests.get(url)
    
#     return response

# Streamlit UI
st.title("Analysis Page")
col1 , col2 , col3 = st.columns([2,2,2,])

with col1:
 column_name = st.selectbox("Select column", df.columns)

 if st.button("Get column"):
    
    analysis_data = get_data_from_fastapi(FASTAPI_URL)
    #st.write(analysis_data)
    column_data =  analysis_data[column_name].tolist()
    data = pd.DataFrame(column_data)
    
    data = data.rename(columns={0: column_name})
    #st.bar_chart(column_data)
    #st.write(data)
    if df[column_name].dtype == 'object':
        # Create count plot for object columns
        st.subheader(f"Count Plot for {column_name}")
        count_plot = sns.countplot(x=column_name, data=df)
        plt.xticks(rotation=45)
        plt.xlabel(column_name)
        plt.ylabel("Count")
        st.pyplot(count_plot.figure)
    elif data[column_name].dtype == 'int64':
        # Create histogram for integer columns
        st.subheader(f"Histogram for {column_name}")
        histogram = plt.hist(data[column_name], bins=10)
        plt.xlabel(column_name)
        plt.ylabel("Frequency")
        fig, ax = plt.subplots()
        ax.hist(data[column_name], bins=10)
        
        # Pass the figure to st.pyplot()
        st.pyplot(fig)

    