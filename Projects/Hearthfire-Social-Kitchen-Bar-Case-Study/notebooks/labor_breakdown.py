import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Build path to the CSV (from the notebooks folder)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Hearthfire project root
csv_path = os.path.join(BASE_DIR, "data", "raw", "labor_breakdown.csv")

# 2. Read the data
df = pd.read_csv(csv_path)

# Make sure the column names match exactly what you have
# ['Day','FOH_Labor','BOH_Labor','Bar_Labor','Total_Labor','Labor_Pct']

# 3. Prepare figure
plt.figure(figsize=(10, 6))

days = df["Day"]
foh = df["FOH_Labor"]
boh = df["BOH_Labor"]
bar = df["Bar_Labor"]
labor_pct = df["Labor_Pct"]

# 4. Stacked bars for FOH / BOH / Bar
bar_width = 0.6

p1 = plt.bar(days, foh, bar_width, label="FOH Labor ($)")
p2 = plt.bar(days, boh, bar_width, bottom=foh, label="BOH Labor ($)")
p3 = plt.bar(days, bar, bar_width, bottom=foh + boh, label="Bar Labor ($)")

# 5. Add labor % labels above each stack
total_heights = foh + boh + bar
for x, height, pct in zip(days, total_heights, labor_pct):
    plt.text(
        x,
        height + 40,          # a little above the top
        f"{pct:.1f}%",
        ha="center",
        va="bottom",
        fontsize=9,
    )

# 6. Styling
plt.title("Daily Labor Breakdown by Area\n(FOH / BOH / Bar + Labor %)")
plt.ylabel("Labor Cost ($)")
plt.xlabel("Day")
plt.legend(loc="upper left")
plt.tight_layout()

# 7. Save the figure into assets/images
images_dir = os.path.join(BASE_DIR, "assets", "images")
os.makedirs(images_dir, exist_ok=True)

output_path = os.path.join(images_dir, "labor_breakdown.png")
plt.savefig(output_path, dpi=120)

print(f"Saved figure to: {output_path}")
