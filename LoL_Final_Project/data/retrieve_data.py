import pandas as pd
import numpy as np

def get_local_data():

    # Get data from local disk

    path = "~/LoL-Final-Project/data_cleaned/team_data_cleaned_2022.csv"

    df = pd.read_csv(path)

    return df