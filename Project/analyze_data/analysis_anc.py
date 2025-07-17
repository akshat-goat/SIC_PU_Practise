# analyze_data/analysis_anc.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_plot(df):
    """
    Visualizes C-section rate based on ANC adequacy. [cite: 104]
    Returns a matplotlib Figure object. [cite: 87]
    """
    plt.style.use('seaborn-v0_8-talk')
    fig, ax = plt.subplots(figsize=(10, 7))

    # Calculate C-section rate by ANC status [cite: 105]
    c_section_rates = df.groupby('ANC_Adequacy')['Delivery_Type'].apply(lambda x: (x == 'C-section').mean() * 100).reset_index()
    c_section_rates['ANC_Adequacy'] = c_section_rates['ANC_Adequacy'].map({True: 'Adequate ANC', False: 'Inadequate ANC'})

    sns.barplot(data=c_section_rates, x='ANC_Adequacy', y='Delivery_Type', ax=ax, palette='viridis')

    ax.set_title('C-section Rate by ANC Adequacy', fontsize=16, weight='bold')
    ax.set_xlabel('Antenatal Care (True/False)', fontsize=12)
    ax.set_ylabel('C-section Rate (%)', fontsize=12)
    ax.set_ylim(0, max(c_section_rates['Delivery_Type']) * 1.2)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Add labels on bars
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f%%')
        
    fig.tight_layout()
    return fig