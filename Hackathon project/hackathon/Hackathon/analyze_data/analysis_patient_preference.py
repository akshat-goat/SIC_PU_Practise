# Hackathon/analyze_data/analysis_patient_preference.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def generate_patient_preference_plot(df):
    """
    Generates a bar chart showing C-section rates by Patient Preference for C-section.
    Returns the matplotlib Figure object.
    """
    preference_delivery_counts = df.groupby(['Patient_Preference_Csection', 'Delivery_Type']).size().unstack(fill_value=0)
    preference_delivery_counts['Total'] = preference_delivery_counts.sum(axis=1)
    preference_delivery_counts['C-section_Rate'] = (preference_delivery_counts['C-section'] / preference_delivery_counts['Total']) * 100

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=preference_delivery_counts.index, y='C-section_Rate', data=preference_delivery_counts, palette='cividis',
                hue=preference_delivery_counts.index, legend=False, ax=ax)
    ax.set_title('C-section Rate by Patient Preference for C-section')
    ax.set_xlabel('Patient Preferred C-section (True/False)')
    ax.set_ylabel('C-section Rate (%)')
    ax.set_xticks(ticks=[0, 1], labels=['Preferred Normal', 'Preferred C-section'])
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    fig.tight_layout()
    return fig

if __name__ == "__main__":
    # For standalone testing
    from clean_data import clean_and_transform_data
    BASE_DIR = Path(__file__).resolve().parent
    df = clean_and_transform_data(
        raw_file_path=BASE_DIR.parent / 'data' / 'raw_data.csv',
        clean_file_path=BASE_DIR.parent / 'data' / 'clean_data_test.csv')
    if df is not None:
        fig = generate_patient_preference_plot(df)
        plt.show()