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
    """Drop missing values from the Dataframe (updated docstring) and changing column names to lower case."""
    df = df.dropna()
    df.columns = df.columns.str.lower()
    return df
