# Hackathon/analyze_data/analysis_anc.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_anc_impact_plot(df): # <--- THIS LINE MUST START AT THE VERY LEFT EDGE
    """
    Generates a bar chart showing C-section rate by ANC Adequacy.
    Returns the matplotlib Figure object.
    """
    anc_delivery_counts = df.groupby(['ANC_Adequate', 'Delivery_Type']).size().unstack(fill_value=0)
    anc_delivery_counts['Total'] = anc_delivery_counts.sum(axis=1)
    anc_delivery_counts['C-section_Rate'] = (anc_delivery_counts['C-section'] / anc_delivery_counts['Total']) * 100

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=anc_delivery_counts.index, y='C-section_Rate', data=anc_delivery_counts, palette='viridis',
                hue=anc_delivery_counts.index, legend=False, ax=ax)
    ax.set_title('C-section Rate by ANC Adequacy')
    ax.set_xlabel('Adequate Antenatal Care (True/False)')
    ax.set_ylabel('C-section Rate (%)')
    ax.set_xticks(ticks=[0, 1], labels=['Inadequate ANC', 'Adequate ANC'])
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    fig.tight_layout()
    return fig

if __name__ == "__main__":
    # For standalone testing (uses clean_data.py for data loading, so it needs to be in a parent dir or accessible)
    # Note: For this to work directly, clean_data.py needs to be accessible,
    # often by adding its parent directory to sys.path or by running clean_data.py first.
    # The main app_ui.py handles this correctly by being at the Hackathon root.
    try:
        from clean_data import clean_and_transform_data
        df = clean_and_transform_data(raw_file_path='../data/raw_data.csv', clean_file_path='../data/clean_data_test.csv')
        if df is not None:
            fig = generate_anc_impact_plot(df)
            plt.show()
    except ImportError:
        print("Could not import clean_data. Please ensure clean_data.py is accessible for direct testing.")
    except FileNotFoundError:
        print("Raw data not found for direct testing. Ensure ../data/raw_data.csv exists.")