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

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a style='text-align: left;' href="https://www.languageof.me/" target="_blank">Siddharth Gupta</a> | 
All image rights reserved to the very awesome <a style='text-align: center;' href="https://www.xkcd.com/" target="_blank">xkcd</a>
Under <a style='text-align: center;' href="https://xkcd.com/license.html" target="_blank">Attribution-NonCommercial 2.5 License.</a> | 
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fxkcd-fetcher.herokuapp.com&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>
</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

with header and c1:
    st.title("XKCD COMIC FETCHER")
    st.header("Get 1 random Comic")
    file_name = "xkcd_data.json"
    dataset = preprocess__(file_name)
    user_input = st.text_input("Keyword to look for in comics!")
    num_results = st.empty()
    # print(dataset["link"])
    # print(dataset.head())

with c2:
    image_urls, image_link_nums, comic_title = get_images(dataset, user_input)
    num_of_urls = len(image_urls)

with c1 :
    if user_input!="":
        if(num_of_urls>0):
            st.text("Showing 1 image out of " + str(num_of_urls) + " results")
    
with c2:
    if(num_of_urls<=0):
        num_results.text("No results, Sorry to disappoint you") 

    elif(user_input!=""):
        n = random.randint(0,len(image_urls)-1)
        #print("num of images is ", len(image_urls))
        st.header(comic_title[n])
        st.markdown("![Tux, the Linux mascot]("+image_urls[n]+")")
        #st.image(image_urls[n], width=None)
        comic_link = "https://xkcd.com/" + str(image_link_nums[n])
        st.markdown("Permanent Comic Link to share: "+comic_link, unsafe_allow_html=True)
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
