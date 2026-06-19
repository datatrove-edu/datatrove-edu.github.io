import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 1. Load your dataset
df = pd.read_csv("../weekly_deaths_united_states_only.csv")

# Filter for US national data and the actual Unweighted counts
df_filtered = df[(df['Jurisdiction'] == 'United States') & (df['Type'] == 'Unweighted')].copy()

# Parse date strings into datetime objects
df_filtered['Week Ending Date'] = pd.to_datetime(df_filtered['Week Ending Date'])

# Pivot table to obtain a timeseries per Cause Subgroup
df_pivot = df_filtered.pivot_table(
    index='Week Ending Date', 
    columns='Cause Subgroup', 
    values='Number of Deaths',
    aggfunc='sum'
)

# 2. Configure Paul Tol's colorblind-safe color cycle
color_palette = [
    "#332288", "#88CCEE", "#44AA99", "#117733", 
    "#999933", "#DDCC77", "#CC6677", "#882255", 
    "#AA4499", "#0077BB", "#EE7733", "#CC3311", "#000000"
]

# Alternate line styles to provide non-color cues
line_styles = [
    '-', '--', '-.', ':', 
    '-', '--', '-.', ':', 
    '-', '--', '-.', ':', '-'
]

# Set up clean canvas styling
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(12, 6), dpi=300)

# Sort cause subgroups by historical mean to match the visual stack hierarchy
sorted_columns = df_pivot.mean().sort_values(ascending=False).index

# Plot each line with a dedicated color-style pair
for i, col in enumerate(sorted_columns):
    ax.plot(
        df_pivot.index, 
        df_pivot[col], 
        label=col, 
        color=color_palette[i % len(color_palette)], 
        linestyle=line_styles[i % len(line_styles)],
        linewidth=1.75,
        alpha=0.9
    )

# 3. Labeling and Formatting
ax.set_title("US Weekly Deaths by Cause (Colorblind-Accessible)", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("Date", fontsize=11, labelpad=10)
ax.set_ylabel("Number of Deaths", fontsize=11, labelpad=10)

ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xlim(df_pivot.index.min(), df_pivot.index.max())
ax.set_ylim(bottom=0)

# Clean Year Ticks on the X-axis
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Two-column accessible legend positioned in the upper left
ax.legend(
    loc='upper left', 
    bbox_to_anchor=(0.01, 0.99), 
    ncol=2, 
    frameon=True, 
    facecolor='white', 
    framealpha=0.95, 
    edgecolor='none', 
    fontsize=9
)

plt.tight_layout()
plt.savefig('weekly_deaths_by_cause_US.png', dpi=150, bbox_inches='tight')
plt.close()  # Recommended to free up memory after saving