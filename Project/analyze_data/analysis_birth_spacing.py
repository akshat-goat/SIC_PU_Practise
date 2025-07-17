# analyze_data/analysis_birth_spacing.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_plot(df):
    """
    Visualizes the relationship between birth spacing, maternal age, and delivery type.
    Returns a matplotlib Figure object.
    """
    plt.style.use('seaborn-v0_8-talk')
    fig, ax = plt.subplots(figsize=(12, 8))

    # Filter for subsequent births that have an IDI category
    plot_data = df.dropna(subset=['IDI_Category'])
    
    # Define a custom color palette
    palette = {"Normal": "#90CAF9", "C-section": "#F48FB1"}


    sns.violinplot(
        data=plot_data,
        x='IDI_Category',
        y='Maternal_Age',
        hue='Delivery_Type',
        split=True,
        inner='quartile',
        palette=palette,
        ax=ax,
        order=['Short (<18 months)', 'Optimal (18-59 months)', 'Long (60+ months)']
    )

    ax.set_title('Maternal Age Distribution by IDI Category and Delivery Type', fontsize=16, weight='bold')
    ax.set_xlabel('Inter-Delivery Interval Category', fontsize=12)
    ax.set_ylabel('Maternal Age', fontsize=12)
    ax.legend(title='Delivery Type', loc='upper right')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    fig.tight_layout()
    return fig