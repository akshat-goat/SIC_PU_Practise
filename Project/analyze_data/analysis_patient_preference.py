# analyze_data/analysis_patient_preference.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_plot(df):
    """
    Visualizes C-section rates based on patient preference.
    Returns a matplotlib Figure object.
    """
    plt.style.use('seaborn-v0_8-talk')
    fig, ax = plt.subplots(figsize=(10, 7))

    # Calculate C-section rate by patient preference
    c_section_rates = df.groupby('Patient_Preference_Csection')['Delivery_Type'].apply(lambda x: (x == 'C-section').mean() * 100).reset_index()
    c_section_rates['Patient_Preference_Csection'] = c_section_rates['Patient_Preference_Csection'].map({True: 'Preferred C-section', False: 'Preferred Normal'})

    sns.barplot(
        data=c_section_rates,
        x='Patient_Preference_Csection',
        y='Delivery_Type',
        ax=ax,
        palette='bone'
    )

    ax.set_title('C-section Rate by Patient Preference', fontsize=16, weight='bold')
    ax.set_xlabel('Patient Preferred C-section (True/False)', fontsize=12)
    ax.set_ylabel('C-section Rate (%)', fontsize=12)
    ax.set_ylim(0, 100)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Add labels on bars
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f%%')

    fig.tight_layout()
    return fig