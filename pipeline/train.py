import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

def train_model(train_df):
    X_train = train_df[[
        'trip_distance',
        'pickup_longitude',
        'pickup_latitude',
        'dropoff_longitude',
        'dropoff_latitude'
    ]]
    y_train = train_df['duration']

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

if __name__ == "__main__":
    train_df = pd.read_csv("artifacts/train.csv")

    model = train_model(train_df)

    with open("artifacts/model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("✔ Train step completed")
