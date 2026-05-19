import pandas as pd
import matplotlib.pyplot as plt

userInput1 = input("Enter the filename without the filextension: SParam_")
userInput2 = "SParam_" + userInput1 + ".csv"

df = pd.read_csv(userInput2)

# 1. Processing
df['Timestamp'] = pd.to_datetime(df['Sample Name'].astype(str).str.extract(r'(\d{8}_\d{6})')[0], format='%Y%m%d_%H%M%S')
df['Type'] = df['Sample Name'].astype(str).apply(lambda x: 'Nickel' if 'ANA' in x else 'Zeolite')

# Filter out data points with unusually high error bars (> 0.002)
df = df[df['S Uncertainty'] <= 0.002]

# 2. Create a single plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Zeolite (Time Series)
zeolite_df = df[df['Type'] == 'Zeolite'].sort_values('Timestamp')

# Use .min() to guarantee the true earliest timestamp is used as the origin
start_time = zeolite_df['Timestamp'].min()
zeolite_df = zeolite_df.copy()
zeolite_df['Elapsed Hours'] = ((zeolite_df['Timestamp'] -
                               start_time).dt.total_seconds() / 3600) + 1

ax1.errorbar(zeolite_df['Elapsed Hours'], zeolite_df['S Parameter'], yerr=zeolite_df['S Uncertainty'],
             fmt='o-', color='teal', label='Zeolite', markersize=4, capsize=2, alpha=0.8)

# Formatting
ax1.set_xlabel('Elapsed Time (hrs)')
ax1.set_ylabel('S Parameter')
ax1.set_title('Zeolite S Parameter Over Time')
ax1.legend()
ax1.xaxis.set_major_locator(plt.MultipleLocator(1))
ax1.tick_params(axis='x', rotation=45)
ax1.set_xlim(left=0)

# Fixed y-axis range
ax1.set_ylim(0.54, 0.60)

ax1.annotate(
    'The power went out here and data collection had to be started again',                      # The label text
    xy=(2.5, 0.56),                       # Point the arrow is touching (x, y)
    xytext=(4, 0.55),                    # Where the text itself should live (x, y)
    arrowprops=dict(
        facecolor='black',               # Arrow color
        arrowstyle='->',                 # Arrow style ('->', '-|>', 'fancy')
        lw=1                           # Line width of the arrow
    ),
    fontsize=5,
    fontweight='bold'
)

plt.tight_layout()
plt.show()
