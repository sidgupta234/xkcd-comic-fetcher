##### Libraries #####
import streamlit as st
import pandas as pd
import numpy as np
##### Libraries #####

##### Page config #####
# Wide Layout uses entire screen (I prefer),
# Centered restricts to centre 
st.set_page_config(page_title='Comic Fetcher', 
page_icon = "favicon.png", 
layout = 'wide', 
initial_sidebar_state = 'auto')
##### Page config #####

##### Columns #####
# c1, c2, c3= st.columns((1, 2, 1))

# with c1:
#     st.write("hello")

# with c2:
#     st.write("Pyjamas")
#     #st.markdown("<p style = 'text-align: center'> Pyjamas </p>", unsafe_allow_html=True)
    
# with c3:
#     st.write("World")

##### Columns #####

##### Container #####

# c1, c2= st.columns((1, 2))

# header = st.container()

# with header and c1:
#     st.title("XKCD COMIC FETCHER")
#     st.header("Get 1 random Comic")

##### Container #####

##### Text Display Types #####

# c1, c2 = st.columns((1, 2))

# with c1:
#     st.markdown("<i>Markdown: We are having fun in Pyjamas</i>", unsafe_allow_html=True)
#     st.title("Title: We are having fun in Pyjamas")
#     st.header("Header: We are having fun in Pyjamas")
#     st.subheader("Subheader: We are having fun in Pyjamas")
#     st.caption("Caption: We are having fun in Pyjamas")
#     st.code("Code: print(We are having fun in Pyjamas)")
#     st.text("Text: We are having fun in Pyjamas")
#     st.latex("Latex (x^2 + y^2 = z^2)")

##### Text Display Types #####

##### Input Widgets #####

# c1, c2 = st.columns((1, 2))

# with c1:
    
#     if st.button('press'):
#         st.write('Button pressed')
#     else:
#         st.write('Button never pressed')
    
#     text_input = st.text_input("Enter your name")
#     st.write("your name is ...", text_input)


##### Input Widgets #####

##### Charts #####

# c1, c2 = st.columns((1, 2))

# with c1:

#     chart_data = pd.DataFrame(
#         np.random.randn(20, 2),
#         columns=["a", "b"])

#     st.bar_chart(chart_data)

##### Charts #####

##### Media #####

# c1, c2 = st.columns((1, 2))

# with c1:
#     st.image("https://i.imgur.com/q5xmsD1.png")


##### Media #####

# # #from billboard_seaborn import *
# # # from preprocess import preprocess__
# # # from model_file import get_images
# # # import random
# # #st.set_page_config(layout="wide")

# # # user_input = ""
# # #modelTraining = st.container()

# # footer="""<style>
# # a:link , a:visited{
# # color: blue;
# # background-color: transparent;
# # text-decoration: underline;
# # }

# # a:hover,  a:active {
# # color: red;
# # background-color: transparent;
# # text-decoration: underline;
# # }

# # .footer {
# # position: fixed;
# # left: 0;
# # bottom: 0;
# # width: 100%;
# # background-color: white;
# # color: black;
# # text-align: center;
# # }
# # </style>
# # <div class="footer">
# # <p>Developed by <a style='text-align: left;' href="https://www.languageof.me/" target="_blank">Siddharth Gupta</a> | 
# # All image rights reserved to the very awesome <a style='text-align: center;' href="https://www.xkcd.com/" target="_blank">xkcd</a>
# # Under <a style='text-align: center;' href="https://xkcd.com/license.html" target="_blank">Attribution-NonCommercial 2.5 License.</a> | 
# # <a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fxkcd-fetcher.herokuapp.com&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>
# # </p>
# # </div>
# # """
# # st.markdown(footer, unsafe_allow_html=True)

# # with header and c1:
# #     st.title("XKCD COMIC FETCHER")
# #     st.header("Get 1 random Comic")
# #     file_name = "xkcd_data.json"
# #     dataset = preprocess__(file_name)
# #     user_input = st.text_input("Keyword to look for in comics!")
# #     num_results = st.empty()
# #     # print(dataset["link"])
# #     # print(dataset.head())

# # with c2:
# #     image_urls, image_link_nums, comic_title = get_images(dataset, user_input)
# #     num_of_urls = len(image_urls)

# # with c1 :
# #     if user_input!="":
# #         if(num_of_urls>0):
# #             st.text("Showing 1 image out of " + str(num_of_urls) + " results")
    
# # with c2:
# #     if(num_of_urls<=0):
# #         num_results.text("No results, Sorry to disappoint you") 

# #     elif(user_input!=""):
# #         n = random.randint(0,len(image_urls)-1)
# #         #print("num of images is ", len(image_urls))
# #         st.header(comic_title[n])
# #         st.markdown("![Tux, the Linux mascot]("+image_urls[n]+")")
# #         #st.image(image_urls[n], width=None)
# #         comic_link = "https://xkcd.com/" + str(image_link_nums[n])
# #         st.markdown("Permanent Comic Link to share: "+comic_link, unsafe_allow_html=True)
# #     #st.text(image_urls)
    
# #     # if(user_input!=""):
# #     #     for i in image_urls:#min(3,len(image_urls))):
# #     #         print(i)
# #     #         st.text(i)
# #     #         st.image(i, width=None)
# #     #         # except:
# #     #         #     pass
# # #with dataset and c2:
# #     # if user_input and c2:
        

# # # with dataset and c1:
