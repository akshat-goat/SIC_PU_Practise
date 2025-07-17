# analyze_data/analysis_health_worker.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_plot(df):
    """
    Visualizes C-section rates by doctor and midwife density.
    Returns a matplotlib Figure object.
    """
    plt.style.use('seaborn-v0_8-talk')
    # Create a figure with two subplots (side-by-side)
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    # --- Plot 1: Doctor Density ---
    doc_rates = df.groupby('Doctor_Density_Category')['Delivery_Type'].apply(lambda x: (x == 'C-section').mean() * 100).reset_index()
    sns.barplot(
        data=doc_rates,
        x='Doctor_Density_Category',
        y='Delivery_Type',
        ax=axes[0],
        palette='Blues_d',
        order=['Low', 'Medium', 'High']
    )
    axes[0].set_title('C-section Rate by Doctor Density', fontsize=14, weight='bold')
    axes[0].set_xlabel('Doctor Density Category', fontsize=12)
    axes[0].set_ylabel('C-section Rate (%)', fontsize=12)
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)
    axes[0].set_ylim(0, 100)

    # --- Plot 2: Midwife Density ---
    midwife_rates = df.groupby('Midwife_Density_Category')['Delivery_Type'].apply(lambda x: (x == 'C-section').mean() * 100).reset_index()
    sns.barplot(
        data=midwife_rates,
        x='Midwife_Density_Category',
        y='Delivery_Type',
        ax=axes[1],
        palette='Greens_d',
        order=['Low', 'Medium', 'High']
    )
    axes[1].set_title('C-section Rate by Midwife Density', fontsize=14, weight='bold')
    axes[1].set_xlabel('Midwife Density Category', fontsize=12)
    axes[1].set_ylabel('') # Hide y-label for cleaner look
    axes[1].grid(axis='y', linestyle='--', alpha=0.7)
    axes[1].set_ylim(0, 100)
    
    # Add labels to bars for both plots
    for ax in axes:
        for container in ax.containers:
            ax.bar_label(container, fmt='%.1f%%')

    fig.suptitle('C-section Rate by Health Worker Density', fontsize=18, weight='bold')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to make room for suptitle
    return fig