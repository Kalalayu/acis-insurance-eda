import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath, sep="|", low_memory=False)
    return df

def clean_data(df):
    # Remove exact duplicates only
    df = df.drop_duplicates()

    # Do NOT drop all rows with missing values.
    # Instead, keep missing values to analyze them later.
    
    # Trim spaces in string columns
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Convert date columns
    df["TransactionMonth"] = pd.to_datetime(df["TransactionMonth"], errors="coerce")

    return df

if __name__ == "__main__":
    df = load_data("data/raw/MachineLearningRating_v3.txt")
    df = clean_data(df)
    print(df.head())
    print(df.info())
