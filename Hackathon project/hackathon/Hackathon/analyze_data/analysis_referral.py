# Hackathon/analyze_data/analysis_referral.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def generate_referral_patterns_plot(df): # <--- THIS LINE MUST START AT THE VERY LEFT EDGE
    """
    Generates a bar chart showing C-section rates by Referral Status.
    Returns the matplotlib Figure object.
    """
    referral_delivery_counts = df.groupby(['Referred_From_Smaller_Facility', 'Delivery_Type']).size().unstack(fill_value=0)
    referral_delivery_counts['Total'] = referral_delivery_counts.sum(axis=1)
    referral_delivery_counts['C-section_Rate'] = (referral_delivery_counts['C-section'] / referral_delivery_counts['Total']) * 100

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=referral_delivery_counts.index, y='C-section_Rate', data=referral_delivery_counts, palette='magma',
                hue=referral_delivery_counts.index, legend=False, ax=ax)
    ax.set_title('C-section Rate by Referral Status')
    ax.set_xlabel('Referred from Smaller Facility (True/False)')
    ax.set_ylabel('C-section Rate (%)')
    ax.set_xticks(ticks=[0, 1], labels=['Direct Admission', 'Referred'])
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    fig.tight_layout()
    return fig

if __name__ == "__main__":
    # For standalone testing
    try:
        from clean_data import clean_and_transform_data
        BASE_DIR = Path(__file__).resolve().parent
        df = clean_and_transform_data(
            raw_file_path=BASE_DIR.parent / 'data' / 'raw_data.csv',
            clean_file_path=BASE_DIR.parent / 'data' / 'clean_data_test.csv')
        if df is not None:
            fig = generate_referral_patterns_plot(df)
            plt.show()
    except ImportError:
        print("Could not import clean_data. Please ensure clean_data.py is accessible for direct testing.")
    except FileNotFoundError:
        print("Raw data not found for direct testing. Ensure ../data/raw_data.csv exists.")