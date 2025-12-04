import pandas as pd
import os

def extract_data():
    url = "https://raw.githubusercontent.com/DataTalksClub/nyc-tlc-data/master/yellow/yellow_tripdata_2021-01.csv"
    df = pd.read_csv(url)
    return df

if __name__ == "__main__":
    os.makedirs("artifacts", exist_ok=True)

    df = extract_data()
    df.to_csv("artifacts/extracted_data.csv", index=False)

    print("✔ Extract step completed")
    print(f"Rows extracted: {len(df)}")
