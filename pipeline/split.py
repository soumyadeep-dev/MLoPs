import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(df):
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    val, test = train_test_split(test, test_size=0.5, random_state=42)
    return train, val, test

if __name__ == "__main__":
    df = pd.read_csv("artifacts/cleaned_data.csv")

    train_df, val_df, test_df = split_data(df)

    train_df.to_csv("artifacts/train.csv", index=False)
    val_df.to_csv("artifacts/val.csv", index=False)
    test_df.to_csv("artifacts/test.csv", index=False)

    print("✔ Split step completed")
    print(f"Train: {len(train_df)} | Val: {len(val_df)} | Test: {len(test_df)}")
