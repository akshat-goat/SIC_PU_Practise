# analyze_data/analysis_time_of_day_week.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_plot(df):
    """
    Generates a heatmap of C-section rates by day of week and hour of day. [cite: 124]
    Returns a matplotlib Figure object. [cite: 87]
    """
    plt.style.use('seaborn-v0_8-talk')
    fig, ax = plt.subplots(figsize=(14, 9))

    # Create a pivot table for C-section rates [cite: 125]
    heatmap_data = df.pivot_table(
        values='Delivery_Type',
        index='Delivery_Day_of_Week',
        columns='Delivery_Time_Hour',
        aggfunc=lambda x: (x == 'C-section').mean() * 100
    )

    # Order the days of the week correctly
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    heatmap_data = heatmap_data.reindex(days_order)

    sns.heatmap(
        heatmap_data,
        ax=ax,
        cmap='YlGnBu',
        linewidths=.5,
        annot=True,
        fmt=".1f",
        annot_kws={"size": 9},
        cbar_kws={'label': 'C-section Rate (%)'}
    )

    ax.set_title('C-section Rate (%) by Day of Week and Hour of Day', fontsize=16, weight='bold')
    ax.set_xlabel('Hour of Day (24-hour)', fontsize=12)
    ax.set_ylabel('Day of Week', fontsize=12)
    
    fig.tight_layout()
    return fig