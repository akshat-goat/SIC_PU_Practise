import pandas as pd

def clean_data(df):
    """
    Cleans the raw delivery data: handles missing values, converts types,
    and standardizes categorical entries.
    """
    print("Starting data cleaning...")

    # 1. Handle Missing Values (Example strategy: simple imputation/removal)
    # For simplicity, let's fill numerical NaNs with median and categorical with mode.
    # More sophisticated strategies might be needed based on actual data.
    for col in ['maternal_age', 'gestational_age', 'birth_weight']:
        if col in df.columns:
            df[col].fillna(df[col].median(), inplace=True)

    for col in ['hospital_type', 'previous_delivery_type', 'medical_complications_maternal', 'medical_complications_fetal']:
        if col in df.columns:
            df[col].fillna('Unknown', inplace=True) # Or mode()

    # Remove rows where primary keys or essential columns are missing
    df.dropna(subset=['delivery_id', 'delivery_type', 'hospital_id', 'delivery_date'], inplace=True)

    # 2. Data Type Conversion
    if 'delivery_date' in df.columns:
        df['delivery_date'] = pd.to_datetime(df['delivery_date'], errors='coerce')
        df.dropna(subset=['delivery_date'], inplace=True) # Remove rows with invalid dates

    categorical_cols = ['delivery_type', 'hospital_type', 'previous_delivery_type',
                        'hospital_location', 'doctor_id'] # Add other relevant categorical cols
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype('category')

    numerical_cols = ['maternal_age', 'parity', 'gestational_age', 'birth_weight']
    for col in numerical_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df.dropna(subset=[col], inplace=True)

    # 3. Data Standardization
    if 'delivery_type' in df.columns:
        df['delivery_type'] = df['delivery_type'].str.lower().replace({'c-section': 'C-section', 'normal': 'Normal', 'vaginal': 'Normal', 'natural': 'Normal'}).astype('category')
        df = df[df['delivery_type'].isin(['Normal', 'C-section'])] # Keep only valid types

    print("Data cleaning completed.")
    print(df.info())
    return df

if __name__ == '__main__':
    # Example Usage: Create a dummy dataframe for testing
    dummy_data = {
        'delivery_id': range(1, 10),
        'delivery_date': ['2023-01-15', '2023-02-20', '2023-01-25', '2023-03-10', '2023-04-05', 'invalid_date', '2023-05-12', '2023-06-01', '2023-07-07'],
        'delivery_type': ['Normal', 'C-SECTION', 'normal', 'C-section', 'Vaginal', 'Normal', 'C-section', 'NORMAL', 'C-section'],
        'hospital_id': ['H1', 'H2', 'H1', 'H3', 'H2', 'H1', 'H3', 'H2', 'H1'],
        'hospital_type': ['Public', 'Private', 'Public', 'Private', 'Public', 'Private', 'Public', 'Private', 'Public'],
        'maternal_age': [25, 32, 28, 35, 29, None, 30, 27, 33],
        'previous_delivery_type': [None, 'Normal', 'C-section', 'Normal', 'C-section', 'Normal', 'C-section', 'Normal', 'C-section']
    }
    dummy_df = pd.DataFrame(dummy_data)
    cleaned_df = clean_data(dummy_df.copy())
    print("\nCleaned DataFrame Head:")
    print(cleaned_df.head())