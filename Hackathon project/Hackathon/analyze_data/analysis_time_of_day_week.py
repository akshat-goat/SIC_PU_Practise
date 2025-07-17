# Hackathon/analyze_data/analysis_time_of_day_week.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def generate_time_of_day_week_heatmap(df):
    """
    Generates a heatmap showing C-section rates by Hour of Day and Day of Week.
    Returns the matplotlib Figure object.
    """
    # Ensure relevant columns are correctly set by clean_data.py
    # Re-calculate here defensively if clean_data.py was skipped in direct testing
    if 'Delivery_Time_Hour' not in df.columns or 'Delivery_Day_of_Week' not in df.columns:
        df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'])
        df['Delivery_Time_Hour'] = df['Delivery_Date'].dt.hour
        df['Delivery_Day_of_Week'] = df['Delivery_Date'].dt.day_name()


    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['Delivery_Day_of_Week'] = pd.Categorical(df['Delivery_Day_of_Week'], categories=day_order, ordered=True)

    csection_counts = df[df['Delivery_Type'] == 'C-section'].groupby(['Delivery_Day_of_Week', 'Delivery_Time_Hour']).size()
    total_counts = df.groupby(['Delivery_Day_of_Week', 'Delivery_Time_Hour']).size()

    csection_rate_matrix = (csection_counts / total_counts).unstack(fill_value=np.nan) * 100 # Use NaN for missing
    
    # Ensure all hours 0-23 are present as columns, fill with NaN if no data
    for hour in range(24):
        if hour not in csection_rate_matrix.columns:
            csection_rate_matrix[hour] = np.nan
    csection_rate_matrix = csection_rate_matrix.reindex(columns=range(24))

    # Sort rows by day order
    csection_rate_matrix = csection_rate_matrix.reindex(day_order)

    fig, ax = plt.subplots(figsize=(14, 8))
    sns.heatmap(csection_rate_matrix, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=.5, ax=ax,
                cbar_kws={'label': 'C-section Rate (%)'}, annot_kws={"size": 8})
    ax.set_title('C-section Rate (%) by Day of Week and Hour of Day')
    ax.set_xlabel('Hour of Day (24-hour)')
    ax.set_ylabel('Day of Week')
    fig.tight_layout()
    return fig

if __name__ == "__main__":
    # For standalone testing
    from clean_data import clean_and_transform_data
    df = clean_and_transform_data(raw_file_path='../data/raw_data.csv', clean_file_path='../data/clean_data_test.csv')
    if df is not None:
        fig = generate_time_of_day_week_heatmap(df)
        plt.show()