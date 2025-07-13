import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Pre-script setup: Create the DataFrame and remove duplicate rows
# This section is executed as a standard preamble to the main script

# dataset = pandas.DataFrame(Total Maintenance Time (hours), Cost of Purchased Parts, 
# Amount Spent (R$), Total Cost (Labor + Parts), Equipment Lifecycle (years), 
# Equipment Criticality, Failure Count)
# dataset = dataset.drop_duplicates()

# Rename columns to valid, simplified names
dataset.columns = [
    "Total Maintenance Time (hours)", "Cost of Purchased Parts", "Amount Spent (R$)",
    "Total Cost (Labor + Parts)"
]

# Remove missing values
data = dataset.dropna()

# Apply visual style without grid or background
sns.set_style("white")  # Removes background grid

# Pairplot with custom colors
g = sns.pairplot(
    data,
    diag_kind="kde",  # Kernel density estimate on diagonals
    plot_kws={
        "alpha": 0.8, "s": 60, "edgecolor": "none", "color": "#011184"
    },
    diag_kws={
        "fill": True, "color": "#011184", "linewidth": 0
    },
    corner=True
)

# Remove main figure title
g.fig.suptitle("")  # Ensures no title is shown

# Set figure background to fully transparent
g.fig.patch.set_alpha(0.0)

# Remove subplot axis backgrounds
for ax in g.axes.flat:
    if ax is not None:
        ax.set_facecolor("white")         # Or use (1,1,1,0) for full transparency
        ax.patch.set_alpha(0.0)

plt.tight_layout()
plt.show()
