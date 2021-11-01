import streamlit as st
import pandas as pd
#from billboard_seaborn import *
from preprocess import preprocess__
from model_file import get_images
import random
#st.set_page_config(layout="wide")
st.set_page_config(page_title='Comic Fetcher', page_icon = "favicon.png", layout = 'wide', initial_sidebar_state = 'auto')
c1, c2= st.columns((1, 2))
header = st.container()
dataset_container = st.container()

# user_input = ""
#modelTraining = st.container()

with header and c1:
    st.title("XKCD Comic fetcher")
    st.header("Get 1 random XKCD Comic!")
    file_name = "xkcd_data.json"
    dataset = preprocess__(file_name)
    user_input = st.text_input("Keyword to look for in comics!")
    num_results = st.empty()

with c2:
    image_urls = get_images(dataset, user_input)
    num_of_urls = len(image_urls)

with c1 :
    if user_input!="":
        st.text("total search results: " + str(num_of_urls))
    
with c2:
    if(num_of_urls<=0):
        num_results.text("Sorry that xkcd disappointed you") 

    elif(user_input!=""):
        n = random.randint(0,len(image_urls)-1)
        print("num of images is ", n+1)
        st.image(image_urls[n], width=None)
    #st.text(image_urls)
    
    # if(user_input!=""):
    #     for i in image_urls:#min(3,len(image_urls))):
    #         print(i)
    #         st.text(i)
    #         st.image(i, width=None)
    #         # except:
    #         #     pass
#with dataset and c2:
    # if user_input and c2:
        

# with dataset and c1:
