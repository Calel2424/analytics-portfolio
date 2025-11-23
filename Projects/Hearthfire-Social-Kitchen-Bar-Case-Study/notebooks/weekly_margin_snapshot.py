import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))          # hearthfire project root
CSV_PATH = os.path.join(BASE_DIR, "data", "raw", "weekly_margin_snapshot.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "assets", "images", "weekly_margin_snapshot.png")

# 2. Load CSV
df = pd.read_csv(CSV_PATH)

# 3. Plot a line chart with markers
plt.figure(figsize=(12, 6))
plt.plot(df["Day"], df["Margin_Pct"], marker="o", linewidth=3)

# 4. Add labels & formatting
plt.title("Weekly Margin % by Day", fontsize=16, weight="bold")
plt.xlabel("Day", fontsize=12)
plt.ylabel("Margin %", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.4)

# 5. Add value labels on each point
for i, value in enumerate(df["Margin_Pct"]):
    plt.text(i, value + 0.5, f"{value}%", ha="center", fontsize=10)

plt.tight_layout()

# 6. Save the visual
plt.savefig(OUTPUT_PATH, dpi=300)
print(f"Saved: {OUTPUT_PATH}")
