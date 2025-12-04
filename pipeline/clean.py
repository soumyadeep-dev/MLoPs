def clean_data(df):
    df = df[df['trip_distance'] > 0]
    df['pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    df['duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60

    df = df[(df['duration'] > 1) & (df['duration'] < 60)]
    print("df")

    return df[['trip_distance','PULocationID','DOLocationID','duration']]
