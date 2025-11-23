from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# 1. Lock paths to the *project* folder (Hearthfire-Social-Kitchen-Bar-Case-Study)
PROJECT_DIR = Path(__file__).resolve().parents[1]

# 2. Point to the raw CSV
csv_path = PROJECT_DIR / "data" / "raw" / "bar_food_sales_mix.csv"

# 3. Point to the folder where we want the chart saved
images_dir = PROJECT_DIR / "assets" / "images"
images_dir.mkdir(parents=True, exist_ok=True)

# 4. Load the data
df = pd.read_csv(csv_path)

# 5. Make the chart
plt.figure(figsize=(10, 6))
plt.bar(df["Category"], df["Sales ($)"])

plt.title("Margin Contribution by Category")
plt.xlabel("Category")
plt.ylabel("Sales ($)")

# Add the dollar labels on top of each bar
for idx, value in enumerate(df["Sales ($)"]):
    plt.text(idx, value + 50, f"${value:,}", ha="center", va="bottom", fontsize=9)

plt.tight_layout()

# 6. Save the figure in assets/images
output_file = images_dir / "category_sales_mix.png"
plt.savefig(output_file, dpi=300)

print(f"Saved figure to: {output_file}")
