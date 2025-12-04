import pandas as pd
import os

def clean_data(df):
    # Keep valid trip distances
    df = df[df['trip_distance'] > 0]

    # Convert timestamps
    df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    # Compute duration in minutes
    df['duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60

    # Keep reasonable trips
    df = df[(df['duration'] > 1) & (df['duration'] < 60)]

    # Select usable columns for model
    cleaned_df = df[[
        'trip_distance',
        'pickup_longitude',
        'pickup_latitude',
        'dropoff_longitude',
        'dropoff_latitude',
        'duration'
    ]]

    print("Sample cleaned rows:")
    print(cleaned_df.head())

    return cleaned_df

if __name__ == "__main__":
    df = pd.read_csv("artifacts/extracted_data.csv")

    cleaned = clean_data(df)
    cleaned.to_csv("artifacts/cleaned_data.csv", index=False)

    print("✔ Clean step completed")
    print(f"Rows after cleaning: {len(cleaned)}")
