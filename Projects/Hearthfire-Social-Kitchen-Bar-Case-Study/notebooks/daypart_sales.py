from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# 1. Locate the CSV (relative to THIS file)
BASE_DIR = Path(__file__).resolve().parents[1]
csv_path = BASE_DIR / "data" / "raw" / "sales_covers_by_daypart.csv"

print(f"Loading CSV from: {csv_path}")

# 2. Read the CSV
df = pd.read_csv(csv_path)

# Debug: show the column names so we know what pandas sees
print("Columns in CSV:", list(df.columns))

# 3. Use the EXACT column names from your header
days = df["Day"]
hh_sales = df["HH_Sales"]
dinner_sales = df["Dinner_Sales"]
ln_sales = df["LN_Sales"]

# 4. Build a grouped bar chart
x = range(len(days))
bar_width = 0.25

plt.figure(figsize=(10, 6))

plt.bar([i - bar_width for i in x], hh_sales, width=bar_width, label="Happy Hour")
plt.bar(x, dinner_sales, width=bar_width, label="Dinner")
plt.bar([i + bar_width for i in x], ln_sales, width=bar_width, label="Late Night")

plt.xticks(x, days, rotation=45)
plt.ylabel("Sales ($)")
plt.title("Sales by Daypart Across the Week")
plt.legend()
plt.tight_layout()

# 5. Save the figure into assets/images
output_path = BASE_DIR / "assets" / "images" / "daypart_sales.png"
plt.savefig(output_path, dpi=300)

print(f"Saved figure to: {output_path}")

