import pandas as pd
import kagglehub
import os
import glob

def extract_data():
    # Download dataset via KaggleHub
    path = kagglehub.dataset_download("elemento/nyc-yellow-taxi-trip-data")
    print("Kaggle dataset downloaded to:", path)

    # Debug: Show all files inside the downloaded folder
    print("\nFiles found inside dataset folder:")
    for root, dirs, files in os.walk(path):
        print(root, files)

    # Recursively find CSV files (KaggleHub uses nested folders)
    csv_files = glob.glob(os.path.join(path, "**", "*.csv"), recursive=True)

    if not csv_files:
        raise FileNotFoundError("❌ No CSV files found inside the Kaggle dataset folder.")

    # Use the first CSV found (usually 'yellow_tripdata_2015-01.csv')
    csv_path = csv_files[0]
    print("\nUsing CSV file:", csv_path)

    # Load CSV
    df = pd.read_csv(csv_path)
    print("✔ Loaded CSV with rows:", len(df))
    return df

if __name__ == "__main__":
    os.makedirs("artifacts", exist_ok=True)

    df = extract_data()
    df.to_csv("artifacts/extracted_data.csv", index=False)

    print("✔ Extract step completed")
