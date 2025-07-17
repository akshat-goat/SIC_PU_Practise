import pandas as pd

def get_overall_prevalence(df):
    """
    Calculates the overall national percentages for Normal vs. C-section deliveries.
    Assumes 'is_normal_delivery' and 'is_c_section' flags are present.
    """
    if 'is_normal_delivery' not in df.columns or 'is_c_section' not in df.columns:
        raise ValueError("DataFrame must contain 'is_normal_delivery' and 'is_c_section' columns.")

    total_deliveries = df.shape[0]
    if total_deliveries == 0:
        return {"normal_percentage": 0, "csection_percentage": 0}

    normal_count = df['is_normal_delivery'].sum()
    csection_count = df['is_c_section'].sum()

    normal_percentage = (normal_count / total_deliveries) * 100
    csection_percentage = (csection_count / total_deliveries) * 100

    print(f"Overall Prevalence: Normal={normal_percentage:.2f}%, C-section={csection_percentage:.2f}%")
    return {
        "normal_percentage": round(normal_percentage, 2),
        "csection_percentage": round(csection_percentage, 2)
    }

if __name__ == '__main__':
    # Example Usage:
    dummy_df = pd.DataFrame({
        'is_normal_delivery': [1, 0, 1, 1, 0, 1, 0, 1, 0],
        'is_c_section': [0, 1, 0, 0, 1, 0, 1, 0, 1]
    })
    overall_stats = get_overall_prevalence(dummy_df)
    print(f"Overall stats: {overall_stats}")