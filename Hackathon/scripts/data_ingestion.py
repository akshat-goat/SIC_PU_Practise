import pandas as pd
try:
    import pyreadstat
except ImportError:
    print("pyreadstat not found. Install it for .sav file support: pip install pyreadstat")

def load_raw_data(filepath):
    """
    Loads raw data from a specified filepath.
    Supports CSV and SPSS (.sav) formats.
    """
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith('.sav'):
        # For .sav files (SPSS), pyreadstat is often needed
        df, meta = pyreadstat.read_sav(filepath)
        # You might need to handle value labels from meta for categorical variables
    else:
        raise ValueError("Unsupported file format. Please provide .csv or .sav")
    print(f"Successfully loaded data from {filepath}")
    print(df.head())
    print(df.info())
    return df

if __name__ == '__main__':
    # Example Usage:
    # Assuming you have an NFHS-5.sav or synthetic_data.csv in the data folder
    # raw_df = load_raw_data('../data/NFHS-5.sav')
    # raw_df = load_raw_data('../data/synthetic_delivery_data.csv')
    pass