import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Rename columns
dataset.columns = ["Stage", "Total_Cost"]

# Clean data
df = dataset.dropna()

# Style without background
sns.set(style="white")

# Create figure with transparent background
fig, ax = plt.subplots(figsize=(9,6), facecolor='none')

# Violin plot with embedded boxplot and vibrant colors
sns.violinplot(
    data=df,
    x="Stage",
    y="Total_Cost",
    inner="box",
    palette="Set1",  # more vibrant color palette
    scale="width",
    ax=ax
)

# Adjust labels for dark background
ax.set_title("", fontsize=20, weight="bold", color='white')
ax.set_xlabel("Project stage", color='white')
ax.set_ylabel("Total Cost (R$)", color='white')
ax.tick_params(colors='white')
sns.despine()

# Keep the plot area background transparent
ax.set_facecolor("none")

# Final layout
plt.tight_layout()
plt.show()
