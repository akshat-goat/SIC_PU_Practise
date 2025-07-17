# clean_data.py
import pandas as pd
import numpy as np
import os

def clean_and_prepare_data():
    """
    Loads raw_data.csv, cleans it, engineers features,
    and saves the result to clean_data.csv. [cite: 58]
    """
    try:
        print("Starting data cleaning and preparation...")
        raw_path = 'data/raw_data.csv'
        df = pd.read_csv(raw_path)

        # Correct data types [cite: 77, 100]
        df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'])
        for col in ['Medical_Complication', 'ANC_Adequacy', 'Referred_From_Smaller_Facility', 'Patient_Preference_Csection']:
            df[col] = df[col].astype(bool)

        # Feature Engineering [cite: 77, 101]
        # 1. Time-based features
        df['Delivery_Time_Hour'] = df['Delivery_Date'].dt.hour
        df['Delivery_Day_of_Week'] = df['Delivery_Date'].dt.day_name()

        # 2. Inter-Delivery Interval (IDI) Category
        bins = [0, 18, 60, np.inf]
        labels = ['Short (<18 months)', 'Optimal (18-59 months)', 'Long (60+ months)']
        df['IDI_Category'] = pd.cut(df['Inter_Delivery_Interval_Months'], bins=bins, labels=labels, right=False)

        # 3. Add Hospital_ID for potential outlier analysis
        df['Hospital_ID'] = df.groupby('Hospital_Type').ngroup()
        
        # Save cleaned data
        clean_path = 'data/clean_data.csv'
        df.to_csv(clean_path, index=False)
        print(f"✅ Data cleaning complete. Saved to {clean_path}")
        return True, f"Successfully cleaned and saved {len(df)} records."
        
    except FileNotFoundError:
        error_msg = f"Error: '{raw_path}' not found. Please generate the data first."
        print(f"❌ {error_msg}")
        return False, error_msg
    except Exception as e:
        error_msg = f"An unexpected error occurred: {e}"
        print(f"❌ {error_msg}")
        return False, error_msg

if __name__ == '__main__':
    clean_and_prepare_data()