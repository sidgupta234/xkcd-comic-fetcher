import pandas as pd
import re

def get_images(dataset, user_input):
    data_df_required = dataset.copy()
    #print(len(data_df_required))
    #user_input = " " + user_input + " "
    user_input = user_input.lower()
   # data_df_required
    #data_df_required['transcript'] = data_df_required['transcript'].str.lower()  
    query = re.escape(user_input)
    data_df_required = dataset.loc[dataset['transcript'].str.contains(fr'\b{query}\b')]
    return data_df_required["img"].tolist(), data_df_required["num"].tolist(), data_df_required["title"].tolist()