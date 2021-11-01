import streamlit as st
import pandas as pd 
@st.cache
def preprocess__(file_name):
    data_df = pd.read_json(file_name)
    return data_df