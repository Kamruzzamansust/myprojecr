import streamlit as st
import pandas as pd 
import requests


@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df





# Function to make a request to FastAPI backend
def get_data_from_fastapi(FASTAPI_URL):
    response = requests.get(FASTAPI_URL + "data")
    if response.status_code == 200:
        data = response.json()
        data = pd.DataFrame(data) 
        return data
    else:
        st.error("Failed to fetch data from FastAPI backend")


def calculate_missing_values(data):
    if data is not None:
        df = pd.DataFrame(data)
        missing_values = df.isnull().sum()
        return missing_values
    else:
        return None


# Function to extract data types from the data
def get_info(data):
    if data is not None and not data.empty:
        # Assuming data is a DataFrame, we can extract the data types of columns
        data_types_df = pd.DataFrame(data.dtypes, columns=['Data Types'])
        return data_types_df
    else:
        return None




