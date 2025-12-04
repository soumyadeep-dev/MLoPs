from sklearn.metrics import mean_squared_error
import numpy as np

def evaluate_model(model, val_df):
    X_val = val_df[['trip_distance']]
    y_val = val_df['duration']

    preds = model.predict(X_val)
    rmse = np.sqrt(mean_squared_error(y_val, preds))
    return rmse
