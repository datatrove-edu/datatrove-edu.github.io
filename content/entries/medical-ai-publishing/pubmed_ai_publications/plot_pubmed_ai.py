import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ── Load data from CSV ────────────────────────────────────────────────
years, counts = [], []
with open('../PubMed_Timeline_Results_by_Year.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        y = int(row['Year'])
        c = int(row['Count'])
        if 2000 <= y <= 2025:
            years.append(y)
            counts.append(c)

# Sort ascending (PubMed exports descending)
years, counts = zip(*sorted(zip(years, counts)))
years, counts = list(years), list(counts)

# ── Exponential fit from 2014 ─────────────────────────────────────────
fit_idx = years.index(2014)
x_fit = np.array(years[fit_idx:]) - 2014
y_fit = np.array(counts[fit_idx:])
b, ln_a = np.polyfit(x_fit, np.log(y_fit), 1)
a = np.exp(ln_a)

x_curve = np.linspace(0, len(years) - 1 - fit_idx, 300)
y_curve = a * np.exp(b * x_curve)
x_curve_years = x_curve + 2014

# ── Plot ──────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 4), dpi=200)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

ax.plot(years, counts, color='#185FA5', linewidth=2,
        marker='o', markersize=4, label='Actual publications', zorder=3)
ax.plot(x_curve_years, y_curve, color='#D85A30', linewidth=2,
        linestyle='--', label='Exponential fit (2014–2025)', zorder=2)

ax.set_xlim(1999, 2026)
ax.set_xticks(range(2000, 2026, 2))
ax.tick_params(axis='x', rotation=45, labelsize=9)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(
    lambda v, _: f'{int(v/1000)}k' if v >= 1000 else str(int(v))))
ax.tick_params(axis='y', labelsize=9)
ax.set_ylabel('Publications', fontsize=10, color='#555')
ax.set_xlabel('Year', fontsize=10, color='#555')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#ccc')
ax.spines['bottom'].set_color('#ccc')
ax.yaxis.grid(True, color='#e8e8e8', linewidth=0.7)
ax.set_axisbelow(True)

ax.legend(fontsize=9, frameon=False, loc='upper left')

# caption = ('Source: PubMed search — ("artificial intelligence"[tiab] OR "machine learning"[tiab]) '
           # 'AND humans[MeSH] AND English[lang]. Accessed June 2026.')
# fig.text(0.5, -0.02, caption, ha='center', fontsize=7.5, color='#888')

plt.tight_layout()
plt.savefig('pubmed_ai_publications.png', dpi=200, bbox_inches='tight', facecolor='white')
print("Saved: pubmed_ai_publications.png")
