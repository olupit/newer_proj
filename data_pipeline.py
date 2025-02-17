import pandas as pd

def load_data(filepath):
    """Load CSV data into a Pandas DataFrame."""
    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """Drop missing values from the Dataframe (updated docstring)."""
    df = df.dropna()
    return df

def handle_missing_values(df):
    """Fill missing values with column mean."""
    return df.fillna(df.mean())