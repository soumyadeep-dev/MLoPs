import pandas as pd
import kagglehub
import os
import glob

def extract_data():
    # Download dataset via KaggleHub
    path = kagglehub.dataset_download("elemento/nyc-yellow-taxi-trip-data")
    print("Kaggle dataset downloaded to:", path)

    # Find a CSV file inside the downloaded folder
    csv_files = glob.glob(os.path.join(path, "*.csv"))

    if not csv_files:
        raise FileNotFoundError("❌ No CSV files found inside the Kaggle dataset folder.")

    # Use the first CSV file found
    csv_path = csv_files[0]
    print("Using CSV file:", csv_path)

    # Read CSV into DataFrame
    df = pd.read_csv(csv_path)

    return df

if __name__ == "__main__":
    os.makedirs("artifacts", exist_ok=True)

    df = extract_data()
    df.to_csv("artifacts/extracted_data.csv", index=False)

    print("✔ Extract step completed")
    print(f"Rows extracted: {len(df)}")
