import pandas as pd
import matplotlib.pyplot as plt

# Check if the columns exist
if 'Segment' in dataset.columns and 'Sales value' in dataset.columns:

    # Convert 'Sales value' to numeric
    dataset['Sales value'] = pd.to_numeric(dataset['Sales value'], errors='coerce')

    # Remove missing values
    dataset = dataset.dropna(subset=['Segment', 'Sales value'])

    # Group data by Segment
    grouped = dataset.groupby('Segment')['Sales value'].sum().reset_index()

    # Sort descending and keep top 6
    top6 = grouped.sort_values(by='Sales value', ascending=False).head(6)

    # Create the chart with transparent background
    fig, ax = plt.subplots(figsize=(10, 5), facecolor='none')
    ax.set_facecolor('none')

    # Bar chart
    ax.bar(top6['Segment'], top6['Sales value'], color='#12239E')

    # Title with spacing
    ax.set_title('', fontsize=22, color='#FFFFFF', pad=30)

    # Remove axis titles
    ax.set_xlabel('')
    ax.set_ylabel('')

    # Configure ticks
    ax.tick_params(axis='x', labelrotation=45, labelcolor='#FFFFFF', labelsize=18)
    ax.tick_params(axis='y', labelcolor='#FFFFFF', labelsize=10)

    # Subtle grid on Y axis
    ax.grid(axis='y', linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.show()

else:
    print("Make sure you have added the correct columns and their types.")
