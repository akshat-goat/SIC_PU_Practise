# data_generator_initial.py
import pandas as pd
import numpy as np
import os

def generate_raw_data():
    """
    Generates a synthetic raw_data.csv file with 50,000 records
    based on the project description.
    """
    print("Generating raw synthetic data...")
    NUM_RECORDS = 50000

    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Base attributes based on [cite: 31]
    data = {
        'Patient_ID': range(1, NUM_RECORDS + 1),
        'Maternal_Age': np.random.randint(18, 45, size=NUM_RECORDS),
        'Birth_Order': np.random.randint(1, 6, size=NUM_RECORDS),
        'Residence': np.random.choice(['Urban', 'Rural'], size=NUM_RECORDS, p=[0.4, 0.6]),
        'Hospital_Type': np.random.choice(['Private', 'Public'], size=NUM_RECORDS, p=[0.6, 0.4]),
        'Socio_Economic_Status': np.random.choice(['Low', 'Middle', 'High'], size=NUM_RECORDS, p=[0.4, 0.4, 0.2]),
        'Medical_Complication': np.random.choice([True, False], size=NUM_RECORDS, p=[0.25, 0.75]),
        'Delivery_Date': pd.to_datetime(np.random.randint(pd.to_datetime('2022-01-01').value, pd.to_datetime('2024-12-31').value, size=NUM_RECORDS)),
        'ANC_Adequacy': np.random.choice([True, False], size=NUM_RECORDS, p=[0.7, 0.3]),
        'Referred_From_Smaller_Facility': np.random.choice([True, False], size=NUM_RECORDS, p=[0.2, 0.8]),
        'Doctor_Density_Category': np.random.choice(['Low', 'Medium', 'High'], size=NUM_RECORDS),
        'Midwife_Density_Category': np.random.choice(['Low', 'Medium', 'High'], size=NUM_RECORDS),
        'Patient_Preference_Csection': np.random.choice([True, False], size=NUM_RECORDS, p=[0.15, 0.85]),
    }

    df = pd.DataFrame(data)

    # Generate correlated Delivery_Type [cite: 19]
    # Base probability of C-section
    prob_c_section = 0.35  # National average baseline
    prob_c_section += np.where(df['Hospital_Type'] == 'Private', 0.20, -0.10)
    prob_c_section += np.where(df['Medical_Complication'], 0.30, 0)
    prob_c_section += np.where(df['Maternal_Age'] > 35, 0.15, 0)
    prob_c_section += np.where(df['Patient_Preference_Csection'], 0.40, 0)
    prob_c_section = np.clip(prob_c_section, 0.05, 0.95)

    df['Delivery_Type'] = np.where(np.random.rand(NUM_RECORDS) < prob_c_section, 'C-section', 'Normal')

    # Add Inter-Delivery Interval for non-first births [cite: 31]
    df['Inter_Delivery_Interval_Months'] = np.nan
    non_first_birth_mask = df['Birth_Order'] > 1
    num_non_first = non_first_birth_mask.sum()
    df.loc[non_first_birth_mask, 'Inter_Delivery_Interval_Months'] = np.random.randint(12, 72, size=num_non_first)
    
    # Save to CSV
    file_path = 'data/raw_data.csv'
    df.to_csv(file_path, index=False)
    print(f"✅ Successfully generated {NUM_RECORDS} records and saved to {file_path}")

if __name__ == '__main__':
    generate_raw_data()