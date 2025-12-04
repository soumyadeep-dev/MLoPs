from sklearn.linear_model import LinearRegression

def train_model(train_df):
    X_train = train_df[['trip_distance']]
    y_train = train_df['duration']

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model
