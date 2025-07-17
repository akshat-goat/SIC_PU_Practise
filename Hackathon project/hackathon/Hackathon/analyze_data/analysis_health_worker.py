# Hackathon/analyze_data/analysis_health_worker.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def generate_health_worker_impact_plot(df):
    """
    Generates bar charts showing C-section rates by Doctor and Midwife Density Categories.
    Returns the matplotlib Figure object.
    """
    # Doctor Density
    doc_density_counts = df.groupby(['Doctor_Density_Category', 'Delivery_Type']).size().unstack(fill_value=0)
    doc_density_counts['Total'] = doc_density_counts.sum(axis=1)
    doc_density_counts['C-section_Rate'] = (doc_density_counts['C-section'] / doc_density_counts['Total']) * 100

    # Midwife Density
    mid_density_counts = df.groupby(['Midwife_Density_Category', 'Delivery_Type']).size().unstack(fill_value=0)
    mid_density_counts['Total'] = mid_density_counts.sum(axis=1)
    mid_density_counts['C-section_Rate'] = (mid_density_counts['C-section'] / mid_density_counts['Total']) * 100

    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    # Plotting Doctor Density
    sns.barplot(x=doc_density_counts.index, y='C-section_Rate', data=doc_density_counts, palette='Blues_d',
                hue=doc_density_counts.index, legend=False, ax=axes[0])
    axes[0].set_title('C-section Rate by Doctor Density Category')
    axes[0].set_xlabel('Doctor Density Category')
    axes[0].set_ylabel('C-section Rate (%)')
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)

    # Plotting Midwife Density
    sns.barplot(x=mid_density_counts.index, y='C-section_Rate', data=mid_density_counts, palette='Greens_d',
                hue=mid_density_counts.index, legend=False, ax=axes[1])
    axes[1].set_title('C-section Rate by Midwife Density Category')
    axes[1].set_xlabel('Midwife Density Category')
    axes[1].set_ylabel('C-section Rate (%)')
    axes[1].grid(axis='y', linestyle='--', alpha=0.7)

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
        fig = generate_health_worker_impact_plot(df)
        plt.show()