import pandas as pd
import pickle
import numpy as np
from sklearn.metrics import mean_squared_error

def evaluate_model(model, val_df):
    X_val = val_df[[
        'trip_distance',
        'pickup_longitude',
        'pickup_latitude',
        'dropoff_longitude',
        'dropoff_latitude'
    ]]
    y_val = val_df['duration']

    preds = model.predict(X_val)
    rmse = np.sqrt(mean_squared_error(y_val, preds))

    print("Validation RMSE:", rmse)
    return rmse

if __name__ == "__main__":
    val_df = pd.read_csv("artifacts/val.csv")

    with open("artifacts/model.pkl", "rb") as f:
        model = pickle.load(f)

    rmse = evaluate_model(model, val_df)

    with open("artifacts/metrics.txt", "w") as f:
        f.write(f"rmse={rmse}")

    print("✔ Evaluate step completed")
