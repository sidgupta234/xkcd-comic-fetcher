import streamlit as st
import pandas as pd
#from billboard_seaborn import *
from preprocess import preprocess__
from model_file import get_images
st.set_page_config(layout="wide")
c1, c2= st.columns((1, 3))
header = st.container()
dataset_container = st.container()
# user_input = ""
#modelTraining = st.container()

with header and c1:
    st.title("XKCD Comic fetcher")
    file_name = "xkcd_data.json"
    dataset = preprocess__(file_name)
    user_input = st.text_input("Keyword to look for in comics!")

with c2:
    image_urls = get_images(dataset, user_input)
    st.text(image_urls)
    
    if(user_input!=""):
        for i in image_urls:#min(3,len(image_urls))):
            print(i)
            st.text(i)
            st.image(i, width=None)
            # except:
            #     pass
#with dataset and c2:
    # if user_input and c2:
        

# with dataset and c1:
