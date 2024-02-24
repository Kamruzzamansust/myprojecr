import pandas as pd 
import streamlit as st 
import requests
from src.loding_data import * #load_data, get_data_from_fastapi,calculate_missing_values,get_info




st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


FASTAPI_URL = "http://127.0.0.1:8000/"

df=load_data('Data\data.csv')
#st.write(df.head(10))

col1, col2, col3 = st.columns([2, 2, 2])





# Function to make a request to FastAPI backend

with col1:
    col4, col5 = st.columns([8,4])

    with col4:
        st.markdown("""
        <style>
        div.stButton > button:first-child { 
            color: black;
            border-radius: 5%;
            background-color: #75C4EE; /* Corrected typo in background-color */
            height: 5rm;
            width: 5rm; 
            box-shadow: 2px 2px 4px rgba(0, 0, 1, 0.5);        
        }
        </style>
        """, unsafe_allow_html=True)

        
        
        st.write("DataFrame Name 'STUDENT PERFORMANCE'")
        # Button to trigger request to FastAPI backend
        if st.button("See Dataframe"):
            data = get_data_from_fastapi(FASTAPI_URL)
            if data is not None:
                with st.expander("This is the Dataframe", expanded=True):



                    st.data_editor(data,width=1000,disabled=False)
    with st.container(border=True):
        col6, col7,col8 = st.columns([2,2,2])
        with col6:
            st.text('Observation')
            st.write("---")
            st.subheader(df.shape[0])
        with col7:
            st.text(' ')
            st.write(" ")
        with col8:
            st.text('Data Source')
            st.write("---")
            st.subheader("kaggle")


with col2:
        with st.container(border=True):

            with st.expander("Data Information"):
                st.markdown("""
            - **gender**: Sex of students (Male/Female)
            - **race/ethnicity**: Ethnicity of students (Group A, B, C, D, E)
            - **parental level of education**: Parents' final education (Bachelor's degree, Some college, Master's degree, Associate's degree, High school)
            - **lunch**: Having lunch before the test (Standard or Free/Reduced)
            - **test preparation course**: Complete or not complete before the test
            - **math score**: Score in Math
            - **reading score**: Score in Reading
            - **writing score**: Score in Writing
            """)
                
           

           
            with st.expander("Missing Values"):
                    if st.button("Check Mising Values"):
                        data = get_data_from_fastapi(FASTAPI_URL)
                        if data is not None:
                            missing_values = calculate_missing_values(data)
                            if missing_values is not None:
                                    st.write("Missing Values:")
                                    st.write(missing_values)
                            else:
                                    st.write("No missing values.")
            
            with st.expander("Check data types"):
                 if st.button("data types"):
                        data = get_data_from_fastapi(FASTAPI_URL)
                        if data is not None:
                            data_type = get_info(data)
                            if data_type is not None:
                                    st.write("Data type:")
                                    st.write(data_type)
                            
            
                            





    





