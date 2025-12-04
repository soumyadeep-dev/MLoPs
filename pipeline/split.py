from sklearn.model_selection import train_test_split

def split_data(df):
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    val, test = train_test_split(test, test_size=0.5, random_state=42)
    return train, val, test
