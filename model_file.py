import pandas as pd
import re

def get_images(dataset, user_input):
    data_df_required = dataset.dropna().copy()
    #user_input = " " + user_input + " "
    user_input = user_input.lower()
   # data_df_required
    #data_df_required['transcript'] = data_df_required['transcript'].str.lower()  
    data_df_required = dataset.loc[dataset['transcript'].str.contains(fr'\b{user_input}\b')]
    return data_df_required["img"].tolist()