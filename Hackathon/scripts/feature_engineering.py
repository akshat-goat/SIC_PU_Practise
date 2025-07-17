import pandas as pd

def engineer_features(df):
    """
    Engineers new features from the cleaned delivery data, including
    seasonal indicators and comparative delivery rates.
    """
    print("Starting feature engineering...")

    # Ensure delivery_date is datetime
    if 'delivery_date' in df.columns and not pd.api.types.is_datetime64_any_dtype(df['delivery_date']):
        df['delivery_date'] = pd.to_datetime(df['delivery_date'], errors='coerce')
        df.dropna(subset=['delivery_date'], inplace=True)

    # 1. Extract Temporal Features
    df['delivery_month'] = df['delivery_date'].dt.month
    df['delivery_year'] = df['delivery_date'].dt.year
    df['delivery_quarter'] = df['delivery_date'].dt.quarter

    # Define seasons (example for India, can be refined)
    def get_season(month):
        if month in [12, 1, 2]: return 'Winter'
        elif month in [3, 4, 5]: return 'Summer'
        elif month in [6, 7, 8, 9]: return 'Monsoon'
        else: return 'Post-Monsoon'
    df['delivery_season'] = df['delivery_month'].apply(get_season)

    # 2. Create Binary Flags for Delivery Types
    df['is_c_section'] = (df['delivery_type'] == 'C-section').astype(int)
    df['is_normal_delivery'] = (df['delivery_type'] == 'Normal').astype(int)

    # 3. Calculate Comparative Rates (Pre-calculated for Flask app)
    # Overall Rates
    total_deliveries = df.shape[0]
    overall_csection_count = df['is_c_section'].sum()
    overall_normal_count = df['is_normal_delivery'].sum()
    overall_rates = {
        'normal_percentage': (overall_normal_count / total_deliveries * 100) if total_deliveries else 0,
        'csection_percentage': (overall_csection_count / total_deliveries * 100) if total_deliveries else 0
    }
    print(f"Overall Rates: {overall_rates}")

    # Rates per State/Location
    if 'hospital_location' in df.columns:
        state_rates = df.groupby('hospital_location').agg(
            total_deliveries=('delivery_id', 'count'),
            csection_count=('is_c_section', 'sum'),
            normal_count=('is_normal_delivery', 'sum')
        ).reset_index()
        state_rates['C_section_Rate'] = (state_rates['csection_count'] / state_rates['total_deliveries'] * 100).round(2)
        state_rates['Normal_Delivery_Rate'] = (state_rates['normal_count'] / state_rates['total_deliveries'] * 100).round(2)
        state_rates = state_rates[['hospital_location', 'C_section_Rate', 'Normal_Delivery_Rate']]
        print("State Rates calculated.")
    else:
        state_rates = pd.DataFrame(columns=['hospital_location', 'C_section_Rate', 'Normal_Delivery_Rate'])
        print("hospital_location column not found, skipping state rates.")


    # Rates per Hospital
    if 'hospital_id' in df.columns and 'hospital_type' in df.columns:
        hospital_rates = df.groupby(['hospital_id', 'hospital_type']).agg(
            total_deliveries=('delivery_id', 'count'),
            csection_count=('is_c_section', 'sum'),
            normal_count=('is_normal_delivery', 'sum')
        ).reset_index()
        hospital_rates['C_section_Rate'] = (hospital_rates['csection_count'] / hospital_rates['total_deliveries'] * 100).round(2)
        hospital_rates['Normal_Delivery_Rate'] = (hospital_rates['normal_count'] / hospital_rates['total_deliveries'] * 100).round(2)
        hospital_rates = hospital_rates[['hospital_id', 'hospital_type', 'C_section_Rate', 'Normal_Delivery_Rate']]
        print("Hospital Rates calculated.")
    else:
        hospital_rates = pd.DataFrame(columns=['hospital_id', 'hospital_type', 'C_section_Rate', 'Normal_Delivery_Rate'])
        print("hospital_id or hospital_type column not found, skipping hospital rates.")


    # Rates per Season/Month
    seasonal_trends = df.groupby('delivery_season').agg(
        total_deliveries=('delivery_id', 'count'),
        csection_count=('is_c_section', 'sum'),
        normal_count=('is_normal_delivery', 'sum')
    ).reset_index()
    seasonal_trends['C_section_Rate'] = (seasonal_trends['csection_count'] / seasonal_trends['total_deliveries'] * 100).round(2)
    seasonal_trends['Normal_Delivery_Rate'] = (seasonal_trends['normal_count'] / seasonal_trends['total_deliveries'] * 100).round(2)
    print("Seasonal Trends calculated.")

    # 4. Parity Analysis Feature
    if 'parity' in df.columns and 'previous_delivery_type' in df.columns:
        df['previous_c_section_flag'] = ((df['parity'] > 0) & (df['previous_delivery_type'] == 'C-section')).astype(int)
        print("Parity feature engineered.")
    else:
        print("Parity or previous_delivery_type column not found, skipping parity feature engineering.")


    print("Feature engineering completed.")
    return df, overall_rates, state_rates, hospital_rates, seasonal_trends

if __name__ == '__main__':
    # Example Usage: Using a dummy DataFrame (similar to what clean_data would output)
    dummy_data_cleaned = {
        'delivery_id': range(1, 20),
        'delivery_date': pd.to_datetime([f'2023-{m:02d}-15' for m in ([1]*5 + [7]*5 + [10]*5 + [4]*4)]),
        'delivery_type': ['Normal', 'C-section', 'Normal', 'C-section', 'Normal'] * 4,
        'hospital_id': ['H1', 'H2', 'H1', 'H3', 'H2'] * 4,
        'hospital_name': ['Gen Hospital A', 'City Clinic B', 'Gen Hospital A', 'Private Hos C', 'City Clinic B'] * 4,
        'hospital_type': ['Public', 'Private', 'Public', 'Private', 'Public'] * 4,
        'hospital_location': ['MH', 'KA', 'MH', 'DL', 'KA'] * 4, # Maharashtra, Karnataka, Delhi
        'maternal_age': [25, 32, 28, 35, 29, 30, 27, 33, 26, 31, 28, 34, 29, 30, 27, 33, 26, 31, 28],
        'parity': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        'previous_delivery_type': [None, 'Normal', None, 'C-section', None, 'Normal', None, 'C-section', None, 'Normal', None, 'C-section', None, 'Normal', None, 'C-section', None, 'Normal', None]
    }
    dummy_df_eng = pd.DataFrame(dummy_data_cleaned)
    df_engineered, overall, states, hospitals, seasonal = engineer_features(dummy_df_eng.copy())
    print("\nEngineered DataFrame Head:")
    print(df_engineered.head())
    print("\nState Rates:")
    print(states)
    print("\nHospital Rates:")
    print(hospitals)
    print("\nSeasonal Trends:")
    print(seasonal)