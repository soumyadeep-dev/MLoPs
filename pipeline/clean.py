import pandas as pd
import os

def clean_data(df):
    df = df[df['trip_distance'] > 0]
    df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    df['duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60

    df = df[(df['duration'] > 1) & (df['duration'] < 60)]

    print("Sample cleaned rows:")
    print(df[['trip_distance','PULocationID','DOLocationID','duration']].head())

    return df[['trip_distance','PULocationID','DOLocationID','duration']]

if __name__ == "__main__":
    df = pd.read_csv("artifacts/extracted_data.csv")

    cleaned = clean_data(df)
    cleaned.to_csv("artifacts/cleaned_data.csv", index=False)

    print("✔ Clean step completed")
    print(f"Rows after cleaning: {len(cleaned)}")
