# Hackathon/analyze_data/analysis_birth_spacing.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def generate_birth_spacing_impact_plot(df):
    """
    Generates violin plots showing the distribution of Maternal Age by IDI Category and Delivery Type.
    Returns the matplotlib Figure object.
    """
    df_idi = df[df['Birth_Order'] > 1].dropna(subset=['Inter_Delivery_Interval_Months', 'IDI_Category']).copy()

    if df_idi.empty:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.text(0.5, 0.5, "No data for birth spacing (IDI) analysis (requires Birth Order > 1 and valid IDI).",
                horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=12)
        ax.set_title('Inter-Delivery Interval Impact')
        ax.axis('off')
        return fig
    
    # Ensure IDI_Category is ordered (should be handled by clean_data.py)
    idi_order = ['Short (<18 months)', 'Optimal (18-59 months)', 'Long (60+ months)']
    df_idi['IDI_Category'] = pd.Categorical(df_idi['IDI_Category'], categories=idi_order, ordered=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(x='IDI_Category', y='Maternal_Age', hue='Delivery_Type', data=df_idi, split=True,
                   inner='quart', palette={'Normal': '#66b3ff', 'C-section': '#ff9999'}, ax=ax)
    ax.set_title('Maternal Age Distribution by IDI Category and Delivery Type')
    ax.set_xlabel('Inter-Delivery Interval Category')
    ax.set_ylabel('Maternal Age')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.legend(title='Delivery Type')
    fig.tight_layout()
    return fig

if __name__ == "__main__":
    # For standalone testing
    from clean_data import clean_and_transform_data
    df = clean_and_transform_data(raw_file_path='../data/raw_data.csv', clean_file_path='../data/clean_data_test.csv')
    if df is not None:
        fig = generate_birth_spacing_impact_plot(df)
        plt.show()