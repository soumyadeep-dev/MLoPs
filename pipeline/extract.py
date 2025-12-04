import pandas as pd

def extract_data():
    url = "https://raw.githubusercontent.com/DataTalksClub/nyc-tlc-data/master/yellow_tripdata_2021-01.csv"
    df = pd.read_csv(url)
    return df
