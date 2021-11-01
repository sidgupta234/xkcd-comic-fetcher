import pandas as pd
import re

def get_images(dataset, user_input):
    data_df_required = dataset.dropna()
    #user_input = " " + user_input + " "
    data_df_required = dataset.loc[dataset['transcript'].str.contains(fr'\b{user_input}\b')]
    return data_df_required["img"].tolist()