# Hackathon/clean_data.py
import pandas as pd
import numpy as np

def clean_and_transform_data(raw_file_path='data/raw_data.csv', clean_file_path='data/clean_data.csv'):
    """
    Loads raw delivery data, performs cleaning and transformations,
    and saves the cleaned data to a new CSV file.
    """
    try:
        df = pd.read_csv(raw_file_path)
        print(f"Raw data loaded successfully from {raw_file_path}. Shape: {df.shape}")
    except FileNotFoundError:
        print(f"Error: Raw data file not found at {raw_file_path}.")
        print("Please ensure 'raw_data.csv' (your synthetic data) is in the 'data' folder.")
        return None
    except Exception as e:
        print(f"An error occurred while loading raw data: {e}")
        return None

    # --- Data Cleaning and Type Conversion ---
    df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'])

    # Ensure Hospital_ID is present for outlier analysis or create a dummy one
    if 'Hospital_ID' not in df.columns:
        num_hospitals = 50 # Example: 50 unique hospitals
        df['Hospital_ID'] = np.random.randint(1, num_hospitals + 1, size=len(df))

    # Handle Inter_Delivery_Interval_Months (convert to numeric, categorize)
    df['Inter_Delivery_Interval_Months'] = pd.to_numeric(df['Inter_Delivery_Interval_Months'], errors='coerce')
    # Categorize IDI only for non-first births with valid intervals
    df['IDI_Category'] = pd.cut(df['Inter_Delivery_Interval_Months'],
                                bins=[0, 17.9, 59.9, 121], # Adjusted bins to catch all within range
                                labels=['Short (<18 months)', 'Optimal (18-59 months)', 'Long (60+ months)'],
                                right=True, include_lowest=True,
                                duplicates='drop')

    # Ensure Socio_Economic_Status is categorical for consistent ordering
    ses_order = ['Poorest', 'Poorer', 'Middle', 'Richer', 'Richest']
    df['Socio_Economic_Status'] = pd.Categorical(df['Socio_Economic_Status'], categories=ses_order, ordered=True)

    # Convert ANC_Adequate and Referred_From_Smaller_Facility to Boolean if they aren't already
    df['ANC_Adequate'] = df['ANC_Adequate'].astype(bool)
    df['Referred_From_Smaller_Facility'] = df['Referred_From_Smaller_Facility'].astype(bool)
    df['Patient_Preference_Csection'] = df['Patient_Preference_Csection'].astype(bool)

    # Define categorical order for health worker densities if they are string categories
    doc_density_order = ['Low', 'Medium', 'High']
    df['Doctor_Density_Category'] = pd.Categorical(df['Doctor_Density_Category'], categories=doc_density_order, ordered=True)
    mid_density_order = ['Low', 'Medium', 'High']
    df['Midwife_Density_Category'] = pd.Categorical(df['Midwife_Density_Category'], categories=mid_density_order, ordered=True)

    # Save cleaned data
    try:
        df.to_csv(clean_file_path, index=False)
        print(f"Cleaned data saved successfully to {clean_file_path}. Shape: {df.shape}")
        return df
    except Exception as e:
        print(f"An error occurred while saving cleaned data: {e}")
        return None

if __name__ == "__main__":
    # This block runs when clean_data.py is executed directly
    print("Running data cleaning and transformation...")
    clean_and_transform_data()